from os import path
import weasyprint

def write_smth_to_pdf(pdfPath,smth):
    '''write some information to pdf files'''
    html_weasy = weasyprint.HTML(string=smth)
    html_weasy.write_pdf(pdfPath)


pdfPath=path.join('./', 'news.pdf')
write_smth_to_pdf(pdfPath,'Goglev')