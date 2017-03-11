'''
Write a python program to print out the console the integer numbers from 30 to 300 , but if that number that is multiples of 7 then print out 'abc', if that number is multiples of 13 then print out 'xyz'. For those numbers those are multiple of both 7 and 13 then print out 'a-z' . 
'''
import string
alpha = string.ascii_lowercase

def multiples_of_7(num):
	if num%7 == 0:
		return True
	return False

def multiples_of_13(num):
	if num%13 == 0:
		return True
	return False


if __name__ == "__main__":
	# in so tu 30 den 300
	for i in range(30, 301):
		if multiples_of_13(i) and multiples_of_7(i):
			print(alpha)
		elif multiples_of_7(i):
			print('abc')
		elif multiples_of_13(i):
			print('xyz')
		else:
			print(i)
