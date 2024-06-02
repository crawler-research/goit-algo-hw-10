from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

model = LpProblem(name="resource-allocation", sense=LpMaximize)

x = LpVariable(name="Lemonade", lowBound=0)
y = LpVariable(name="Fruit_Juice", lowBound=0)

# обмеження
model += (2 * x + y <= 100, "Water")
model += (x <= 50, "Sugar")
model += (x <= 30, "Lemon_Juice")
model += (2 * y <= 40, "Fruit_Puree")

model += lpSum([x, y])

status = model.solve()

print(f"Статус: {LpStatus[status]}")
print(f"Лемонад: {x.varValue}")
print(f"Сік: {y.varValue}")