print("birthday problem solver")

days:int = 365
people:int = 23
running_sum:float = 1

for i in range(days,days-people,-1):
	running_sum = running_sum * (i/days)

pa = 1 - running_sum
print(str(float(f'{pa*100:.2f}')) + "%")