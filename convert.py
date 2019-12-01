from os import path
import weasyprint


divider1='░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
divider2='******************************************************************************************************************************'

def makeString(infdir):
    '''

    make string of informations
    '''
    values =infdir.values()
    strngAnswer='     NEWSRSSREADER     '+divider1+divider1
    for v in values:
        strngAnswer +="DATE: "+v['DATE']+'\n'+"TITLE: "+v['TITLE']+'\n'+divider2+'\n\n'+"INFO: "+v['INFO']+'\n\n'+"LINK: "+v['LINK']+'\n'+"IMG: "+v['IMG']+'\n'+divider1

    return strngAnswer




def write_smth_to_pdf(pdfPath,smth):
    '''write some information to pdf files'''
    try:
        weasy = weasyprint.HTML(string=smth)
        weasy.write_pdf(pdfPath)
        print('Success! Open news.pdf')
    except Exception as e:
        print('pdf convert error:'+str(e))


