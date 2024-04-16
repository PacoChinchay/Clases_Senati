import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class MyWorld extends World
{
    private int objectCreationDelay = 0;
    private Counter counter;
    private Canasta canasta;
    
    public void act() {
        generarFresas();
    }
    
    public MyWorld()
    {    
        super(600, 400, 1);
        counter = new Counter("Puntos: ");
        canasta = new Canasta();
        addObject(canasta, 300, 370);
        addObject(counter, 60, 45);
    }
    
    public void incrementarContador() {
        counter.increment();
    }
    
    public void generarFresas() {
        if(objectCreationDelay == 0) {
          int position = Greenfoot.getRandomNumber(getWidth());  
          addObject(new Fresa(), position, 0);
          objectCreationDelay = 50;
        } else {
            objectCreationDelay--;
        }
    }
    
    
    
}
