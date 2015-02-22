
public class PreProcess
{
    public static void preProcess(  int[] grayData, int[] rgbData, int width, int height ) {
        GrayImg grayImg = new GrayImg( grayData, width, height );
        RGBImg rgbImg = new RGBImg( rgbData, width, height );
        ImgProcess.process( grayImg, rgbImg );
    }
    
}