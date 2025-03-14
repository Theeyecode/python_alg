from ortools.linear_solver import pywraplp

# Define data
num_routes = 2
num_shifts = 2
bus_type_I_capacity = 60
bus_type_II_capacity = 90
num_type_I_buses = 10
num_type_II_buses = 5
trip_factor = 4
shifts = [1, 2]
routes = [1, 2]

# Demand D[i][j]
D = {
    (1,1): 500,
    (1,2): 300,
    (2,1): 400,
    (2,2): 200
}

# Calculate P_i
total_demand_route_1 = 800
total_demand_route_2 = 600
total_demand = 1400
P = {
    1: total_demand_route_1 / total_demand,
    2: total_demand_route_2 / total_demand
}

# Minimum trips m_j
m = {
    1: 10,
    2: 8
}

# Create the solver
solver = pywraplp.Solver('bus_scheduling', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# Create variables
x = {}
y = {}
for i in routes:
    for j in shifts:
        x[i,j] = solver.IntVar(0, solver.infinity(), f'x_{i}_{j}')
        y[i,j] = solver.IntVar(0, solver.infinity(), f'y_{i}_{j}')  

# Objective
objective = solver.Minimize(solver.Sum(x[i,j] + y[i,j] for i in routes for j in shifts))

# Constraints
# Demand satisfaction
for i in routes:
    for j in shifts:
        solver.Add(bus_type_I_capacity * x[i,j] + bus_type_II_capacity * y[i,j] >= D[i,j])

# Fleet size constraints
total_trips_type_I = solver.Sum(x[i,j] for i in routes for j in shifts)
total_trips_type_II = solver.Sum(y[i,j] for i in routes for j in shifts)
solver.Add(total_trips_type_I <= num_type_I_buses * (trip_factor * num_shifts))
solver.Add(total_trips_type_II <= num_type_II_buses * (trip_factor * num_shifts))

# Minimum trips constraints
for j in shifts:
    total_trips_shift_j = solver.Sum(x[i,j] + y[i,j] for i in routes)
    solver.Add(total_trips_shift_j >= m[j])

# Trip limit constraints
for i in routes:
    for j in shifts:
        solver.Add(x[i,j] <= num_type_I_buses * P[i] * trip_factor)
        solver.Add(y[i,j] <= num_type_II_buses * P[i] * trip_factor)

# Solve
status = solver.Solve()

# Print solution
if status == pywraplp.Solver.OPTIMAL:
    print('Optimal solution found')
    for i in routes:
        for j in shifts:
            print(f'x[{i},{j}] = {x[i,j].solution_value()}')
            print(f'y[{i},{j}] = {y[i,j].solution_value()}')
else:
    print('No optimal solution found')