import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
np.random.seed(0)
num_samples = 50
heights = np.random.uniform(150, 190, num_samples)
weights = 0.6 * heights + 50 + np.random.normal(0, 10, num_samples)

# 定义线性回归模型
class LinearRegression:
    def __init__(self):
        self.weight = np.random.rand()
        self.bias = np.random.rand()
        
    def predict(self, X):
        return self.weight * X + self.bias
    
    def update(self, X, y, learning_rate):
        y_pred = self.predict(X)
        error = y_pred - y
        self.weight -= learning_rate * np.mean(error * X)
        self.bias -= learning_rate * np.mean(error)

# 初始化模型和超参数
lr_model = LinearRegression()
learning_rate = 0.0001
num_epochs = 1000

# 训练模型
for epoch in range(num_epochs):
    lr_model.update(heights, weights, learning_rate)
    if epoch % 100 == 0:
        loss = np.mean((lr_model.predict(heights) - weights) ** 2)
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss:.4f}')

# 可视化结果
plt.scatter(heights, weights, label='Data')
plt.plot(heights, lr_model.predict(heights), color='red', label='Linear Regression')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regression Model')
plt.legend()
plt.show()
