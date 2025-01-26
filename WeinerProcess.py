import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

#Set ticker and download data
ticker = 'AAPL'
data = yf.download(ticker,start="2024-01-01", end="2025-01-01")

#Calculate daily log returns
data['Log Returns'] = np.log(data['Close'] / data['Close'].shift(1))

#Estimate mu(drift) and sigma (Volatility)
mu = data['Log Returns'].mean() * 252 # Annualize Mean
sigma = data['Log Returns'].std() * np.sqrt(252) # Annualize Standard deviation

# Parameters for the Simulation
S0 = data['Close'].iloc[-1] #last closing price as starting price
T = 1.0 #time horizon one year
dt = 1/252 #time step
N = int(T / dt) #Total number of time steps
simulations = 10 # number of path to simulate

# Arrays for storing data
time = np.linspace(0, T, N)
W = np.zeros(N)
S = np.zeros(N)
S[0] = S0

for i in range(1,N):
    dW = np.random.normal(0, np.sqrt(dt))
    W[i] = W[i-1] + dW
    S[i] = S[i-1] * (1 + mu * dt + sigma * dW)

# Plotting Results
plt.figure(figsize=(10, 5))
plt.plot(time, S, label = f'Stock Price of {ticker}')
plt.title('Stimulated Stock Price Using Wiener Process')
plt.xlabel('Time (Years)')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.show()