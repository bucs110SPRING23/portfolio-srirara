import random
#Part A
print("Part A:")
weeks = 16
print("Weeks: ", weeks, type(weeks))
classes = 5
print("Number of classes: ", classes, type(classes))
tuition = 6000
print("Tuition cost: ", tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))
classes_per_week = 3
print("Classes per week: ", classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class, type(cost_per_class))

#Part B
print("\n")
print("Part B:")
data_list = [3, "3", 3.0, "three", 3.01]
choice = random.choice(data_list)
print("The system chose", choice)