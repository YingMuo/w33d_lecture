extern printf
extern exit

global main

section .data
  format db "%d", 10, 0
section .text

main:
    mov eax, 100
    push eax
    push  format
    call  printf  ; printf(format, eax)

    push  0
    call exit     ; exit(0)
