from ortools.linear_solver import pywraplp

# Data from the problem statement
I = 5  # Number of products
J = 3  # Number of suppliers
T = 3  # Number of time periods

# Demand for products over time
demand = [
    [57, 90, 58, 92, 54],  # Period 1
    [72, 73, 95, 97, 88],  # Period 2
    [92, 89, 95, 53, 87],  # Period 3
]

# Unit purchasing costs from suppliers
purchase_price = [
    [209, 719, 503, 857, 530],  # Supplier 1
    [997, 362, 582, 731, 930],  # Supplier 2
    [578, 133, 750, 589, 467],  # Supplier 3
]

# Holding costs per product
holding_cost = [15, 10, 15, 18, 16]  # for each product

# Storage space per product
storage_space = [10, 15, 20, 25, 30]  # sq ft per product

# Available storage space per period
available_storage = [3500, 4200, 6000]  # sq ft per period

# Ordering costs per supplier
ordering_cost = [5795, 1856, 4106]  # for each supplier

# Maximum possible inventory (big M value for constraints)
big_M = 1000

# Create the solver
solver = pywraplp.Solver.CreateSolver('SCIP')
if not solver:
    print("Solver not created.")
    exit(1)

# Decision Variables
X = {}
Y = {}
inventory_vars = {}

# Define X_ijt: Ordering quantity from supplier j for product i at time t
for i in range(I):
    for j in range(J):
        for t in range(T):
            X[i, j, t] = solver.IntVar(0.0, solver.infinity(), f'X_{i}_{j}_{t}')

# Define Y_jt: Binary decision whether to place an order from supplier j at time t
for j in range(J):
    for t in range(T):
        Y[j, t] = solver.IntVar(0.0, 1.0, f'Y_{j}_{t}')

# Define inventory_vars: Inventory level for product i at time t
for i in range(I):
    for t in range(T):
        inventory_vars[i, t] = solver.IntVar(0.0, solver.infinity(), f'I_{i}_{t}')

# Objective function: Minimize total cost
objective = solver.Objective()

# Ordering cost
for j in range(J):
    for t in range(T):
        objective.SetCoefficient(Y[j, t], ordering_cost[j])

# Purchasing cost
for i in range(I):
    for j in range(J):
        for t in range(T):
            objective.SetCoefficient(X[i, j, t], purchase_price[j][i])

# Holding cost
for i in range(I):
    for t in range(T):
        objective.SetCoefficient(inventory_vars[i, t], holding_cost[i])

# Set the objective to minimize
objective.SetMinimization()

# Inventory balance: I_it = I_(i,t-1) + X_ijt - D_it
for i in range(I):
    for t in range(T):
        constraint = solver.Constraint(demand[t][i], solver.infinity())  # lower bound = demand
        for j in range(J):
            constraint.SetCoefficient(X[i, j, t], 1)
        if t > 0:  # for all periods except the first one
            constraint.SetCoefficient(inventory_vars[i, t-1], -1)

# Total storage space constraint
for t in range(T):
    constraint = solver.Constraint(0, available_storage[t])
    for i in range(I):
        constraint.SetCoefficient(inventory_vars[i, t], storage_space[i])

# X_ijt is positive only if an order is placed (Y_ijt = 1)
for i in range(I):
    for j in range(J):
        for t in range(T):
            constraint = solver.Constraint(0, big_M)
            constraint.SetCoefficient(X[i, j, t], 1)
            constraint.SetCoefficient(Y[j, t], -big_M)

# Solve the problem
solver.Solve()

# Print the results
if solver.Solve() == pywraplp.Solver.OPTIMAL:
    print(f'Objective value = {objective.Value()}')
    for i in range(I):
        for j in range(J):
            for t in range(T):
                print(f'X_{i}_{j}_{t}: {X[i, j, t].solution_value()}')
    for j in range(J):
        for t in range(T):
            print(f'Y_{j}_{t}: {Y[j, t].solution_value()}')
else:
    print("No optimal solution found.")
