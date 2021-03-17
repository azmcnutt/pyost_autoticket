import configparser
import logging as l
import functions as f


config = configparser.ConfigParser()
config.read('pyost_autoticket.ini')
print (f.loglevel(config['pyost_autoticket']['loglevel']))
 
