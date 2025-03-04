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

# X_ijt
X = {}
for i in range(I):
    for j in range(J):
        for t in range(T):
            X[i, j, t] = solver.NumVar(0, solver.infinity(), f'X_{i}_{j}_{t}')
    
# Y_jt                           
Y = {}
for j in range(J):
    for t in range(T):
        Y[j, t] = solver.BoolVar(f'Y_{j}_{t}')


# 'Inv'  inventory variables instead I_it
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
    print(f'Optimal Solution Found! Total Cost = ${solver.Objective().Value():.2f}\n')

    # Loop through each period
    for t in range(T):
        print(f"Period {t+1}:")

        # Ordering Cost for this period
        period_ordering_cost = sum(O[j] * Y[j, t].solution_value() for j in range(J))
        print(f"  Ordering Cost: ${period_ordering_cost:.2f}")

        # Purchasing Cost for this period
        period_purchasing_cost = sum(P[i][j] * X[i, j, t].solution_value() 
                                     for i in range(I) for j in range(J))
        print(f"  Purchasing Cost: ${period_purchasing_cost:.2f}")

        # Holding Cost for this period
        period_holding_cost = sum(H[i] * Inv[i, t].solution_value() for i in range(I))
        print(f"  Holding Cost: ${period_holding_cost:.2f}")

        # Additional Information
        print("  Ordering Quantities (X_ijt):")
        for i in range(I):
            for j in range(J):
                if X[i, j, t].solution_value() > 0:
                    print(f"    Product {i+1}, Supplier {j+1}: {X[i, j, t].solution_value():.2f}")

        print("  Order Decisions (Y_jt):")
        for j in range(J):
            if Y[j, t].solution_value() > 0:
                print(f"    Supplier {j+1}: Order Placed")

        print("  Inventory Levels (I_it):")
        for i in range(I):
            if Inv[i, t].solution_value() > 0:
                print(f"    Product {i+1}: {Inv[i, t].solution_value():.2f}")
        print()  # Blank line for readability

    # Total Costs for Verification
    total_ordering = sum(O[j] * Y[j, t].solution_value() for j in range(J) for t in range(T))
    total_purchasing = sum(P[i][j] * X[i, j, t].solution_value() for i in range(I) for j in range(J) for t in range(T))
    total_holding = sum(H[i] * Inv[i, t].solution_value() for i in range(I) for t in range(T))
    print(f"Total Ordering Cost: ${total_ordering:.2f}")
    print(f"Total Purchasing Cost: ${total_purchasing:.2f}")
    print(f"Total Holding Cost: ${total_holding:.2f}")

else:
    print("No optimal solution found.")