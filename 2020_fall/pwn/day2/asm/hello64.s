extern printf
extern exit
global main

section .data ; data
	format db '%s', 0x3
	msg db 'hello world', 0xa

section .text ; code
main:
	mov rdi, format
	mov rsi, msg
	call printf

	mov rdi, 0
	call exit
