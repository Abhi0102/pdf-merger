import os
from PyPDF2 import PdfFileMerger
import logging
from datetime import datetime

def getFiles(path):
    """
    The function accepts the path of the directory and returns a dictionary having all files, pdf files and path as key.
    Example path : C:\\User\\Folder...
    :param path: string, path of directory
    :return: dict, having all files, pdf files and path of directory
    """
    logging.info('Inside getFiles')
    list_of_files = os.listdir(path)
    file_dict = {'all_files': [], 'pdf_files': [], 'path': path}
    logging.info('Files Fetched.. Path is correct..')
    for i in list_of_files:
        file_dict['all_files'].append(i)
        if(i.endswith('.pdf')):
            logging.info('PDF file - ', i)
            file_dict['pdf_files'].append(i)

    logging.info('Returning from Files Fetched')
    return file_dict

def mergePDF(path,pdfs):
    '''
    The function merges all pdf files and save in that directory.
    :param path: string, path of the directory
    :param pdfs: list of the name of pdfs in that directory eg.:[a.pdf,b.pdf...]
    :return: Null
    '''
    logging.info('Inside mergePDF')
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(open(path+'\\'+pdf,'rb'))
        logging.info('Merged- %s',pdf)
    pdf_file_name = 'result '+ str(datetime.now().month) +'-'+str(datetime.now().year)+'-'+str(datetime.now().minute)+'-'+str(datetime.now().second) + '.pdf';
    with open(path+'\\'+pdf_file_name, 'wb') as fout:
        merger.write(fout)
    logging.info('Merged Complete')
    return



