
import cv2
import numpy as np
from jnius import autoclass

def process( src_img ):
    height, width = src_img.shape[:2]
    PreProcess = autoclass('PreProcess')
    
    shape = src_img.shape
    num_channels = 3
    colorBytesArray = np.reshape( src_img, ( width * height * num_channels ) )
    colorBytesList = colorBytesArray.tolist()
    
    gray_image = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    grayBytesArray = np.reshape( gray_image, ( width * height ) )
    grayBytesList = grayBytesArray.tolist()
    
    PreProcess.preProcess( grayBytesList, colorBytesList, width, height )
    
    colorNewArray = np.asarray( colorBytesList )
    colorNewArray = colorNewArray.astype( 'uint8' )
    return np.reshape( colorNewArray, shape )
    