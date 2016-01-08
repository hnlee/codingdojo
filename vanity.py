import sys


DIALPAD = dict([(x, 2) for x in 'abc'] +
	       [(x, 3) for x in 'def'] +
               [(x, 4) for x in 'ghi'] +
               [(x, 5) for x in 'jkl'] +
               [(x, 6) for x in 'mno'] +
               [(x, 7) for x in 'pqrs'] +
               [(x, 8) for x in 'tuv'] +
	       [(x, 9) for x in 'wxyz'])

def phone_number(name):
	if not hasattr(name, "lower"):
		return '7' * 7

	name = name.lower()

	if len(name) > 7:
		overhang = len(name) - 7
		truncated_name = []
		for n in name[-2:0:-1]:
			if n not in 'aeiou' or overhang == 0:
				truncated_name.append(n)
			else:
				overhang -= 1
		truncated_name.reverse()
		truncated_name = name[0] + ''.join(truncated_name) + name[-1]
		if len(truncated_name) > 7:
			truncated_name = name[:3] + name[-4:]
	else:
		truncated_name = name
	
	number = ''.join(str(DIALPAD[x]) if x in DIALPAD else str(x) for x in truncated_name)
	if len(number) < 7:
			number = '7' * (7 - len(number)) + number

	return '1-617-%s-%s' % (number[:3], number[-4:])

def main():
	print(phone_number(sys.argv[1]))

if __name__ == "__main__":
	main()


