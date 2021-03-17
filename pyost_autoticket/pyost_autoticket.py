# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# pyost_autoticket - automatically creates tickets in osTicket  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Any questions can be sent via the github project at           #
# https://github.com/azmcnutt/pyost_autoticket                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Project and files originaly create by James McNutt            #
# Put into the Public Domain or the betterment of mankind 2021  #
# https://unlicense.org                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import configparser
import logging as l
import functions as f


config = configparser.ConfigParser()
config.read('pyost_autoticket.ini')
print (f.loglevel(config['pyost_autoticket']['loglevel']))
 
