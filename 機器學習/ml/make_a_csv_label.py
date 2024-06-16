import numpy as np 
import os
from matplotlib import pyplot as plt
import csv
import cv2

path = ('Data/dataset_tar')
with open('Data/dataset_label.csv' , 'w' , newline = '') as csvfile :
    writer = csv.writer(csvfile)
    writer.writerow(['filename' , 'label'])

    for filename in os.listdir(path):
        dirname = filename
        tar_path = (path + '/' + filename)
        print(tar_path)
        for filename in os.listdir(tar_path):
            write_in_file_name = (dirname + '/' + filename)
            writer.writerow([write_in_file_name,dirname])