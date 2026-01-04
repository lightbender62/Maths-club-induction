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
#anyways defining the way to find IRR
def find(lo , hi , money , e=1e-6):
    while (hi-lo>e):
        midd = (lo + hi)/2
        if(NPV(lo ,n ,money)*NPV(midd , n , money)>0):
            lo = midd
        else:
            hi = midd
    
    return (hi+lo)/2


r_min = 0
r_max = 5 #def not going above 500%
rates = np.linspace(r_min , r_max , 20000) #dividing them in small intervals
npv_val = [NPV(r, n , money) for r in rates]

#Finding intervals where sign changes
intervals = []
for i in range(len(rates)-1):
    if npv_val[i] * npv_val[i+1] < 0:
        intervals.append((rates[i], rates[i+1]))

#Filling irr list now
irr = []
if len(intervals)==0:
    print("No IRRs Exists")

else:
    for lo, hi in intervals:
        irrx=find(lo , hi , money)
        irr.append(irrx)

for i, irrx in enumerate(irr, 1):
    print(f"  IRR {i}: {irrx * 100:.4f}%")


#printing the grid part now
print("+---------+----------------+")
print(f"| {'r (%)':^7} | {'NPV(r)':^14} |")
print("+---------+----------------+")

rates123 = [0.0, 0.05, 0.10, 0.15, 0.20]

for r in rates123:
    npv = NPV(r, n ,money)
    print(f"| {r*100:^7.2f} | {npv:^14.2f} |")

print("+---------+----------------+")

#making graph
plt.figure(figsize=(16,8))
plt.plot(rates*100 , npv_val , label = 'NPV Values' , color = 'red')
plt.axhline(0, color="black", linewidth=1)

#marking irr points now
for idx, irrx in enumerate(irr):
    label = f"IRR {idx+1} = {irrx*100:.2f}%"
    plt.axvline(irrx * 100, color="blue", linestyle="--", label=label)
    plt.scatter(irrx * 100, 0, color="blue")

#labelsss
plt.xlabel("Rate of Interest (%)")
plt.ylabel("NPV (Net Present Value)")
plt.title("NPV graph with marked IRR(s)")

#new syntax
plt.legend()
plt.grid(True)

plt.show()





