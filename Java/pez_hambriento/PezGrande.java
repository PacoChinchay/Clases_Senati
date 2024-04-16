import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class PezGrande extends Actor
{
    public void act()
    {
        seguirPezJugador();
        comerPezJugador();
    }
    
    private void seguirPezJugador() {
        PezJugador pezJugador = getWorld().getObjects(PezJugador.class).get(0);
        int angle = (int) Math.toDegrees(Math.atan2(pezJugador.getY() - getY(), pezJugador.getX() - getX()));
        setRotation(angle);
        move(1);
    }
    
    private void comerPezJugador() {
    if (!getWorld().getObjects(PezPequeño.class).isEmpty()) {
        PezJugador pezJugador = (PezJugador) getOneIntersectingObject(PezJugador.class);
        if (pezJugador != null) {
            getWorld().removeObject(pezJugador);
            ((MyWorld) getWorld()).perderJuego();
        }
    }
}


}
