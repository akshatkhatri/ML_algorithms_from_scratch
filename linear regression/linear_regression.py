import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

def loss_function_MSE(m,b,dataset):
    total_error = 0
    
    for i in range(len(dataset)):
        x = dataset.iloc[i].f1
        y = dataset.iloc[i].f2
        
        total_error += (y - (m * x + b)) ** 2
        
    total_error = total_error / float(len(dataset))
    return total_error
    
def gradient_descent(m_curr, b_curr, dataset, L): 
    m_gradient = 0
    b_gradient = 0
    for i in range(len(dataset)):
        x = dataset.iloc[i].f1
        y = dataset.iloc[i].f2
        
        m_gradient += -(2/(len(dataset))) * (y - (m_curr * x + b_curr)) * x
        b_gradient += -(2/(len(dataset))) * (y - (m_curr * x + b_curr))
    
    m_new = m_curr - (L * m_gradient)
    b_new = b_curr - (L * b_gradient)
    
    return (m_new,b_new)

m = 0
b = 0
L = 0.0001

epochs = 1000

for i in range(epochs):
    if i % 50 == 0:
        current_loss = loss_function_MSE(m, b, data)
        print(f"epoch : {i}, MSE: {current_loss}")
           
    m,b = gradient_descent(m,b,data,L)

print(m , b)

plt.scatter(data.f1,data.f2,color = "black")
plt.plot(list(range(0,35)),[m * x + b for x in range(0,35)] , color = "red")
plt.show()
