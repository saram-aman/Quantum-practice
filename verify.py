from qiskit_aer.primitives import Estimator

# To get a sense of good and bad, simulate the circuit to get the ideal, noiseless result

estimator = Estimator(skip_transpilation=True)

sim_job = estimator.run(
              t_qc, 
              t_obs,
              parameter_values,
              shots=10000
          )

sim_result = sim_job.result()