import csv
import numpy as np 
import os

with open('Data/label.csv' , 'w' , newline = '') as csvfile :
    writer = csv.writer(csvfile)
    
    writer.writerow(['RawFileName' , 'RshapeFileName' , 'ReshapeFilePath' , 'EngName' , 'ChiName'])

    RawFilePath = 'Data/RawData'
    ReshapeFilePath = 'Data/ReshapeData'

    count = 0
    for rawfilename in os.listdir(RawFilePath):
        count = count + 1 
        reshapefilename = str(count) + '.jpg'
        writer.writerow([rawfilename , reshapefilename , ReshapeFilePath + '/' + reshapefilename , '0' , '0'])
