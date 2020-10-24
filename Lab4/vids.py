import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1,2,3,4],[1,4,2,3])
plt.ylabel('y values')
plt.xlabel('x values')
fig.show()
plt.show()
names = ['Nametso', 'Lerato', 'Kenneth', 'Phatsimo']
scores =[60,40,20,89]
plt.figure(figsize=(6,3))
plt.subplot(131)
plt.bar(names, scores)
plt.subplot(132)
plt.scatter(names, scores)
plt.subplot(133)
plt.plot(names, scores)
plt.suptitle("Students Marks")
plt.show