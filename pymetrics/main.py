
from benchmark import BenchmarkRunner
import python_solver
import numba_solver
import cython_solver
import julia_solver


if __name__ == '__main__':
    runner = BenchmarkRunner(solvers=[
        python_solver.PythonSolver(),
        numba_solver.NumbaSolver(),
        cython_solver.CythonSolver(),
        julia_solver.JuliaSolver()

    ])
    runner.time_it()
    runner.verify_results()

    results = {b: {s: None for s in runner.solver_names} for b in runner.benchmarks}
    for r in runner.results:
        results[r.benchmark][r.solver] = r.time

    for mark in runner.benchmarks:
        print(mark)
        for s in runner.solver_names:
            print(f"\t{round(results[mark][s]*1000)}ms - {s}")
