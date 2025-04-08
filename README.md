# Reversing

## Terminologies

- rbp => base pointer
- rsp => stack pointer
- rax => acumulador
- rdx => para almacenar la data
- rcx => contador (usado en loops)
- rsi => segunda variable
- rdi => primera variable
- eax => variable global usada en CPU architectures
- rbx => base
- rip => instruction pointer



## Reversing samples

```gcc
int f(){
  return 5;
}

void hackthur(){
  printf("hello I'm Hackthur\n");
}

int main(){
  f();
  hackthur();
}
```


After the file creation, we need to check in gdb, what's going on in the binary in the execution


