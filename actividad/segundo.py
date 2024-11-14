import pulp

# Define the problem
prob = pulp.LpProblem("Maximize_Rice_Production", pulp.LpMaximize)

# Define variables for the area to be planted in each community (in hectares)
x1 = pulp.LpVariable("Las_Palmitas", lowBound=0, cat="Continuous")
x2 = pulp.LpVariable("Gavalda", lowBound=0, cat="Continuous")
x3 = pulp.LpVariable("El_Naranjo", lowBound=0, cat="Continuous")

# Objective function: maximize the planted area
prob += x1 + x2 + x3, "Total_Planted_Area"

# Constraints for land availability (in hectares)
prob += x1 <= 400, "Land_Las_Palmitas"
prob += x2 <= 600, "Land_Gavalda"
prob += x3 <= 300, "Land_El_Naranjo"

# Constraints for water availability (in hectare-feet)
prob += x1 * 1 <= 600, "Water_Las_Palmitas"
prob += x2 * 1 <= 800, "Water_Gavalda"
prob += x3 * 1 <= 375, "Water_El_Naranjo"

# Solve the problem
prob.solve()

# Print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue} hectares")

print(f"Total planted area = {pulp.value(prob.objective)} hectares")
