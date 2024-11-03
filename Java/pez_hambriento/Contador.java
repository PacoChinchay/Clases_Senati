import greenfoot.*; // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Contador extends Actor
{
    private int total = 0;

    public void act() {
        setImage(new GreenfootImage("Puntos: " + total, 24, Color.WHITE, new Color(0, 0, 0, 0)));
    }

    public void sumarPunto() {
        total++;
    }
}

