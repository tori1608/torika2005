# Программа для проверки и исправления пробелов после знаков препинания

print("=== Анализатор и корректор цитат ===")
print("Проверка пробелов после знаков препинания")

# Получаем цитату от пользователя
quote = input("Введите цитату: ")
print(f"\nИсходная цитата: \"{quote}\"")

# Функция для проверки и исправления цитаты
def check_and_fix_punctuation(text):
    punctuation_marks = ['.', ',', '!', '?']
    needs_fixing = False
    fixed_text = ""
    
    # Анализируем текст посимвольно
    for i in range(len(text)):
        current_char = text[i]
        fixed_text += current_char
        
        # Проверяем, является ли текущий символ знаком препинания
        if current_char in punctuation_marks:
            # Проверяем, есть ли следующий символ и не является ли он пробелом
            if i + 1 < len(text) and text[i + 1] != ' ' and text[i + 1] not in punctuation_marks:
                # Добавляем пробел после знака препинания
                fixed_text += ' '
                needs_fixing = True
    
    return fixed_text, needs_fixing

# Проверяем и исправляем цитату
corrected_quote, has_errors = check_and_fix_punctuation(quote)

# Выводим результаты проверки
print("\n" + "="*50)
print("РЕЗУЛЬТАТЫ ПРОВЕРКИ:")
print("="*50)

if has_errors:
    print(f"Исправленная цитата: \"{corrected_quote}\"")
    print("\n⚠️  ВНИМАНИЕ: Обнаружены пропущенные пробелы после знаков препинания и исправлены.")
else:
    print(f"Цитата: \"{corrected_quote}\"")
    print("\n✅ Отлично! Пробелы после знаков препинания расставлены правильно.")

# Дополнительная информация
print("\n" + "="*50)
print("СПРАВКА:")
print("="*50)
print("Программа проверяет знаки препинания: . , ! ?")
print("Правило: после этих знаков должен стоять пробел.")

