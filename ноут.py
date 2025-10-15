# Ввод данных пользователем
user_name = input("Введите ваше имя: ")
user_message = input("Опишите ваше состояние: ")
anxiety_score = int(input("Введите балл по шкале тревоги от 20 до 80: "))

# Форматирование вывода
print("\n" + "="*50)
print("РЕЗУЛЬТАТ АНАЛИЗА УРОВНЯ СТРЕССА")
print("="*50)
print(f"Имя: {user_name}")
print(f"Сообщение: {user_message}")
print()

# Анализ текстовых маркеров
print("АНАЛИЗ МАРКЕРОВ СТРЕССА")

# Списки ключевых слов для анализа
anxiety_keywords = ["тревог", "страх", "боюсь", "паник"]
positive_keywords = ["надежд", "спокойств", "радост"]

# Проверка наличия ключевых слов в сообщении
found_anxiety = any(keyword in user_message for keyword in anxiety_keywords)
found_positive = any(keyword in user_message for keyword in positive_keywords)

# Определение эмоциональной окраски
if found_anxiety and found_positive:
    emotional_tone = "Смешанные или нейтральные эмоции"
elif found_anxiety:
    emotional_tone = "Обнаружены признаки тревоги"
elif found_positive:
    emotional_tone = "Текст имеет позитивную окраску"
else:
    emotional_tone = "Эмоциональная окраска не определена"

print(emotional_tone)
print()

# Анализ числовой оценки
print("АНАЛИЗ ЧИСЛОВОЙ ОЦЕНКИ СТРЕССА")

# Определение уровня стресса
if anxiety_score <= 30:
    stress_category = "низкий"
elif 31 <= anxiety_score <= 44:
    stress_category = "умеренный"
else:
    stress_category = "высокий"

print(f"Оценка стресса: {anxiety_score} → {stress_category}")

# Итоговая рекомендация
print("Итог")
if found_anxiety and anxiety_score >= 45:
    print("Рекомендуется срочная психологическая поддержка")
else:
    print("Состояние в пределах ожидаемого. Продолжайте наблюдение")


