import numpy as np
import matplotlib.pyplot as plt

# ダミーデータ
x = np.random.randn(100)
y = np.random.randn(100)

# 描画
plt.figure(figsize=(6, 4))
plt.scatter(x, y, alpha=0.7)

plt.title("Dummy Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()