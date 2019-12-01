import argparse
import logics
import os
import version
import sys
import convert
from os import path
import cache
import json

parser = argparse.ArgumentParser(description='RSS Newsreader system')
parser.add_argument(
    '--version',
    help='Print version info',
    action='store_true'

)
parser.add_argument(

    'source',
    type=str,
    #nargs='*',
    help='newslink on RSS',

)

parser.add_argument(
    '--json',
    help='print the news as JSON in stdout',
    action='store_true'

)

parser.add_argument(
    '--to-pdf',
    help='print  news on pdf file',
    action='store_true'

)


parser.add_argument(
    '--limit',
    type=int,
    default=1,
    help='limit of news(default=1)'
)
parser.add_argument(
    '--date',
    type=int,
    default=None,
    help='cached info'
)

my_namespace = parser.parse_args()
def urlWork():
    try:
        if my_namespace.source:
            infoDict=logics.getInfo(my_namespace.source,my_namespace.limit)
            return infoDict
    except:
        print('ERROR URL')
        return {}
CACHE={}
try:
    with open('cache.json') as j:
        CACHE=json.load(j)
except:
    pass
# with open('person.txt', 'w') as json_file:
#   json.dump(personDict, json_file)

TITLE='''

░░░░░░░░▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄░░░░░░░░░
░░░░░░▄▀░░▄▄▄▄▄▄▄▄▄▄▄░░▀▄░░░░░░░
░░░░░█░▄███████████████▄░█░░░░░░
░░░░░█░████████████████▀░█░░░░░░
░░░░░▀█▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄████▄░░░░
░░▄▄▄▄███████████████████░░██▄░░
▄▀░░░░░██████████████████▄██▀░▀▄
█▄░░░░░░▀█████████████▀▀▀▀░░░░▄█
▀█▄░░░░░░░▀█████████▀░░░░░░░░▄█▀
░▀██▄▄░░░░░░░░░░░░░░░░░░░░▄▄██▀░
░░░░▀███▄▄▄▄░░░░░░░░▄▄▄▄███▀░░░░
░░░░░░░░▀▀▀██████████▀▀▀░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░███████████████████████████░░
░░░█────█────█───█───█───█───█░░
░░░█─██─█─██─█─███─███─███─███░░
░░░█─████─██─█───█───█───█───█░░
░░░█─██─█─██─█─███─███─███─███░░
░░░█────█────█─███─███───█───█░░
░░░███████████████████████████░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''
divider1='░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
divider2='******************************************************************************************************************************'

os.system('clear')
print('\n\n\n')
print(TITLE)

try:
    cntr = 0
    infoDict=urlWork()
    if my_namespace.version:
        os.system('clear')
        print('VERSION = '+version.version)
        sys.exit()

#     if my_namespace.web:
#         web.web(infoDict)


    if my_namespace.to_pdf:
        pdfPath = path.join('./', 'news.pdf')
        convert.write_smth_to_pdf(pdfPath,convert.makeString(infoDict))

    if my_namespace.json:
        try:
            logics.print_json(infoDict)
            sys.exit()
        except:
           print('stdout error')

    else:
        if my_namespace.date :
            try:
                print(CACHE[str(my_namespace.date)])
                os.abort()
            except:
                print('not cache')
        else:
            os.system('clear')
            print (TITLE)
            for info in infoDict.values():
                if cntr < my_namespace.limit:
                    print("DATE: "+info['DATE']+'\n'+"TITLE: "+info['TITLE']+'\n'+divider2+'\n\n'+"INFO: "+info['INFO']+'\n\n'+"LINK: "+info['LINK']+'\n'+"IMG: "+info['IMG']+'\n'+divider1)
                    cntr+=1
                    cache.workCache(CACHE,info)
            with open('cache.json', 'w') as fp:
                json.dump(CACHE, fp)
            # print("CACHE:",CACHE)
except Exception as e:
    print('error news view: '+ str(e))



