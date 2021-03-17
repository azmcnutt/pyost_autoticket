# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file contains functions related to the pyost_autoticket  #
# Project.  Any questions can be sent via the github project at #
# https://github.com/azmcnutt/pyost_autoticket                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Project and files originaly create by James McNutt            #
# Put into the Public Domain or the betterment of mankind 2021  #
# https://unlicense.org                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


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


