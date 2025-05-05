#include <unistd.h>

int main(){

  write(1, "Hello World!", 12);
  _exit(0);
}
