from pwn import *

#p = process( './test' )
p = remote( 'hackyour.pw', 5568 )

#print( p.recvuntil( ': ' ) )

#p.sendline( p64( 123 ) )

p.interactive()
