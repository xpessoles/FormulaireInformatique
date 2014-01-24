#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <string.h>
void main()
{
   //printf("Bonjour \n");
   float a;
   // Cacul de puissance
   a=pow(2,2);
   // Modulo
   int b;
   b = 4 % 2;
   // Boucle while
   int compteur = 0;
   while (compteur <1)
     {
        printf("%d\n",compteur);
	compteur++;
     }
   // arctan 2
   //printf("%f",atan2(4.,3.));
   
   // Chaine de caracteres
   char phrase[15] = "phrase toctoc";
   int cpt;
   cpt = strlen(phrase);
   printf("%d",cpt);
   for (cpt = 0; cpt<10;cpt++)
     {
	//printf("%c \n",phrase[cpt]);
	printf("%d \t",cpt);
     }
   
}
