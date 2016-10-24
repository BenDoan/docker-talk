#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER docker PASSWORD 'dbpass';
    CREATE DATABASE click_counter;
    GRANT ALL PRIVILEGES ON DATABASE click_counter TO docker;
EOSQL
