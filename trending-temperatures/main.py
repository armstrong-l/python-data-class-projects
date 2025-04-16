import matplotlib.pyplot as plt

month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
temp = [28,32,31,40,45,55,60,65,54,43,34,30]

plt.plot(month, temp, color="#03fc45")

plt.xlabel("Months of Year", fontsize=16)
plt.ylabel("Temperature in Degrees Celcius", fontsize=16)

plt.title("Average Monthly Temperatures in North Pole, Alaska")

plt.savefig("alaska_temps.png")