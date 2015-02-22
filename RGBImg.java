
public class RGBImg
{
    private int[] _data;
    private int _width;
    private int _height;
    private int _channels = 3;
    private int _lineSize;
    
    public RGBImg( int[] data, int width, int height ) {
        _data = data;
        _width = width;
        _height = height;
        _lineSize = _width * _channels;
    }
    
    public void setRGB( int x, int y, char r, char g, char b ) {
        int baseIndex = y * _lineSize + x * _channels;
        _data[baseIndex] = b;
        _data[baseIndex + 1] = g;
        _data[baseIndex + 2] = r;
    }
    
    public int getWidth() {
        return _width;
    }
    
    public int getHeight() {
        return _height;
    }

}