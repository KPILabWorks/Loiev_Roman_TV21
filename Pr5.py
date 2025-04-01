from faker import Faker
import pandas as pd

# Ініціалізація генератора даних
fake = Faker()

# Генерація синтетичних даних
num_records = 1000  # Кількість записів
data = {
    "id": [i for i in range(1, num_records + 1)],
    "name": [fake.name() for _ in range(num_records)],
    "email": [fake.email() for _ in range(num_records)],
    "phone": [fake.phone_number() for _ in range(num_records)],
    "address": [fake.address() for _ in range(num_records)],
    "birthdate": [fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat() for _ in range(num_records)],
    "company": [fake.company() for _ in range(num_records)],
    "salary": [round(fake.random_number(digits=5), 2) for _ in range(num_records)]
}

# Створення датафрейму
synthetic_df = pd.DataFrame(data)

# Запис у файл CSV
synthetic_df.to_csv("people.csv", index=False)

# Виведення перших рядків
print(synthetic_df.head())