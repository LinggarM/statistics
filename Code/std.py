import math

data = 51,71,76,81,67,98,58,69,87,74,79,81
mean = sum(data)/len(data)

summed = 0
for i in data:
	result_now = (i-mean) * (i-mean)
	summed += result_now
	print(result_now)

print("\n")

print(summed)

print(summed/len(data))

std = math.sqrt(summed/len(data)-1)
print(std)