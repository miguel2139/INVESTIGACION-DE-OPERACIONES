import pulp

# Define the problem
prob = pulp.LpProblem("Maximize_Net_Return", pulp.LpMaximize)

# Define variables for hectares planted of each crop in each community
x11 = pulp.LpVariable("Las_Palmitas_Arroz_Secano", lowBound=0, cat="Continuous")
x12 = pulp.LpVariable("Las_Palmitas_Arroz_Forastero", lowBound=0, cat="Continuous")
x13 = pulp.LpVariable("Las_Palmitas_Sandia", lowBound=0, cat="Continuous")

x21 = pulp.LpVariable("Gavalda_Arroz_Secano", lowBound=0, cat="Continuous")
x22 = pulp.LpVariable("Gavalda_Arroz_Forastero", lowBound=0, cat="Continuous")
x23 = pulp.LpVariable("Gavalda_Sandia", lowBound=0, cat="Continuous")

x31 = pulp.LpVariable("El_Naranjo_Arroz_Secano", lowBound=0, cat="Continuous")
x32 = pulp.LpVariable("El_Naranjo_Arroz_Forastero", lowBound=0, cat="Continuous")
x33 = pulp.LpVariable("El_Naranjo_Sandia", lowBound=0, cat="Continuous")

# Objective function: maximize net return
prob += (
    1000 * (x11 + x21 + x31) +  # Net return for Arroz Secano
    750 * (x12 + x22 + x32) +   # Net return for Arroz Forastero
    250 * (x13 + x23 + x33)     # Net return for Sandia
), "Total_Net_Return"

# Constraints for each community's land availability
prob += x11 + x12 + x13 <= 400, "Land_Las_Palmitas"
prob += x21 + x22 + x23 <= 600, "Land_Gavalda"
prob += x31 + x32 + x33 <= 300, "Land_El_Naranjo"

# Constraints for each community's water availability
prob += 3 * x11 + 2 * x12 + 1 * x13 <= 600, "Water_Las_Palmitas"
prob += 3 * x21 + 2 * x22 + 1 * x23 <= 800, "Water_Gavalda"
prob += 3 * x31 + 2 * x32 + 1 * x33 <= 375, "Water_El_Naranjo"

# Crop planting constraints (maximum planting area per crop)
prob += x11 + x21 + x31 <= 600, "Max_Arroz_Secano"
prob += x12 + x22 + x32 <= 500, "Max_Arroz_Forastero"
prob += x13 + x23 + x33 <= 325, "Max_Sandia"

# Proportional planting constraints as per community's available land
# Las Palmitas: Arroz Secano (185), Arroz Forastero (154), Sandia (100)
prob += x11 == (185 / 400) * (x11 + x12 + x13), "Proportion_Las_Palmitas_Arroz_Secano"
prob += x12 == (154 / 400) * (x11 + x12 + x13), "Proportion_Las_Palmitas_Arroz_Forastero"
prob += x13 == (100 / 400) * (x11 + x12 + x13), "Proportion_Las_Palmitas_Sandia"

# Gavalda: Arroz Secano (277), Arroz Forastero (231), Sandia (150)
prob += x21 == (277 / 600) * (x21 + x22 + x23), "Proportion_Gavalda_Arroz_Secano"
prob += x22 == (231 / 600) * (x21 + x22 + x23), "Proportion_Gavalda_Arroz_Forastero"
prob += x23 == (150 / 600) * (x21 + x22 + x23), "Proportion_Gavalda_Sandia"

# El Naranjo: Arroz Secano (138), Arroz Forastero (115), Sandia (75)
prob += x31 == (138 / 300) * (x31 + x32 + x33), "Proportion_El_Naranjo_Arroz_Secano"
prob += x32 == (115 / 300) * (x31 + x32 + x33), "Proportion_El_Naranjo_Arroz_Forastero"
prob += x33 == (75 / 300) * (x31 + x32 + x33), "Proportion_El_Naranjo_Sandia"

# Solve the problem
prob.solve()

# Print the results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue} hectares")

print(f"Total Net Return = ${pulp.value(prob.objective)}")

