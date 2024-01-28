def total_salary(path):
    
    try: # Пробуємо відкрити файл
        with open(path, 'r') as file:
            
            total_salary = 0
            all_salaries = []
            
            while True:
                
                line = file.readline()
                
                if not line: # Коли рядки закінчаться цикл перестане читати файл
                    break
                
                salary = int(line.split(",")[1]) # Забираємо зарплату та перетворюємо на int
                all_salaries.append(salary)
                total_salary += salary
                
    except FileNotFoundError:
        print("File not found!")
        return 0
    
    return (total_salary, total_salary / len(all_salaries))

salaries_data = total_salary('dz1.txt')

print(type(salaries_data), salaries_data)
