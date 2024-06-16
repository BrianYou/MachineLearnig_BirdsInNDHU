import os
import cv2
import pandas as pd


path_obj = ('Data/ClassifyRawData')
path_tar = ('Data/dataset_tar_2')



for birddir in os.listdir(path_obj):
    path_birddir = os.path.join(path_obj,birddir)
    count = 0
    print(birddir)
    for filename in os.listdir(path_birddir):
        count = count+1
        print(filename + ' -> ' + 'img' + str(count) + '.jpg')
        path_tar_birddir = os.path.join(path_tar,birddir)
        
        img = cv2.imread( path_birddir + '/' + filename )
        res = cv2.resize(img , dsize = (256 ,256 ) , interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(path_tar_birddir + '/' + 'img' + str(count) + '.jpg',res)