import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class PezPequeño extends Actor
{
    private int actos = 0;
    
    public void act()
    {
        mover();
    }
    
    private void mover() {
        actos++;
        if(actos % 60 == 0) {
         setRotation(Greenfoot.getRandomNumber(360));   
        }
        move(2);
    }
}
