'''
Functions take a path to file with data salaries,
and return tuple with total salary and average salaries.
'''

def total_salary(path):
    
    try: # Пробуємо відкрити файл
        with open(path, 'r', encoding='utf-8' ) as file:

            total_salary = 0
            all_salaries = []
            
            while True:

                line = file.readline()
                
                if not line: # Коли рядки закінчаться цикл перестане читати файл
                    break
                
                salary = int(line.split(",")[1]) # Забираємо зарплату та перетворюємо на int
                all_salaries.append(salary)
                total_salary += salary
                average_salary = total_salary / len(all_salaries)
                
    except FileNotFoundError:
        print("File not found!")
        return 0
    
    return [total_salary, average_salary]

total, average = total_salary('dz1.txt')
print(f"total_salary: {total}, average_salary: {average}")

