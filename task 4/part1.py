num_list=[]
num = int(input("Введите значения:"))
while num !=0:
   num_list.append(num)
   num = int(input("Введите значения:"))
for i in range(0, len(num_list)):
   for j in range(0, len(num_list)-1):
      if num_list [j]>num_list[j+1]:
         num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
min = num_list[0]
max = num_list[0]
l = 0
for value in num_list:
   if value < min:
      min = value
   if value > max:
      max = value
   l += 1
for k in range(0, len(num_list)):
   if k % 2 == 0:
      num_list.pop(k)
print(num_list)