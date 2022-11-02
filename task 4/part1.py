num_list = []
num = int(input())
while num !=0:
   num_list.append(num)
   num = int(input())
for i in range (0,len(num_list)):
   for j in range(0,len(num_list)-1):
      if num_list [j]>num_list[j+1]:
         num_list [j], num_list[j+1]= num_list[j+1], num_list[j+1]
num_list.sort()
min = num_list [0]
i = 0
for value in num_list:
   if value<min:
      min=value
max = num_list [0]
for value in num_list:
   if value>max:
      max=value
      i+=1
      num_list.pop(j)
print(num_list)