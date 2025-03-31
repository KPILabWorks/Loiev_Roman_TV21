import pandas as pd
import numpy as np

# Створення випадкового DataFrame з енергоспоживанням
np.random.seed(42)
data = pd.DataFrame({
    'household': np.random.randint(100, 500, 1000),
    'industry': np.random.randint(500, 2000, 1000),
    'commercial': np.random.randint(200, 800, 1000)
})

# Обчислення медіани для кожного стовпця
medians = data.median()

# Фільтрація рядків, де значення більше за медіану
filtered_data = data.query("household > @medians.household & industry > @medians.industry & commercial > @medians.commercial")

# Вивід розміру відфільтрованого DataFrame
print("Кількість відібраних рядків:", len(filtered_data))
