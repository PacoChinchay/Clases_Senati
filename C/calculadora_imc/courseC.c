#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    float peso;
    float altura;
    float imc;
    char mensaje[50];
    
    printf("Ingrese su peso en kg: ");
    scanf("%f", &peso);
    printf("Ingrese su altura en m: ");
    scanf("%f", &altura);
    
    imc = peso / (altura * altura);
    
    if (imc < 18.5) {
        strcpy(mensaje, "bajo");
    } else if (imc >= 18.5 && imc <= 24.9) {
        strcpy(mensaje, "normal");
    } else if (imc >= 25 && imc < 30) {
        strcpy(mensaje, "sobrepeso");
    } else {
        strcpy(mensaje, "morbido");
    }
    
    printf("\nPeso de: %f\nAltura de: %f\nSu IMC es de: %f\nDiagnóstico: %s", peso, altura, imc, mensaje);
    return 0;
}

