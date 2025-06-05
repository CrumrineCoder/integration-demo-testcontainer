from testcontainers.core.container import DockerContainer
import requests
import time

def test_flask_services_communicate():
    with DockerContainer("service-b") \
        .with_exposed_ports(5001) \
        .with_command("python app.py") as service_b:

        service_b_port = service_b.get_exposed_port(5001)

        with DockerContainer('service-a') \
            .with_exposed_ports(5000) \
            .with_env("SERVICE_B_URL", f"http://host.docker.internal:{service_b_port}") \
            .with_command("python app.py") as service_a:

            service_a_port = service_a.get_exposed_port(5000)

            for _ in range(10):
                try:
                    r = requests.get(f"http://localhost:{service_a_port}/trigger")
                    assert "Hello from B" in r.text
                    return
                except Exception:
                    time.sleep(1)
            
            raise AssertionError("Service A failed to communicate with Service B")