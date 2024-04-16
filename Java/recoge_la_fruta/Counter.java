import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Counter extends Actor
{
    private int value = 0;
    private String text;
    private GreenfootImage background;
    
    public Counter(String prefix) {
        text = prefix;
        background = getImage();
        updateImage();
    }
    
    public void increment() {
        value++;
        updateImage();
    }
    
    private void updateImage() {
        GreenfootImage image = new GreenfootImage(background);
        GreenfootImage textImage = new GreenfootImage(text + value, 20, Color.WHITE, new Color(0,0,0,0));
        image.drawImage(textImage, (image.getWidth()-textImage.getWidth())/2, (image.getHeight()-textImage.getHeight())/2);
        setImage(image);
    }
    
    public void act()
    {
        // Add your action code here.
    }
}
