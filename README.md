# Reversing

## Terminologies

- rbp => base pointer
- rsp => stack pointer
- rax => acumulador
- rdx => General register or to pass arguments.
- rcx => contador (used in loops).
- rsi => second variable
- rdi => first variable
- eip => next instruction to be executed
- eax => variable global usada en CPU architectures
- rbx => base
- rip => instruction pointer (actual instruction that is executing)
- lea => Load Effective address

## Keywords.

  - Breakpoint:

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


