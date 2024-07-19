#!/usr/bin/env python3

'''
Update postgresql.conf and change max_prepared_transactions 1 or more
ex: max_prepared_transactions = 10

Setup virtual env for python
$ python -m venv env

Enter the virtual env
$ source env/bin/activate

Upgrade pip
$ pip install --upgrade pip

Install psycopg 3.x
$ pip install "psycopg[binary,pool]"

Note: Always run TPCDemo inside venv

To exit venv
$ deactivate

'''

import argparse
import psycopg
def ExecuteTPC(conns, ddl):
    connections=[]
    xids=[]
    try:
        for i in range(len(conns)):
            try:
                print("Connecting to", conns[i])
                connections.append(psycopg.connect(conns[i]))
                print("XID", conns[i])
                xids.append(connections[i].xid(10, "tpc", conns[i]))
                print("tpc_begin", conns[i])
                connections[i].tpc_begin(xids[i])
            except:
                print("Failed to connect/xids/begin to", conns[i])
                raise

        for i in range(len(conns)):
            try:
                print("Cursor execute", conns[i])
                with connections[i].cursor() as cursor:
                    cursor.execute(ddl)
            except:
                print("Failed to execute ddl to", conns[i])
                raise

        for i in range(len(conns)):
            try:
                print("tpc_prepare", conns[i])
                connections[i].tpc_prepare()
            except:
                print("Failed to tpc_prepare", conns[i])
                raise
        for i in range(len(conns)):
            try:
                print("tpc_commit", conns[i])
                connections[i].tpc_commit()
            except:
                print("Failed to commit", conns[i])
                raise
    except:
        print("Rollback")
        for i in range(len(conns)):
            print("tpc_rolllback", conns[i])
            connections[i].tpc_rollback()
    finally:
        for i in range(len(conns)):
            try:
                print("Close", conns[i])
                connections[i].close()
            except:
                print("Failed to close connection", conns[i])
                raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='TPCDemo',
                    description='Two Phase Commit Demo')

    parser.add_argument('-c', '--con', action='append', required=True, help='PostgreSQL connection string, this parameter can be repeated, ex: postgresql://<user>:<password>@<host>:<port>/<dbname>')
    parser.add_argument('-d', '--ddl', required=True, help='DDL to execute on all the connections')
    args = parser.parse_args()
    ExecuteTPC(args.con, args.ddl)


