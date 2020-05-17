#include <stdio.h>
#include <string.h>

void main(int argc, char * argv[]){
   if(argc > 2){
      if(strcmp(argv[1], "--to") == 0){
         for(int i=0; argv[2][i]; i++){
            switch(argv[2][i]){
               case 'a': printf("alpha ");
                 break;
               case 'b': printf("bravo ");
                 break;
               case 'c': printf("charlie ");
                 break;
               case 'd': printf("delta ");
                 break;
               case 'e': printf("echo ");
                 break;
               case 'f': printf("foxtrot ");
                 break;
               case 'g': printf("golf ");
                 break;
               case 'h': printf("hotel ");
                 break;
               case 'i': printf("india ");
                 break;
               case 'j': printf("juliet ");
                 break;
               case 'k': printf("kilo ");
                 break;
               case 'l': printf("lima ");
                 break;
               case 'm': printf("mike ");
                 break;
               case 'n': printf("november ");
                 break;
               case 'o': printf("oscar ");
                 break;
               case 'p': printf("papa ");
                 break;
               case 'q': printf("quebec ");
                 break;
               case 'r': printf("romeo ");
                 break;
               case 's': printf("sierra ");
                 break;
               case 't': printf("tango ");
                 break;
               case 'u': printf("uniform ");
                 break;
               case 'v': printf("victor ");
                 break;
               case 'w': printf("whiskey ");
                 break;
               case 'x': printf("x-ray ");
                 break;
               case 'y': printf("yankee ");
                 break;
               case 'z': printf("zulu ");
            }
         }
            printf("\n");
      } else {
          for(int i=2; i<argc; i++){
            printf("%c",argv[i][0]);
          }
          printf("\n");
      }
   } else {
      printf("Accepts one of two options: --to or --from.\n");
      printf("If --to, will translate to the Military Alphabet and print it to the console.\n");
      printf("If --from, will print the first character of each of the following words to the console.\n");
   }
}
