import sys
#print each letter of the alphabet backwards, one on each line

alphabet = 'abcdef...z'
alphabet_reverse = alphabet[::-1]
print(alphabet_reverse)

#random exercise
sys.stdout.write('\033c') # clear screen

sys.stdout.write('\033[5;10H') # set cursor to position x;y 5,10

sys.stdout.write('\x1b[34m') # set terminal color to blue fg (34)

sys.stdout.write('Hello Students!!!\n')

sys.stdout.write('\x1b[0m') # reset terminal to default colors

sys.stdout.write('\x1b[46m\x1b[30m') # set terminal color to Cyan bg (46) black fg (30)

sys.stdout.write('She wore blue velvet...')

sys.stdout.write('\x1b[0m') # reset terminal to default colors

sys.stdout.flush() # useful if you have timers and delays
