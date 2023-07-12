#!/bin/sh

psql -U handle < /docker-entrypoint-initdb.d/pg/01_nas.sql
psql -U handle < /docker-entrypoint-initdb.d/pg/02_handles.sql
