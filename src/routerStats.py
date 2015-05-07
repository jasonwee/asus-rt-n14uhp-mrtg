#!/usr/bin/python


import MySQLdb as mdb
import sys


def get_db_version(con):
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    return ver

def create_table(con):
    cur = con.cursor() 
    cur.execute("create table bw_internet ( timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, rx bigint unsigned DEFAULT 0, tx bigINT unsigned DEFAULT 0, PRIMARY KEY (timestamp) )")

def add_data(con, data):
    cur = con.cursor() 
    cur.execute("INSERT INTO bw_internet(rx, tx) VALUES('%s', '%s')" % (data.get("rx"), data.get("tx")))
    return cur.rowcount

def get_data(con):
    # if you use the following, you can refer to the tuple by the db table column name.
    #cur = con.cursor(mdb.cursors.DictCursor)
    cur = con.cursor()
    #  cur.description   to print header name print "%s %3s" % (desc[0][0], desc[1][0])
    cur.execute("SELECT * FROM bw_internet")
    rows = cur.fetchall()
    return rows

def update_data(con, data):
    cur = con.cursor()
    cur.execute("UPDATE bw_internet SET rx = %s, tx = %s WHERE timestamp = %s", (data.get(""), data.get(""), data.get("")))
    return cur.rowcount

if __name__ == '__main__':
    try:
        #TODO read from config file.
        con = mdb.connect('localhost', 'user', 'test', 'monitor');
        version = get_db_version(con)
        print "Database version: %s " % version

        rows = get_data(con)
        print rows[0]

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()
