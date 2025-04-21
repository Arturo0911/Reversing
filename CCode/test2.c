#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	
    int firstN = atoi(argv[1]);
    int secondN = atoi(argv[2]);
    float sum;
    float rest;
    sum = firstN + secondN;
    rest = firstN - secondN;
    printf("%.1f\n", sum);
    return 0;
}
