# -*- coding: utf-8 -*-
"""Анализ диалогов в художественном тексте"""

# 1. Создаем список реплик
replicas = [
    "Я не понимаю, что происходит",
    "Это очень странная ситуация", 
    "Я думаю, нам нужно поговорить",
    "Он сказал, что вернется завтра",
    "А я не верю его словам",
    "Почему ты так сказал?",
    "Я просто выражаю свое мнение",
    "Она сказала мне всю правду",
    "Я не знаю, что делать дальше"
]

print("=== 1. ИСХОДНЫЙ СПИСОК РЕПЛИК ===")
for i, replica in enumerate(replicas, 1):
    print(f"{i}. {replica}")

print("\n" + "="*50)

# 2. Добавляем новую реплику
new_replica = "Я совершенно с этим согласен"
replicas.append(new_replica)

print("=== 2. ПОСЛЕ ДОБАВЛЕНИЯ НОВОЙ РЕПЛИКИ ===")
print(f"Добавлена реплика: '{new_replica}'")
print(f"Теперь всего реплик: {len(replicas)}")

print("\n" + "="*50)

# 3. Выводим каждую вторую реплику
print("=== 3. КАЖДАЯ ВТОРАЯ РЕПЛИКА ===")
for i in range(1, len(replicas), 2):
    print(f"{i+1}. {replicas[i]}")

print("\n" + "="*50)

# 4. Находим самую короткую реплику
shortest_replica = min(replicas, key=len)
shortest_length = len(shortest_replica)

print("=== 4. САМАЯ КОРОТКАЯ РЕПЛИКА ===")
print(f"Реплика: '{shortest_replica}'")
print(f"Длина: {shortest_length} символов")

print("\n" + "="*50)

# 5. Считаем реплики, начинающиеся с "Я"
replicas_start_with_ya = [r for r in replicas if r.startswith('Я')]
count_ya = len(replicas_start_with_ya)

print("=== 5. РЕПЛИКИ, НАЧИНАЮЩИЕСЯ С 'Я' ===")
print(f"Количество: {count_ya}")
print("Список:")
for i, replica in enumerate(replicas_start_with_ya, 1):
    print(f"  {i}. {replica}")

print("\n" + "="*50)

# 6. Реплики со словом "сказал"
replicas_with_skazal = [r for r in replicas if 'сказал' in r.lower()]

print("=== 6. РЕПЛИКИ СО СЛОВОМ 'СКАЗАЛ' ===")
print(f"Количество: {len(replicas_with_skazal)}")
if replicas_with_skazal:
    for i, replica in enumerate(replicas_with_skazal, 1):
        print(f"  {i}. {replica}")
else:
    print("  Не найдено")

print("\n" + "="*50)

# ИТОГОВАЯ СТАТИСТИКА
print("=== ИТОГОВАЯ СТАТИСТИКА ===")
print(f"Общее количество реплик: {len(replicas)}")
print(f"Самая короткая реплика: '{shortest_replica}' ({shortest_length} симв.)")
print(f"Реплик на 'Я': {count_ya}")
print(f"Реплик со словом 'сказал': {len(replicas_with_skazal)}")

# Дополнительная статистика
avg_length = sum(len(r) for r in replicas) / len(replicas)
longest_replica = max(replicas, key=len)
print(f"Средняя длина реплики: {avg_length:.1f} символов")
print(f"Самая длинная реплика: '{longest_replica}' ({len(longest_replica)} симв.)")
