# Import required Libraries
from ortools.linear_solver import pywraplp

solver_name = 'CBC'


# Define the Data
# Indices
I = 5  # Number of products (keep as integer)
J = 3  # Number of suppliers
T = 3  # Number of time periods

# Parameters (from tables)
D = [
    #period 1, period 2, period 3
    [57, 72, 92],  # Product 1
    [90, 73, 89],  # Product 2
    [58, 95, 95],  # Product 3
    [92, 97, 53],  # Product 4
    [54, 88, 87]   # Product 5
]

P = [
#unit cost at supplier 1, supplier 2, supplier 3
    [209, 997, 578],  # Product 1
    [719, 362, 133],  # Product 2
    [503, 582, 750],  # Product 3
    [857, 731, 589],  # Product 4
    [530, 930, 467]   # Product 5
]

H = [15.00, 10.00, 15.00, 18.00, 16.00]   #Unit Holding cost per peiod
O = [5795, 1856, 4106]                    #Ordering cost per order
W = [3500, 4200, 6000]                     #Available Storage space per period
S = [10, 15, 20, 25, 30]                   #Unit Storage space per product

# Inititalize Solver
solver = pywraplp.Solver.CreateSolver(solver_name)
if not solver:
    print("Solver not created.")
    exit(1)

# Define Decision Variables
X = {}
for i in range(I):
    for j in range(J):
        for t in range(T):
            X[i, j, t] = solver.NumVar(0, solver.infinity(), f'X_{i}_{j}_{t}')
    
                             
Y = {}
for j in range(J):
    for t in range(T):
        Y[j, t] = solver.BoolVar(f'Y_{j}_{t}')
    print(Y)
    exit

# Use 'Inv' for inventory variables instead of 'I'
Inv = {}
for i in range(I):
    for t in range(T):
        Inv[i, t] = solver.NumVar(0, solver.infinity(), f'I_{i}_{t}')

# Objective Function
ordering_cost = solver.Sum(O[j] * Y[j, t] for j in range(J) for t in range(T))
purchasing_cost = solver.Sum(P[i][j] * X[i, j, t] for i in range(I) for j in range(J) for t in range(T))
holding_cost = solver.Sum(H[i] * Inv[i, t] for i in range(I) for t in range(T))
solver.Minimize(ordering_cost + purchasing_cost + holding_cost)

#  Constraints
# 1. Inventory Balance: Inv_{i,t-1} + ∑ Q_ijt = D_it + Inv_it
for i in range(I):
    for t in range(T):
        if t == 0:
            solver.Add(solver.Sum(X[i, j, t] for j in range(J)) == D[i][t] + Inv[i, t])
        else:
            solver.Add(Inv[i, t-1] + solver.Sum(X[i, j, t] for j in range(J)) == D[i][t] + Inv[i, t])

# 2. Order Trigger
M = sum(sum(D[i]) for i in range(I))  # Big-M
for i in range(I):
    for j in range(J):
        for t in range(T):
            solver.Add(X[i, j, t] <= M * Y[j, t])

# 3. Storage Space
for t in range(T):
    solver.Add(solver.Sum(S[i] * Inv[i, t] for i in range(I)) <= W[t])

# Invoke the solver....Solve the Model
status = solver.Solve()

# Basic Output
if status == pywraplp.Solver.OPTIMAL:
    print(f'Optimal Solution Found! Total Cost = ${solver.Objective().Value():.2f}')
    # print("\nOrdering Quantities (Q_ijt):")
    # for i in range(I):
    #     for j in range(J):
    #         for t in range(T):
    #             if X[i, j, t].solution_value() > 0:
    #                 print(f'Product {i+1}, Supplier {j+1}, Period {t+1}: {X[i, j, t].solution_value():.2f}')
    # print("\nOrder Decisions (X_jt):")
    # for j in range(J):
    #     for t in range(T):
    #         if Y[j, t].solution_value() > 0:
    #             print(f'Supplier {j+1}, Period {t+1}: Order Placed')
    # print("\nInventory Levels (I_it):")
    # for i in range(I):
    #     for t in range(T):
    #         if Inv[i, t].solution_value() > 0:
    #             print(f'Product {i+1}, Period {t+1}: {Inv[i, t].solution_value():.2f}')
else:
    print("No optimal solution found.")



#     Optimal Solution Found! Total Cost = $480343.00

# Ordering Quantities (Q_ijt):
# Product 1, Supplier 1, Period 1: 129.00
# Product 1, Supplier 1, Period 3: 92.00
# Product 2, Supplier 3, Period 1: 90.00
# Product 2, Supplier 3, Period 2: 73.00
# Product 2, Supplier 3, Period 3: 89.00
# Product 3, Supplier 1, Period 1: 153.00
# Product 3, Supplier 1, Period 3: 95.00
# Product 4, Supplier 3, Period 1: 92.00
# Product 4, Supplier 3, Period 2: 97.00
# Product 4, Supplier 3, Period 3: 53.00
# Product 5, Supplier 3, Period 1: 54.00
# Product 5, Supplier 3, Period 2: 88.00
# Product 5, Supplier 3, Period 3: 87.00

# Order Decisions (X_jt):
# Supplier 1, Period 1: Order Placed
# Supplier 1, Period 3: Order Placed
# Supplier 3, Period 1: Order Placed
# Supplier 3, Period 2: Order Placed
# Supplier 3, Period 3: Order Placed

# Inventory Levels (I_it):
# Product 1, Period 1: 72.00
# Product 3, Period 1: 95.00