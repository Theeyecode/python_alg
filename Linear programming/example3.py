# Import required Libraries
from ortools.init.python import init
from ortools.linear_solver import pywraplp

# Initialize or Declare the solver required
solver_name = 'CLP'
solver = pywraplp.Solver.CreateSolver(solver_name)
if not solver:
    print(f'Could not create solver {solver_name}')

#Create the variables 
x_var = solver.NumVar(0,1,"x")
y_var = solver.NumVar(0,2,"y")
print("Number of variables =", solver.NumVariables())

#Define the constraints  x + y <= 2.
infinity = solver.infinity()
# solver.Add(x_var + y_var <=2)
constraint = solver.Constraint(-infinity, 2, "ct")
constraint.SetCoefficient(x_var, 1)
constraint.SetCoefficient(y_var, 1)
print("Number of constraints =", solver.NumConstraints())


#Define the objective function  3 * x + y.
objective = solver.Objective()
objective.SetCoefficient(x_var,3)
objective.SetCoefficient(y_var,1)
objective.SetMaximization()

#Invoke the solver
print(f"Solving with {solver.SolverVersion()}")
status = solver.Solve()
if status != pywraplp.Solver.OPTIMAL:
    print("The problem does not have an optimal solution.")
    if status == pywraplp.Solver.FEASIBLE:
        print("A potentially suboptimal solution was found.")
    else:    
        print(f"The solver could not solve the problem. Error code: {status}")
print("Solution:")
print(f"Objective value = {objective.Value():0.2f}")
print(f"x = {x_var.solution_value():0.1f}")
print(f"y = {y_var.solution_value():0.1f}")
    
    


