#include <stdio.h>

int main() {
    char operacion;
    double numero1, numero2, total;
    
    printf("ingrese su operaci%cn: suma(+), resta(-), multiplicaci%cn(*), divisi%cn(/): ", 162, 162, 162);
    scanf("%c", &operacion);
    
    printf("Ingrese el n%cmero 1: \n", 163);
    scanf("%lf", &numero1);

    printf("Ingrese el n%cmero 2: \n", 163);
    scanf("%lf", &numero2);

    switch (operacion)
    {
    case '+': total = numero1 + numero2;
        break;
    case '-': total = numero1 - numero2;
        break;
    case '*': total = numero1 * numero2;
        break;
    case '/': total = numero1 / numero2;
        break;
    
    default: printf("operaci%cn invalida", 162);
        break;
    }

    printf("\nel resultado de la opeaci%cn es: %.2lf", 162, total);
    return 0;
}