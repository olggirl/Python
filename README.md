# Python
# Практическое задание к уроку №1.
#1
numbers = 3 * 5, 5 + 25, 35/7, 36//7
words = 'hot', 'nod', 'dog'
total = numbers + strand
print(numbers)
print(words)
print(total)

#2_1
import time
n = 4600
time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print("Time in preferred format: ", time_format)
#2_2
def convert_to_preferred_format(sec):
    time_s = 4600
    hour = time_s // 3600 
    minutes = (time_s - 3600) // 60
    sec = time_s % 60 
    return "%02d:%02d:%02d" % (hour, minutes, sec) 
print("Time in preferred format: ", convert_to_preferred_format(sec))

#3
n = 5
nn = 55
nnn = 555
print(n + nn + nnn)

#4 
a = 695 
a = [6, 9, 5]
max_number = find_max[a]

#5
profit = 345
cost = 150
if profit > cost:
    print("We have earned")
else:
    print("Everything is lost")
#6
conversion = cost / profit * 100
print(conversion)
numbers_empl = 58
salary = numbers_empl / conversion
print(salary)

#7

distance = 2
max_dist = 3
while True:
    distance += 0.2
    if distance <= max_dist:
        print(distance)
