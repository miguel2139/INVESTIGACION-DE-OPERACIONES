import pulp

# Define the problem
prob = pulp.LpProblem("Maximizar_Ganancia", pulp.LpMaximize)

# Define the variables
x11 = pulp.LpVariable("x11", lowBound=0, cat="Continuous")
x12 = pulp.LpVariable("x12", lowBound=0, cat="Continuous")
x13 = pulp.LpVariable("x13", lowBound=0, cat="Continuous")
x21 = pulp.LpVariable("x21", lowBound=0, cat="Continuous")
x22 = pulp.LpVariable("x22", lowBound=0, cat="Continuous")
x23 = pulp.LpVariable("x23", lowBound=0, cat="Continuous")
x31 = pulp.LpVariable("x31", lowBound=0, cat="Continuous")
x32 = pulp.LpVariable("x32", lowBound=0, cat="Continuous")
x33 = pulp.LpVariable("x33", lowBound=0, cat="Continuous")
x41 = pulp.LpVariable("x41", lowBound=0, cat="Continuous")
x42 = pulp.LpVariable("x42", lowBound=0, cat="Continuous")
x43 = pulp.LpVariable("x43", lowBound=0, cat="Continuous")

# Objective function
prob += (
    320 * x11 + 320 * x12 + 320 * x13 +
    400 * x21 + 400 * x22 + 400 * x23 +
    360 * x31 + 360 * x32 + 360 * x33 +
    290 * x41 + 290 * x42 + 290 * x43
), "ganancia_total"

# Constraints
prob += x11 + x21 + x31 + x41 <= 12, "peso_Parte_Delantera"
prob += x12 + x22 + x32 + x42 <= 10, "Peso_Central"
prob += x13 + x23 + x33 + x43 <= 10, "Peso_Parte_Posterior"

prob += 500 * x11 + 700 * x21 + 600 * x31 + 400 * x41 <= 7000, "Volumen_Parte_Delantera"
prob += 500 * x12 + 700 * x22 + 600 * x32 + 400 * x42 <= 9000, "Volumen_Parte_Central"
prob += 500 * x13 + 700 * x23 + 600 * x33 + 400 * x43 <= 5000, "Volumen_Parte_Posterior"

prob += x11 + x12 + x13 <= 20, "demanda_pedido_1"
prob += x21 + x22 + x23 <= 16, "demanda_pedido_2"
prob += x31 + x32 + x33 <= 25, "demanda_pedido_3"
prob += x41 + x42 + x43 <= 13, "demanda_pedido_4"

# Solve the problem
prob.solve()

# Print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Ganancia total = {pulp.value(prob.objective)}")
