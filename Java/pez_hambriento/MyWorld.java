import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class MyWorld extends World
{
    private Contador contador;
    private PezGrande pezgrande;
    private PezJugador pezjugador;
    private Instrucciones instrucciones;
    
    public MyWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1); 
        contador = new Contador();
        pezgrande = new PezGrande();
        pezjugador = new PezJugador();
        instrucciones = new Instrucciones();
        addObject(pezjugador, getWidth()/2, getHeight()/2);
        addObject(pezgrande, getWidth()/5, getHeight()/4);
        addObject(contador, 50, 50);
        prepararMundo();
        addObject(instrucciones, getWidth()/2, getHeight()/2);
    }
    
    public Contador getContador() {
        return contador;
    }
    
    private void prepararMundo() {
        for (int i = 0; i < 20; i++) {
            int x = Greenfoot.getRandomNumber(getWidth());
            int y = Greenfoot.getRandomNumber(getHeight());
            addObject(new PezPequeño(), x, y);
        }
    }
    
    public void act() {
        if (Greenfoot.isKeyDown("space")) {
            removeObject(instrucciones);
        }
    }
    
    public void ganarJuego() {
    showText("¡Has ganado!", getWidth()/2, getHeight()/2);
    Greenfoot.stop();
    }
    
    public void perderJuego() {
    showText("Game Over", getWidth()/2, getHeight()/2);
    Greenfoot.stop();
    }

}
