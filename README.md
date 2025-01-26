
This Python script is a practical implementation of a Monte Carlo simulation to model the future stock price of Apple Inc. (AAPL) using the Weiner Process, an essential stochastic process used in financial modeling for price prediction. The project leverages the yfinance library to fetch historical stock data from Yahoo Finance, focusing on the last year's data from the start of 2024 to the beginning of 2025.

The program begins by downloading the closing prices for AAPL and computing the daily logarithmic returns, which helps in stabilizing the variance and normalizing the returns. From these log returns, it calculates the mean (mu) and standard deviation (sigma) of the returns, which are then annualized to represent a typical year’s expected return and volatility (risk).

The simulation uses the last observed closing price as the starting point (S0) and assumes the future stock price evolves over a one-year period (T=1) divided into 252 trading days (dt=1/252). It simulates ten different potential paths for the stock price based on random daily changes influenced by the calculated drift (mu) and volatility (sigma), following the equation:

<img width="320" alt="image" src="https://github.com/user-attachments/assets/c2ee7b39-da14-4a3e-8dff-d3f04492df7f" />

dW represents the increment of a Weiner process, modeled as a normal distribution scaled by the square root of the time step.

The result is a plot that displays these simulated paths, providing a visual representation of where the stock price could go in the next year under the modeled assumptions. This type of simulation is crucial for risk management, financial planning, and investment strategy development, as it helps in understanding the range of potential outcomes and the inherent uncertainties in stock price movements.
