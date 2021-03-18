# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file contains functions related to the pyost_autoticket  #
# Project.  Any questions can be sent via the github project at #
# https://github.com/azmcnutt/pyost_autoticket                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Project and files originaly create by James McNutt            #
# Put into the Public Domain or the betterment of mankind 2021  #
# https://unlicense.org                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import configparser
import sqlite3
from sqlite3 import Error
import logging



# Returns the log level in based on the text name.  Returns the value for logging.DEBUG if no match
def loglevel(i):
    switcher={
        'debug':10,
        'info':20,
        'warning':30,
        'error':40,
        'critical':50
    }
    return switcher.get(i.lower(),10)

class c:
    config = configparser.ConfigParser()
    config.read('pyost_autoticket.ini')
    database = config['pyost_autoticket']['database']
    ost_tickets_json_url = config['pyost_autoticket']['ost_tickets_json_url']
    ost_apikey = config['pyost_autoticket']['ost_apikey']
    ll = config['pyost_autoticket']['loglevel']
    llint = loglevel(ll)
    testmode = config['pyost_autoticket']['testmode']

class db:
    conn = None
    def __init__(self, dbfile):
        try:
            l.info('Python SQLite Ver: %s', sqlite3.version)
            self.conn = sqlite3.connect(dbfile)
            l.debug('Database Conn: %s', self.conn)
        except Error as e:
            print(e)

        self.checkSchema()

    def close(self):
        self.conn.close()
        l.info('SQLite connection closed')

    def checkSchema(self):
        l.debug('Checking DB Schema.....')
        c = self.conn.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tickets' ''')
        if c.fetchone()[0]!=1:
            l.debug('Create table tickets....')
            table_tickets = """CREATE TABLE "tickets" (
	                            "id"	INTEGER NOT NULL UNIQUE,
	                            "frequency"	TEXT NOT NULL DEFAULT 'DAILY',
	                            "dayofweek"	TEXT,
	                            "dayofthemonth"	INTEGER,
	                            "monthoftheyear"	INTEGER,
	                            "alert"	INTEGER NOT NULL DEFAULT 1,
	                            "autorespond"	INTEGER NOT NULL DEFAULT 1,
	                            "source"	TEXT NOT NULL DEFAULT 'API',
	                            "topicId"	INTEGER NOT NULL,
	                            "name"	TEXT NOT NULL,
	                            "email"	TEXT,
	                            "phone"	TEXT,
	                            "subject"	TEXT NOT NULL,
	                            "ip"	TEXT DEFAULT '0.0.0.0',
	                            "message"	TEXT,
	                            "lastDate"	TEXT NOT NULL DEFAULT '1970-01-01',
	                            "nextDate"	TEXT NOT NULL DEFAULT '1970-01-01',
	                            "enabled"	INTEGER NOT NULL DEFAULT 1,
	                            PRIMARY KEY("id" AUTOINCREMENT)
                            )"""
            try:
                c = self.conn.cursor()
                c.execute(table_tickets)
                l.debug('Table tickets created.')
            except Error as e:
                print(e)
            
        self.conn.commit()




# set up basic logging depending on loglevel from config file
# log to file and screen
# Default logging level is Debug
global l
l = logging
l.basicConfig(filename='pyost_autoticket.log', level=c.llint)
console = l.StreamHandler()
console.setLevel(c.llint)
l.getLogger().addHandler(console)
