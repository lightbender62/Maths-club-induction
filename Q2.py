import numpy as np
import matplotlib.pyplot as plt

money = list(map(int, input().split()))
n=len(money)

#just defining NPV here
def NPV(r , n , money): 
    x = money[0]
    for i in range (1 , n):
        x += money[i]/((1+r)**i)
    
    return x

# never thought i would need binary search here
hi = 100 #took 100 coz i doubt irr would go above 10000%
lo = 0
irr = 0
e = 1e-6

while (hi-lo>e):
    midd = (lo + hi)/2
    if NPV(midd , n , money)>0:
        lo = midd

    else:
        hi = midd
        irr = midd


#printing them in grid fr
print("+---------+----------------+")
print(f"| {'r (%)':^7} | {'NPV(r)':^14} |")
print("+---------+----------------+")

rates = [0.0, 0.05, 0.10, 0.15, 0.20]

for r in rates:
    npv = NPV(r, n ,money)
    print(f"| {r*100:^7.2f} | {npv:^14.2f} |")

print("+---------+----------------+")

print("IRR with some level of precision :" , irr)

rates1 = np.linspace(0.0, 0.5, 200)
npv_val = [NPV(r , n , money) for r in rates1]

#making graph
plt.figure(figsize=(16,8))
plt.plot(rates1*100 , npv_val , label = 'NPV Values' , color = 'red')
plt.axhline(0, color="black", linewidth=1)

#marking irr point now
plt.axvline(irr * 100, color="red", linestyle="--", label=f"IRR = {irr*100:.2f}%")
plt.scatter(irr * 100, 0, color="red")

#labelsss
plt.xlabel("Rate of Interest (%)")
plt.ylabel("NPV (Net Present Value)")
plt.title("NPV graph with marked IRR")

#new syntax
plt.legend()
plt.grid(True)

plt.show()





