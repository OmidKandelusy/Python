import matplotlib.pyplot as plt
import numpy as np

# ---------- Sample data ----------
x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [23, 17, 35, 29]

# ---------- 1. Line plot ----------
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='--', linewidth=2)
plt.title("Line Plot Example")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid(True)
plt.show()

# ---------- 2. Scatter plot ----------
plt.figure(figsize=(6, 4))
plt.scatter(x, y, c=y, cmap='viridis', s=50, alpha=0.7)
plt.title("Scatter Plot Example")
plt.colorbar(label='Value')
plt.show()

# ---------- 3. Bar chart ----------
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='skyblue')
plt.title("Bar Chart Example")
plt.ylabel("Values")
plt.show()

# ---------- 4. Histogram ----------
data = np.random.normal(loc=0, scale=1, size=1000)
plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='salmon', edgecolor='black')
plt.title("Histogram Example")
plt.show()

# ---------- 5. Pie chart ----------
plt.figure(figsize=(6, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['red', 'green', 'blue', 'orange'])
plt.title("Pie Chart Example")
plt.show()

# ---------- 6. Subplots ----------
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y, 'r-')
axs[0, 0].set_title('Line Plot')

axs[0, 1].scatter(x, y, c=y, cmap='plasma')
axs[0, 1].set_title('Scatter Plot')

axs[1, 0].bar(categories, values, color='green')
axs[1, 0].set_title('Bar Chart')

axs[1, 1].hist(data, bins=20, color='purple')
axs[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()

# ---------- 7. Saving a figure ----------
plt.figure()
plt.plot(x, y)
plt.title("Saved Figure Example")
# plt.savefig("saved_figure.png")  # Saves to the current directory
plt.close()