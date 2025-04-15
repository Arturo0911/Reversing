#include <unistd.h>

int main(){
	write(1, "Hello, world", 12);
	_exit(0);
}
