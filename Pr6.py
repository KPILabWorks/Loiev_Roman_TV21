import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлу
data = pd.read_csv('lighting_data.csv')

# Порівняння середнього рівня освітленості для природного та штучного освітлення
mean_natural = data['Природне освітлення (лк)'].mean()
mean_artificial = data['Штучне освітлення (лк)'].mean()

# Порівняння стандартного відхилення для природного та штучного освітлення
std_natural = data['Природне освітлення (лк)'].std()
std_artificial = data['Штучне освітлення (лк)'].std()

# Виведення результатів
print(f"Середнє значення природного освітлення: {mean_natural:.2f} лк")
print(f"Середнє значення штучного освітлення: {mean_artificial:.2f} лк")
print(f"Стандартне відхилення природного освітлення: {std_natural:.2f}")
print(f"Стандартне відхилення штучного освітлення: {std_artificial:.2f}")

# Побудова гістограм для візуалізації розподілу рівнів освітленості
plt.figure(figsize=(10, 6))
plt.hist(data['Природне освітлення (лк)'], bins=10, alpha=0.5, label='Природне освітлення')
plt.hist(data['Штучне освітлення (лк)'], bins=10, alpha=0.5, label='Штучне освітлення')
plt.xlabel('Рівень освітленості (лк)')
plt.ylabel('Частота')
plt.title('Порівняння рівня освітленості')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# Побудова графіку порівняння середніх значень
plt.figure(figsize=(8, 5))
labels = ['Природне освітлення', 'Штучне освітлення']
means = [mean_natural, mean_artificial]
stds = [std_natural, std_artificial]

plt.bar(labels, means, yerr=stds, capsize=5, color=['skyblue', 'lightgreen'])
plt.ylabel('Рівень освітленості (лк)')
plt.title('Порівняння середніх рівнів освітленості')
plt.grid(True)
plt.show()
