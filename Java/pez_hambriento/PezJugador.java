import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class PezJugador extends Actor
{
    public void act()
    {
        handleMove();
        comerPezPequeño();
        comerPezGrande();
    }
    
    private void handleMove() {
         if(Greenfoot.isKeyDown("up")) {
            setRotation(270);
            setLocation(getX(), getY()-3);
        }
        if(Greenfoot.isKeyDown("down")) {
            setRotation(90);
            setLocation(getX(), getY()+3);
        }
        if(Greenfoot.isKeyDown("left")) {
            setRotation(180);
            setLocation(getX()-3, getY());
        }
        if(Greenfoot.isKeyDown("right")) {
            setRotation(0);
            setLocation(getX()+3, getY());
        }
    }
    
    private void comerPezPequeño() {
    PezPequeño pezPequeño = (PezPequeño) getOneIntersectingObject(PezPequeño.class);
    if (pezPequeño != null) {
        getWorld().removeObject(pezPequeño);  
        ((MyWorld) getWorld()).getContador().sumarPunto();
        GreenfootImage image = getImage();
        image.scale(image.getWidth() + 1, image.getHeight() + 1);
        setImage(image);
    }
    }
    
    private void comerPezGrande() {
    if (getWorld().getObjects(PezPequeño.class).isEmpty()) {
        PezGrande pezgrande = (PezGrande) getOneIntersectingObject(PezGrande.class);
        if (pezgrande != null) {
            getWorld().removeObject(pezgrande);
            ((MyWorld) getWorld()).ganarJuego();
        }
    }
}


}
