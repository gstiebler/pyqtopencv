
public class GrayImg
{
    private int[] _data;
    private int _width;
    private int _height;
    
    public GrayImg( int[] data, int width, int height ) {
        _data = data;
        _width = width;
        _height = height;
    }
    
    public void setLum( int x, int y, char lum ) {
        int baseIndex = y * _width + x;
        _data[baseIndex] = lum;
    }
    
    public char getLum( int x, int y ) {
        int baseIndex = y * _width + x;
        return (char) _data[baseIndex];
    }
    
    public int getWidth() {
        return _width;
    }
    
    public int getHeight() {
        return _height;
    }

}