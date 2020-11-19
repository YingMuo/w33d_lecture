global _start
section .text
_start:
	push rax
	mov rbx, 0x68732f2f6e69622f
	push rbx
	push rsp
	pop rdi
	mov rax, 0x3b
	xor rsi, rsi
	xor rdx, rdx
	syscall
