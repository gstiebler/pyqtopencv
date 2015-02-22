
public class ImgProcess
{
    public static void process( int[] data, int width, int height )  
    {   
        int channels = 3;
        int xCenter = width / 2;
        int yCenter = height / 2;
        int lineSize = width * channels;
        for( int y = yCenter - 10; y < yCenter + 10; ++y)
        {
            for( int x = xCenter - 10; x < xCenter + 10; ++x )
            {
                int baseIndex = y * lineSize + x * channels;
                data[baseIndex] = 0;
                data[baseIndex + 1] = 0;
                data[baseIndex + 2] = 255;
            }
        }
    }  
}
