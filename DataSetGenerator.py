import pandas as pd
import random
import string

# Генерація великих даних
def generate_data(n):
    data = []
    for _ in range(n):
        login = ''.join(random.choices(string.ascii_lowercase, k=10))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        data.append([login, password])
    return data


num_records = 10**6
data = generate_data(num_records)
df = pd.DataFrame(data, columns=["login", "password"])

df.to_csv("large_dataset.csv", index=False)