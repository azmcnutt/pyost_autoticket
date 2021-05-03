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
f.l.info('-----===== PyOST_AutoTicket Starting =====-----')
f.l.info('  Database:       %s', f.c.database)
f.l.info('  JSON API URL:   %s', f.c.ost_tickets_json_url)
f.l.info('  API Key:        Not shown for security')
f.l.info('  Log Level:      %s',f.c.ll)
f.l.info('  Test Mode:      %s',f.c.testmode)
f.l.info('Opening SQLite DB: %s', f.c.database)
db = f.db(f.c.database)




db.close()

