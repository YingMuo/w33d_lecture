from pwn import *

p = process( './guess' )

p.recvuntil( '> ' )
p.sendline( '123' )
data = p.recvline()
b'smaill!!\n'
print( data )

p.interactive()
