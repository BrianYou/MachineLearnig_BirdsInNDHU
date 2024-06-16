import cv2
import numpy as np 
import os
from matplotlib import pyplot as plt

def read_path():
    obj_path = 'Data/dataset_obj/Monticola_solitarius'
    tar_path = 'Data/dataset_tar/Monticola_solitarius'
    count = 0
    os.makedirs(tar_path)
    for filename in os.listdir(obj_path):
        count = count + 1 
        print(filename)
        img = cv2.imread( obj_path + '/' + filename )
        cv2.imwrite(tar_path + '/' + 'img' + str(count) + '.jpg',img)

read_path()






"""
img = cv2.imread('Data/ReshapeData/DSCN0007.JPG')
res = cv2.resize(img , dsize = (64 ,64 ) , interpolation = cv2.INTER_CUBIC)

cv2.imwrite('Data/ReshapeData/res64.jpg' , res)


cv2.imshow("res",res)
cv2.waitKey(0)
"""