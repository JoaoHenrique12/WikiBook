DROP schema public CASCADE;
CREATE schema public;

\i docker-entrypoint-initdb.d/ddl.sql
