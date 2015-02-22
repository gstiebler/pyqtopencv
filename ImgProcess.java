
public class ImgProcess
{
    public static void process( GrayImg grayImg, RGBImg rgbImg, int difMin ) {   
        int width = rgbImg.getWidth();
        int height = rgbImg.getHeight();
        int dy = 2;
        for( int y = dy; y < height - dy; ++y) {
            for( int x = 0; x < width; ++x ) {
                char currLum = grayImg.getLum( x, y );
                char prevLum = grayImg.getLum( x, y - dy );
                char nextLum = grayImg.getLum( x, y + dy );
                
                boolean upDif = (currLum - prevLum) > difMin;
                boolean downDif = (currLum - nextLum) > difMin;
                
                //if ( upDif )
                 //   rgbImg.setRGB( x, y - dy, (char) 255, (char) 0, (char) 0 );
                
                //if ( downDif )
                //    rgbImg.setRGB( x, y + dy, (char) 0, (char) 255, (char) 0 );
                
                if ( downDif && upDif )
                    rgbImg.setRGB( x, y + dy, (char) 255, (char) 255, (char) 0 );
            }
        }
    }  
}
