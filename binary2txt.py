from tensorflow.keras.preprocessing.image import ImageDataGenerator
from skimage.io import imread,imsave,imshow
from skimage.measure import regionprops, label
import glob
import os
import numpy as np
import cv2
import json

im_path    = r'\gt'
save_path = r'\test'
mask_list = glob.glob(im_path + '\\*')

for i in range(len(mask_list)):
# for i in mask_list:
    # opencv 3.2
    ##read ori data
    path = im_path + '\\' + str(i) +'.bmp'
    mask = cv2.imread(path)[:,:,0]##if gt has 3layers
    ##

    m,n = mask.shape
    mask_new, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # before opencv 3.2
    # contours, hierarchy = cv2.findContours((mask).astype(np.uint8), cv2.RETR_TREE,
    #                                                    cv2.CHAIN_APPROX_SIMPLE)
    ''' 0:normal,1:CTS '''
    
    '''test'''
    if i <{your test data}:
        la = 0
    else:
        la = 1
    '''train'''
    # if int(i.split('\\')[-1].split('.')[0]) <{your train data}:
    #     la = 0
    # else:
    #     la = 1
    ''''''
    
    for contour in contours:
        contour = contour.flatten()
    
    x = contour[::2]/n  
    y = contour[1::2]/m
    
    f= open(save_path+'\\'+'%d.txt'%i,'w+')

    f.write('%d'%la)
    f.write(' ')
    for j in range(int(len(contour)/2)):
        f.write(str(x[j]))
        f.write(' ')
        f.write(str(y[j]))
        f.write(' ')
    f.close()

'''grab validation data'''
##val data(179)
val = []##filename ex:0.jpg, 1.jpg, 2.jpg... =>val = ['0','1','2'...]

file_source = r'\train'
file_destination = r'\valid'
val_file = []
d_file = [] 
for i in val:
    val_file.append(file_source + '\\' + i + '.bmp')
    d_file.append(file_destination + '\\' + i + '.bmp')
    
for g in range(len(val)):
    os.replace(val_file[g], d_file[g])
