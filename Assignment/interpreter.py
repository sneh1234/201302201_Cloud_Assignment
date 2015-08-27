
import sys
import fileinput
import re

# Replace all the 32-bit register types with 64-bit register types, i.e register of types e[*]x with type r[*]x
for line in fileinput.input('asm32.asm', inplace=1):
    line = re.sub('eax','rax', line.rstrip())
    line = re.sub('ebx','rbx', line.rstrip())
    line = re.sub('ecx','rcx', line.rstrip())
    line = re.sub('edx','rdx', line.rstrip())
    line = re.sub('esi','rsi', line.rstrip())
    line = re.sub('ebp','rbp', line.rstrip())
    line = re.sub('edi','rdi', line.rstrip())
    line = re.sub('esp','rsp', line.rstrip())
    print(line)
