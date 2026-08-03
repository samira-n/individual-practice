import datetime

DAYS_RU = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье'
}

def get_day_of_week(day, month, year):
    try:
        date = datetime.date(year, month, day)
        # weekday() возвращает 0-6 (понедельник-воскресенье)
        return DAYS_RU[date.weekday()]
    except ValueError:
        return "Ошибка: Неверная дата"

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def print_number_styled(num):
    patterns = {
        '0': ["***", "* *", "* *", "* *", "***"],
        '1': ["  *", "  *", "  *", "  *", "  *"],
        '2': ["***", "  *", "***", "*  ", "***"],
        '3': ["***", "  *", "***", "  *", "***"],
        '4': ["* *", "* *", "***", "  *", "  *"],
        '5': ["***", "*  ", "***", "  *", "***"],
        '6': ["***", "*  ", "***", "* *", "***"],
        '7': ["***", "  *", "  *", "  *", "  *"],
        '8': ["***", "* *", "***", "* *", "***"],
        '9': ["***", "* *", "***", "  *", "***"]
    }

    num_str = str(num)
    lines = ["" for _ in range(5)]
    
    for digit_char in num_str:
        for i in range(5):
            if digit_char in patterns:
                lines[i] += patterns[digit_char][i] + "  "
            else:
                lines[i] += "     "
                
    print("\nДата рождения в стиле электронного табло:")
    for line in lines:
        print(line)

def main():
    print("=== Программа стилистического преобразования даты рождения ===")
    
    while True:
        try:
            day = int(input("Введите день рождения (1-31): "))
            month = int(input("Введите месяц рождения (1-12): "))
            year = int(input("Введите год рождения (например, 1990): "))
            
            datetime.date(year, month, day)
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректные числовые значения.")
        except:
            print("Ошибка: Введена некорректная дата. Попробуйте снова.")
    
    day_of_week = get_day_of_week(day, month, year)
    print(f"\n1. День недели: {day_of_week}")
    
    if is_leap_year(year):
        print("2. Год был високосным.")
    else:
        print("2. Год не был високосным.")
    
    age = calculate_age(day, month, year)
    print(f"3. Ваш возраст: {age} лет")
    
    formatted_date = f"{day:02d}{month:02d}{year}"
    print_number_styled(formatted_date)

if __name__ == "__main__":
    main()