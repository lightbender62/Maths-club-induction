import numpy as np
import matplotlib.pyplot as plt

#you guys said comments, so expect a lot of comments now

#assigning all values rn 
S = 100
u = 0.08
v = 0.20
T=1 
Steps = 252
N = 1000

dt = T/Steps

#creating graph here
price = np.zeros((N , Steps+1))
price[:,0] = S


#whatever formula was given, i am just typing it here

for i in range(N):
   for t in range(1, Steps+1):
       #random shock here
       z=np.random.normal()
       price[i , t] = price [i , t-1] * np.exp((u-0.5*v**2)*dt + v*np.sqrt(dt)*z)

#Gonna show the graph now
plt.figure(figsize=(16 , 8))
for i in range(N):
    plt.plot(price[i] , color = 'green' , alpha=0.05)
plt.title("Simulated Stock Paths")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.show()

#A friend said that we gotta show a good graph too show adding this
plt.figure(figsize=(16,8))
for i in range(25):
    plt.plot(price[i] , color = 'red' , alpha = 0.5)
plt.title("First 25 Simulated Stock Paths")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.show()

#Now comes the histogram of final prices
final = price[:, -1]

plt.figure(figsize=(12,6))
plt.hist(final , bins=50 , color = 'skyblue' , edgecolor = 'black')
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# European Call Option Payoff (Strike = 105)
K = 105

# payoff for each path at maturity
payoff = np.maximum(final - K, 0)

#expected payoff
call_price_simulated = np.mean(payoff)

#simulated mean and std
sim_mean = np.mean(final)
sim_std = np.std(final)


#gonna print them in grid now
#also not making variables coz lazy

print("\n" + "-" * 60)
print("{:<25} | {:<15} | {:<15}".format("Metric", "Theoretical", "Simulated"))
print("-" * 60)

print("{:<25} | {:<15.4f} | {:<15.4f}".format(
    "Mean final price", S*np.exp(u*T) , sim_mean))

print("{:<25} | {:<15.4f} | {:<15.4f}".format(
    "Std final price", S * np.exp(u*T) * np.sqrt(np.exp(v**2 * T) - 1), sim_std))

print("{:<25} | {:<15} | {:<15.4f}".format(
    "Call option payoff", "-", call_price_simulated))

print("-" * 60)



