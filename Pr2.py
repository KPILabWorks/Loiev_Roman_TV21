import pandas as pd
from functools import lru_cache

# Завантаження даних з CSV файлу
df = pd.read_csv("large_dataset.csv")

# Приклад функції для обробки тексту з кешуванням
@lru_cache(maxsize=128)  # Кешування результатів
def process_text(text):
    # Складна операція над текстом
    return text.upper()  # Наприклад, конвертуємо в верхній регістр

# Використовуємо .apply() для трансформації колонки 'login' з кешуванням
df['processed_login'] = df['login'].apply(process_text)

# Перевірка результату
print(df.head())  # Виводимо перші кілька записів
