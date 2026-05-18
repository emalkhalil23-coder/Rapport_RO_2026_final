from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

NOMS = ['Depot','Arafat','Sebkha','Dar Naim','Teyarett','Toujounine']
dist = [
    [ 0,  5,  8, 12,  7, 15],
    [ 5,  0,  6, 10,  9, 13],
    [ 8,  6,  0,  4,  7, 11],
    [12, 10,  4,  0,  5,  8],
    [ 7,  9,  7,  5,  0,  6],
    [15, 13, 11,  8,  6,  0],
]

manager = pywrapcp.RoutingIndexManager(6, 1, 0)
routing = pywrapcp.RoutingModel(manager)

def dist_cb(fi, ti):
    return dist[manager.IndexToNode(fi)][manager.IndexToNode(ti)]

cb = routing.RegisterTransitCallback(dist_cb)
routing.SetArcCostEvaluatorOfAllVehicles(cb)

params = pywrapcp.DefaultRoutingSearchParameters()
params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

sol = routing.SolveWithParameters(params)
if sol:
    idx, tournee = routing.Start(0), []
    while not routing.IsEnd(idx):
        tournee.append(NOMS[manager.IndexToNode(idx)])
        idx = sol.Value(routing.NextVar(idx))
    tournee.append(NOMS[0])
    print(" -> ".join(tournee))