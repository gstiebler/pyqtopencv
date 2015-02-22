
public class PreProcess
{
    public static void preProcess(  int[] data, int width, int height ) {
        RGBImg rgbImg = new RGBImg( data, width, height );
        ImgProcess.process( rgbImg );
    }
    
}