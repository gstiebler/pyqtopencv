
public class ImgProcess
{
    public static void process( GrayImg grayImg, RGBImg rgbImg ) {   
        int width = rgbImg.getWidth();
        int height = rgbImg.getHeight();
        for( int y = 0; y < height; ++y) {
            for( int x = 0; x < width; ++x ) {
                if( grayImg.getLum( x, y ) > 127 )
                    rgbImg.setRGB( x, y, (char) 255, (char) 0, (char) 0 );
            }
        }
    }  
}
