#!/usr/bin/python3

from random import randint

# the original flag was between 20 and 100 characters long
flag = 'flag{REDACTED}'

NUM_BYTES = 12345
CLOCK = NUM_BYTES // len(flag)

def main():
    with open('maze.bin', 'w') as out:
        j = 0
        for i in range(12345):
            if j >= len(flag):
                break

            if i % CLOCK == 0:
                c = flag[j]
                out.write(flag[j])
                j += 1
            else:
                c = chr(randint(40, 100))
                out.write(c)

if __name__ == '__main__':
    main()
