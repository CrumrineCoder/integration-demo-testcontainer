from testcontainers.postgres import PostgresContainer

import sqlalchemy

with PostgresContainer("postgres:16") as postgres:

    psql_url = postgres.get_connection_url()

    engine = sqlalchemy.create_engine(psql_url)

    with engine.begin() as connection:

        version, = connection.execute(sqlalchemy.text("SELECT version()")).fetchone()

print(version)