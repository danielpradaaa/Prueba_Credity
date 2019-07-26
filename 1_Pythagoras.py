# Function for found product of a*b*c
def FoundProduct (sum):
	for a in range (0, sum + 1):
		for b in range (0, sum + 1):
			for c in range (0, sum + 1):
				if a < b and b < c and (a + b + c == sum) and (c * c == a * a + b * b):
					print(a * b * c)
					print(a)
					print(b)
					print(c)

#Calling the function
FoundProduct (1000)					