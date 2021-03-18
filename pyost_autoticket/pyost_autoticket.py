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



import functions as f



# lets get things started
f.l.info('PyOST_AutoTicket Starting.....')
f.l.debug('Loglevel is: %s (%s).', f.c.ll, f.c.llint)
f.l.info('Opening SQLite DB: %s', f.c.database)
db = f.db(f.c.database)
db.close()

