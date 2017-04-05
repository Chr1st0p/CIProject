import os


class Paths:
    def __init__(self):
        pass

    rcv1DataHome = 'E:\Anaconda\Anaconda\packages\data'
    textPath = os.path.dirname(os.getcwd()) + '\\CIProject2\\MyApp\\static\\text\\'

    pklDataPath = os.path.dirname(os.getcwd()) + '\\CIProject2\\MyApp\\static\\storeddata\\'
    keywordspath = os.path.dirname(os.getcwd()) + '\\keywords\\'
    imagespath = os.path.dirname(os.getcwd()) + '\\CIProject2\\MyApp\\static\\images\\'
    csvpath = os.path.dirname(os.getcwd()) + '\\CIProject2\\MyApp\\static\\csvs\\'
