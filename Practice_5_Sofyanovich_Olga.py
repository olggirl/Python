# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:49:11 2022

@author: sofya
"""

#1
add_file = open('#1.txt', 'w')
line = input("Insert line: ")
while line:
    add_file.writelines(line)
    line = input('Insert line: ')
    if not line:
        break

#2
new_file = open('new_data.txt', 'r')
new_content = new_file.readlines()
print(f'Lines in file - {len(new_content)}')
new_file = open("new_data.txt", 'r')
content = new_file.read()
content = content.split()
print(f'Total words - {len(content)}')
new_file.close()
        
#3
with open('#3.txt', 'r') as just_file:
    sal = []
    small_sal = []
    just_list = just_file.read().split('\n')
    for i in just_list:
        i = i.split()
        if int(i[1]) < 20000:
           small_sal.append(i[0])
        sal.append(i[1])
print(f'Salary less than 20.000 {small_sal}, avarage salary {sum(map(int, sal)) / len(sal)}')

#4
with open('#4.txt', 'r') as file_subject:
    for i in file_subject:
        new_file.append(new_list[i[0]] + '  ' + i[1])
new_list = [{'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}]
print(new_list)
   
#5
my_file = open("BabyFile.txt", "w")
newo_file = my_file.write("3\n, 5\n")
print(newo_file)
my_file.write("Привет, файл!")
my_file.close()

with open('#5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

#6
with open('#6.txt', 'r') as init_f:
        content = new_file.read()
        content = content.split()
        total = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {total}')