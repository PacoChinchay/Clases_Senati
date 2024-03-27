import greenfoot.*; // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Instrucciones extends Actor
{
    public Instrucciones() {
        GreenfootImage image = new GreenfootImage(600, 250);
        image.setColor(Color.BLACK); 
        image.fill(); 
        image.setColor(Color.WHITE); 
        image.setFont(new Font(24));
        image.drawString("Pez Hambriento", 20, 30);
        image.drawString("tu objetivo es comerte a todos los peces pequeños", 20, 60);
        image.drawString("antes de que el pez rojo te alcance y te coma", 20, 90);
        image.drawString("cuando logres acabar con los peces pequeños", 20, 120);
        image.drawString("entonces podrás comerte al pez rojo.", 20, 150);
        image.drawString("presiona SPACE antes de comenzar", 20, 180);
        setImage(image);
    }
}

