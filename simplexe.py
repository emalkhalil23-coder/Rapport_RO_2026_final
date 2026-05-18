from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

x1 = solver.NumVar(0, solver.infinity(), 'P1')
x2 = solver.NumVar(0, solver.infinity(), 'P2')

c1 = solver.Constraint(-solver.infinity(), 10, 'Machine')
c1.SetCoefficient(x1, 2)
c1.SetCoefficient(x2, 1)

c2 = solver.Constraint(-solver.infinity(), 12, 'MO')
c2.SetCoefficient(x1, 1)
c2.SetCoefficient(x2, 3)

obj = solver.Objective()
obj.SetCoefficient(x1, 5)
obj.SetCoefficient(x2, 8)
obj.SetMaximization()

status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print("===== Solution Optimale =====")
    print(f"P1 = {x1.solution_value():.2f} unites")
    print(f"P2 = {x2.solution_value():.2f} unites")
    print(f"Profit max = {solver.Objective().Value():.2f} MRU")