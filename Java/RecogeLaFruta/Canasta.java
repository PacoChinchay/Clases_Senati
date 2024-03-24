import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Canasta extends Actor
{
    public void act()
    {
        handleMove();
        recogerFruta();
    }
    
    private void handleMove() {
        if (Greenfoot.isKeyDown("left")) {
            move(-5);
        } else if(Greenfoot.isKeyDown("right")) {
            move(5);
        }
    }
    
     private void recogerFruta() {
        Fresa fresa = (Fresa) getOneIntersectingObject(Fresa.class);
        if(fresa != null) {
            ((MyWorld) getWorld()).incrementarContador();
            getWorld().removeObject(fresa);
        }
    }
}
