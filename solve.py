print("birthday problem solver")

days:int = 65536
people:int = 1341
running_sum:float = 1

for i in range(days,days-people,-1):
	running_sum = running_sum * (i/days)

pa = 1 - running_sum
print(str(float(f'{pa*100:.2f}')) + "%")