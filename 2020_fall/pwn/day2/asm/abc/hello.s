global _start ; entry point

section .data ; string data
    msg db 'hello world', 0xa

section .text ; code

_start:
    mov rsi, msg
    mov rdi, 1
    mov rdx, 12
    mov eax, 1
    syscall
    
    mov eax, 60
    syscall
