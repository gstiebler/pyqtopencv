
import numpy as np
from jnius import autoclass

def process( src_img ):
    height, width = src_img.shape[:2]
    ImgProcess = autoclass('ImgProcess')
    
    shape = src_img.shape
    num_channels = 3
    bytesArray = np.reshape( src_img, ( width * height * 3 ) )
    bytesList = bytesArray.tolist()
    ImgProcess.process( bytesList, width, height )
    newArray = np.asarray( bytesList )
    newArray = newArray.astype( 'uint8' )
    return np.reshape( newArray, shape )