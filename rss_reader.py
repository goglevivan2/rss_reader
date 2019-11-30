import argparse
import logics
import os

parser = argparse.ArgumentParser(description='RSS Newsreader system')
parser.add_argument(
    'chars',
    type=str,
    default='http://news.yahoo.com/rss/',
    help='newslink on RSS'
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
        infoDict=logics.getInfo(my_namespace.chars,my_namespace.limit)
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
    if my_namespace.json:
        try:
            os.system('clear')
            logics.print_json(infoDict)
        except:
           print('stdout error')
    else:
        for info in infoDict.values():
            if cntr < my_namespace.limit:
                print("DATE: "+info['DATE']+'\n'+"TITLE: "+info['TITLE']+'\n'+divider2+'\n\n'+"INFO: "+info['INFO']+'\n\n'+"LINK: "+info['LINK']+'\n'+"IMG: "+info['IMG']+'\n'+divider1)
                cntr+=1
except Exception as e:
    print('error news view: '+ str(e))
    print(infoDict)


