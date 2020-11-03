import matplotlib.pyplot as plt
from function import RandomWalk

# x_values = [1, 2, 3, 4, 5] 
# y_values = [1, 4, 9, 16, 25]

fig = plt.figure()
ax = fig.gca(projection='3d')

random_walk = RandomWalk()
random_walk.fill_walk()
# print(random_walk.x_values)

point_numbers = list(range(random_walk.num_points))

surf = ax.scatter(random_walk.x_values, random_walk.y_values, random_walk.z_values, c=random_walk.x_values, cmap=plt.cm.Blues, edgecolors=None)
# plt.scatter(random_walk.x_values, random_walk.y_values, random_walk.z_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors=None)

plt.title("Geolab scatter", fontsize=20)

plt.xlabel("X label")
plt.ylabel("Y label")

plt.show()
# plt.savefig('fig.png', bbox_inches='tight')