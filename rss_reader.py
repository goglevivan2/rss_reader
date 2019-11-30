import argparse
import logics
import os
import version
import sys

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
    '--limit',
    type=int,
    default=None,
    help='limit of news(default=1)'
)

my_namespace = parser.parse_args()
def urlWork():
    try:
        if my_namespace.source:
            infoDict=logics.getInfo(my_namespace.source,my_namespace.limit)
            return infoDict
    except:
        print('ERROR URL')
        return ''

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
    if my_namespace.json:
        try:
            os.system('clear')
            logics.print_json(infoDict)
        except:
           print('stdout error')
    else:
        os.system('clear')
        print (TITLE)
        for info in infoDict.values():
            if cntr < my_namespace.limit:
                print("DATE: "+info['DATE']+'\n'+"TITLE: "+info['TITLE']+'\n'+divider2+'\n\n'+"INFO: "+info['INFO']+'\n\n'+"LINK: "+info['LINK']+'\n'+"IMG: "+info['IMG']+'\n'+divider1)
                cntr+=1
except Exception as e:
    print('error news view: '+ str(e))
    print(infoDict)


