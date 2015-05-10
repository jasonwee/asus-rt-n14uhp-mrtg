#!/usr/bin/python


import MySQLdb as mdb
import sys
import pycurl
import time
import yaml
from StringIO import StringIO


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

# click 'network Map' then table 'System Status' click tab Status
def get_cpu_stat_from_router(config):
    """get cpu statistics in percentage from router."""
    time = lambda: int(round(time.time() * 1000))
    headers = ['Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
               'Accept-Encoding: gzip, deflate',
               'Accept-Language: en-US,en;q=0.5',
               'Authorization: Basic %s' % (config['router_auth']),
               'Connection: keep-alive',
               'Cookie: dm_install=no; dm_enable=no; hwaddr=%s; apps_last=; notification_history=1,0,0,0,0,0,0,0; bw_rtab=WIRELESS0; bw_24tab=INTERNET; bw_24refresh=1' % (config['router_mac']),
               'Host: %s' % (config['router_ip']),
               'Referer: http://%s/device-map/router_status.asp' % (config['router_ip']),
               'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0 Iceweasel/37.0.1',
               'X-Requested-With: XMLHttpRequest']
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://%s/cpu_status.asp?_=%s' % (config['router_ip'],
                                                       time))
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    return body

# click 'network Map' then table 'System Status' click tab Status
def get_mem_stat_from_router(config):
    """get ram statistics in percentage form router."""
    time = lambda: int(round(time.time() * 1000))
    headers = ['Host: %s' % (config['router_ip']),
               'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0 Iceweasel/37.0.1',
               'Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
               'Accept-Language: en-US,en;q=0.5',
               'Accept-Encoding: gzip, deflate',
               'X-Requested-With: XMLHttpRequest',
               'Referer: http://%s/device-map/router_status.asp' % (config['router_ip']),
               'Cookie: dm_install=no; dm_enable=no; hwaddr=%s; apps_last=; notification_history=1,0,0,0,0,0,0,0; bw_rtab=WIRELESS0; bw_24tab=INTERNET; bw_24refresh=1' % (config['router_mac']),
               'Authorization: Basic %s' % (config['router_auth']),
               'Connection: keep-alive']
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://%s/ram_status.asp?_=%s' % (config['router_ip'],
                                                       time))
    c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    return body


if __name__ == '__main__':
    con=""
    try:
        stream = open("../conf/config.yaml", "r")
        config = yaml.load(stream)
        #print config

        cpu_perc = get_cpu_stat_from_router(config)
        print cpu_perc

        mem_perc = get_mem_stat_from_router(config)
        print mem_perc
        
        #con = mdb.connect(config['db_host'], config['db_user'], config['db_pass'], config['db_name']);
        #version = get_db_version(con)
        #print "Database version: %s " % version

        #rows = get_data(con)
        #print rows[0]

    except yaml.YAMLError, e:
        if hasattr(e, 'problem mark'):
            mark = e.problem_mark
            print "Error position: (%s:%s)" % (mark.line+1, mark.column+1)
        else:
            print "Error in configuration file:", e
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()
