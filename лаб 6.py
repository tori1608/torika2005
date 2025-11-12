# -*- coding: utf-8 -*-
"""
Анализ эмоциональной окраски постов в соцсетях
Программа находит слова, написанные полностью заглавными буквами,
и подсчитывает их частоту встречаемости.
"""

# Исходный текст поста
text = """СРОЧНО! Это ВАЖНО! Все должны это видеть (а тем кто НЕ видел, СРОЧНО расскажите!!!111). НЕ
игнорируйте — это РЕАЛЬНО спасёт жизни!
~СМС пришло в 3 часа. => Я был в ШОКЕ. ПОЖАЛУЙСТА, $$поделитесь$$! #ВАЖНО #СПАСИТЕ
P.S. Я не шучу. ПОВТОРЯЮ: ЭТО ВАЖНО!"""

print("ИСХОДНЫЙ ТЕКСТ:")
print("=" * 50)
print(text)
print("=" * 50)
print()

# Анализ текста
import re
from collections import Counter

def analyze_emotional_words(text):
    """
    Находит слова, написанные полностью заглавными буквами.
    Исключает однобуквенные слова и слова с цифрами.
    """
    # Разбиваем текст на слова
    words = re.findall(r'\b\w+\b', text)
    
    emotional_words = []
    
    for word in words:
        # Проверяем условия:
        # - длина > 1 символа
        # - все буквы заглавные
        # - только буквы (без цифр и других символов)
        if (len(word) > 1 and 
            word.isupper() and 
            word.isalpha()):
            emotional_words.append(word)
    
    # Подсчитываем частоту встречаемости
    word_counts = Counter(emotional_words)
    
    return emotional_words, word_counts

# Выполняем анализ
emotional_words, word_counts = analyze_emotional_words(text)

print("РЕЗУЛЬТАТЫ АНАЛИЗА:")
print("=" * 50)

print("\nНайденные эмоциональные слова (заглавными буквами):")
print(f"Всего найдено: {len(emotional_words)} слов")
print(emotional_words)

print("\nСТАТИСТИКА ПО СЛОВАМ:")
print("-" * 30)
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"'{word}': {count} раз(а)")

print("\nОБЩАЯ СТАТИСТИКА:")
print("-" * 30)
print(f"Всего уникальных эмоциональных слов: {len(word_counts)}")
print(f"Общее количество эмоциональных слов: {len(emotional_words)}")
print(f"Самое частое слово: '{max(word_counts, key=word_counts.get)}'")

# Дополнительный анализ
print("\nДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ:")
print("-" * 30)

# Слова, которые были исключены из анализа
all_upper_words = re.findall(r'\b[A-ZА-Я]+\b', text)
excluded_words = [word for word in all_upper_words 
                 if len(word) == 1 or not word.isalpha()]

print(f"Исключенные из анализа слова: {excluded_words}")
print("Причины исключения:")
for word in excluded_words:
    if len(word) == 1:
        print(f"  '{word}' - однобуквенное слово")
    elif not word.isalpha():
        print(f"  '{word}' - содержит не-буквенные символы")

print("\nВЫВОД:")
print("=" * 50)
print("Анализ показывает высокую эмоциональную окраску текста.")
print("Частые использования заглавных слов указывают на:")
print("- Срочность и важность ('СРОЧНО', 'ВАЖНО')")
print("- Эмоциональный призыв ('НЕ', 'ПОЖАЛУЙСТА')")
print("- Сильные эмоции ('ШОКЕ', 'РЕАЛЬНО')")

