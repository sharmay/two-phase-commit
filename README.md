# Two-Phase-Commit - TPC
PostgreSQL Two Phase Commit


## Python

A python script based Two Phase Demo using python PostgreSQL driver psycopg 3.x.

### Setup
```bash
cd python
python3 -m venv env
source env/bin/activate
pip install --update pip
pip install "psycopg[binary,pool]"
deavctivate
```

### Getting Usage

```bash
cd python
source env/bin/activate
python TPCDemo.py -h
```

### Execution

```bash
cd python
source env/bin/activate
python TPCDemo.py -c 'postgresql://localhost:5432/postgres' -c 'postgresql://localhost:5433/postgres' -d 'CREATE TABLE foo(a int)'
python TPCDemo.py -c 'postgresql://localhost:5432/postgres' -c 'postgresql://localhost:5433/postgres' -d 'CREATE TABLE bar(a int)'
deactivate
```

Note: connection can be repeated multiple times (do not pass duplicate connections)


