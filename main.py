# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 定义人群的数量
N = 20000000

# 定义病毒的传播速度
beta = 0.5

# 定义人群的免疫水平
gamma = 0.1

# 定义传染病传播动力学模型
def model(y, t):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - gamma * E
    dIdt = gamma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

# 定义模型的参数
params = (beta, gamma)

# 定义模型的初始值
inffected0 = 4000000;
y0 = (N-inffected0, 0, inffected0, 0)

# 定义模型求解的时间范围
t = np.linspace(0, 100, 100)

# 使用 odeint 函数求解模型
result = odeint(model, y0, t)

# 将求解结果拆分为不同的量
S, E, I, R = result.T

# 使用 matplotlib 库绘制传播情况的折线图
plt.plot(t, S, label='Susceptible')
plt.plot(t, E, label=u'Exposed')
plt.plot(t, I, label=u'Inffected')
plt.plot(t, R, label=u'Recovered')
plt.xlabel('Time (days)')
plt.ylabel('Number of people')
plt.title('Spread of disease')
plt.legend()
plt.show()

