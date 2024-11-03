#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    const int MIN = 1;
    const int MAX = 100;

    int intento;
    int intentos = 0;
    int respuesta;

    srand(time(0));

    respuesta = (rand() % MAX) + MIN;

    do {
        printf("elige un numero: ");
        scanf("%d", &intento);

        if (intento < respuesta) {
            printf("Muy Bajo!!\n");
        } else if (intento > respuesta) {
            printf("Muy Alto!!\n");
        } else {
            printf("Correcto!!\n");
        }
        intentos++;
    } while (intento != respuesta);

    printf("********************\n");
    printf("Respuesta: %10d\n", respuesta);
    printf("Intentos: %10d\n", intentos);
    printf("********************\n");
    return 0;
}
