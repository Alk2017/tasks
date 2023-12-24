def run():
	count = int(input())
	ls = []
	for _ in range(count):
		ls.append(input())
	print('Initial array:')
	print(', '.join(ls))
	print('**********')
	for i in range(len(ls[0])):
		print(f'Phase {i+1}')
		for j in range(10):
			bucket = [s for s in ls if s[-1 -i] == f'{j}']
			print(f'Bucket {j}: {"empty" if len(bucket) == 0 else ", ".join(bucket)}')
		ls.sort(key=lambda s: s[-1-i])
		print('**********')
	print('Sorted array:')
	print(', '.join(ls))


if __name__ == '__main__':
	run()