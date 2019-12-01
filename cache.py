import datetime

def changeOfDate(date):
    '''
     Date in format "Thu, 28 Nov 2019 10:22:41 -0500" ->to format "20191128"
    '''
    try:
        objectOfDatetime = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')
        date = str(objectOfDatetime.year) + str(objectOfDatetime.month) + str(objectOfDatetime.day)
    except Exception as ex:
        print('date change error: '+print(ex))
    return date

def workCache(cache,info):
    try:
        cache[changeOfDate(info["DATE"])].append({'DATE':info['DATE'],'TITLE':str(info['TITLE']),'INFO':str(info["INFO"])})
    except:
        cache[changeOfDate(info["DATE"])] = [info]
