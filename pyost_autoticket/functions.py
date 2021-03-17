def loglevel(i):
    switcher={
        'debug':10,
        'info':20,
        'warning':30,
        'error':40,
        'critical':50
    }
    return switcher.get(i.lower(),10)


