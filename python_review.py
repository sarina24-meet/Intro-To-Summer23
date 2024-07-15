#temperatures = [] 
#days_of_the_week = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#counter = 0 
#for i in range (7): 
#	num = random.randit(26,40)  
#	if num % 2 == 0 : 
#	print (num, "even") 
#	print(days_of_the_week[num], "has an even temperature") 
#	counter = counter + 1  
#	print(days_of_the_week[i]) 





#import random 
#temperatures = []
#good_days_counter=0
#days_of_the_week=["Sunday","Monday", "Tuesday", "Wendseday", "Thursday", "Friday", "Saturday"]
#even_days=[]

#for i in range(7):
#	temperatures.append(random.randint(26,40))
#	if temperatures[i] % 2== 0:
#		good_days_counter=good_days_counter+1
#		even_days.append(days_of_the_week[i])
#
#
#print (even_days)  
#import random
#temp= []
#for i in range(7):
#   temp.append(random.randint(26,41))
    
#print(temp)
#day = ["sun","mon","tues","wedn","thrs","friday","saturday"]
#count = 0

#for i in range (7):
   # if temp[i] % 2 == 0 :
  #    print(day[i])
 #     count+=1 
      
#print(count)      

#highest_temp = 0
#for i in range(7):  
#	if temp[i] > highest_temp:
#		highest_temp = temp[i] 

#print (highest_temp) 

import random

temperature = []

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

even_temperatures = []
odd_temperatures = []

avg_temp = []

for i in range(7):
    temperature.append(random.randint(26,41))
    print(temperature)

good_days_count = 0

for i in range(7):
	if temperature[i] % 2 == 0:
		good_days_count = good_days_count+1

print("the number of good days are: ", good_days_count)


highest_temp = temperature[0]
for i in range(7):
	if highest_temp < temperature[i]: 
		highest_temp = temperature[i]
		highest_day = days_of_the_week[i] 
	else: 
		print(temperature[i]) 

print("The highest temperature of the week is ", highest_temp)
print("The highest temperature of the week was on a ", days_of_the_week[i])

lowest_temp = temperature[0]
for i in range(7):
	if lowest_temp > temperature[i]: 
		lowest_temp = temperature[i]
		lowest_day = days_of_the_week[i]
print("The lowest temperature of the week is ", lowest_temp)
print("The lowest temperature was on a ", lowest_day)

for i in range(7): 
	average_temperature = sum(temperature) / 7

print("The average temperature throughout the week is ", average_temperature) 