alpha = {
	'A':	'.-',
	'B':	'-...',
	'C':	'-.-.',
	'D':	'-..',
	'E':	'.',
	'F':	'..-.',
	'G':	'--.',
	'H':	'....',
	'I':	'..',
	'J':	'.---',
	'K':	'-.-',
	'L':	'.-..',
	'M':	'--',
	'N':	'-.',
	'O':	'---',
	'P':	'.--.',
	'Q':	'--.-',
	'R':	'.-.',
	'S':	'...',
	'T':	'-',
	'U':	'..-',
	'V':	'...-',
	'W':	'.--',
	'X':	'-..-',
	'Y':	'-.--',
	'Z':	'--..',
	'0':	'-----',
	'1':	'.----',
	'2':	'..---',
	'3':	'...--',
	'4':	'....-',
	'5':	'.....',
	'6':	'-....',
	'7':	'--...',
	'8':	'---..',
	'9':	'----.',
	' ':	' / ',
}

import sys

def trans_morse(msg):
	morse = ''
	for b in msg:
		b = b.upper()
		for a in b:
			morse += alpha[a]
			morse += ' '
	morse[:-1]
	print(morse)

msg = list()
msg = sys.argv
msg.pop(0)
ok = True
for a in msg:
	for b in a:
		if b.isalnum() is False and b.isspace() is False:
			ok = False
res = ' '.join(str(a) for a in msg)
if ok is False:
	print("ERROR")
else:
	trans_morse(res)
