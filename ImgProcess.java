
public class ImgProcess
{
    public static void process( RGBImg rgbImg ) {   
        int xCenter = rgbImg.getWidth() / 2;
        int yCenter = rgbImg.getHeight() / 2;
        for( int y = yCenter - 10; y < yCenter + 10; ++y) {
            for( int x = xCenter - 10; x < xCenter + 10; ++x ) {
                rgbImg.setRGB( x, y, (char) 255, (char) 0, (char) 0 );
            }
        }
    }  
}
