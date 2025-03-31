import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline
from sklearn.metrics import mean_squared_error

# Створення даних
np.random.seed(0)
time = np.linspace(0, 10, 100)
energy_consumption = np.sin(time) + 0.5 * np.random.normal(size=100)

# Створюємо пропущені значення
mask = np.random.choice([True, False], size=100, p=[0.2, 0.8])
energy_consumption_missing = energy_consumption.copy()
energy_consumption_missing[mask] = np.nan

# Інтерполяція: поліноміальна
poly_interp = interp1d(np.where(~np.isnan(energy_consumption_missing))[0],
                       energy_consumption_missing[~np.isnan(energy_consumption_missing)],
                       kind='cubic', fill_value='extrapolate')
energy_poly_filled = poly_interp(np.arange(len(energy_consumption_missing)))

# Інтерполяція: сплайн
spline_interp = CubicSpline(np.where(~np.isnan(energy_consumption_missing))[0],
                             energy_consumption_missing[~np.isnan(energy_consumption_missing)])
energy_spline_filled = spline_interp(np.arange(len(energy_consumption_missing)))

# Лінійна апроксимація
linear_interp = interp1d(np.where(~np.isnan(energy_consumption_missing))[0],
                         energy_consumption_missing[~np.isnan(energy_consumption_missing)],
                         kind='linear', fill_value='extrapolate')
energy_linear_filled = linear_interp(np.arange(len(energy_consumption_missing)))

# Обчислення похибок
mse_poly = mean_squared_error(energy_consumption[~np.isnan(energy_consumption_missing)], energy_poly_filled[~np.isnan(energy_consumption_missing)])
mse_spline = mean_squared_error(energy_consumption[~np.isnan(energy_consumption_missing)], energy_spline_filled[~np.isnan(energy_consumption_missing)])
mse_linear = mean_squared_error(energy_consumption[~np.isnan(energy_consumption_missing)], energy_linear_filled[~np.isnan(energy_consumption_missing)])

# Візуалізація
plt.figure(figsize=(12, 6))
plt.plot(time, energy_consumption, label='Original Data', color='black')
plt.plot(time, energy_consumption_missing, label='Data with Missing Values', linestyle='dashed', color='gray')
plt.plot(time, energy_poly_filled, label='Polynomial Interpolation', linestyle='--')
plt.plot(time, energy_spline_filled, label='Spline Interpolation', linestyle='-.')
plt.plot(time, energy_linear_filled, label='Linear Interpolation', linestyle=':')

plt.legend()
plt.title('Comparison of Interpolation Methods')
plt.xlabel('Time')
plt.ylabel('Energy Consumption')
plt.grid(True)
plt.show()

# Виведення похибок
print(f'Mean Squared Error (Polynomial): {mse_poly:.4f}')
print(f'Mean Squared Error (Spline): {mse_spline:.4f}')
print(f'Mean Squared Error (Linear): {mse_linear:.4f}')
