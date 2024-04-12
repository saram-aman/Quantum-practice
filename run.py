from qiskit_ibm_runtime import Options

options = Options()

# For comparison, we first run circuit with non-optimized parameters
options.transpilation.skip_transpilation = True
options.resilience_level = 0
options.execution.shots = 10000

estimator = Estimator(backend='ibm_nazca', options=options)
unoptimized_job = estimator.run(t_qc, t_obs, parameter_values)

# Get unoptimized result and plot 
unoptimized_result = unoptimized_job.result()
unoptimized_result.values

# Next we redefine Runtime options with optimized parameters for transpilation and error mitigation
options = Options()

options.transpilation.skip_transpilation = True
options.resilience_level = 2
options.execution.shots = 10000

estimator = Estimator(backend='ibm_nazca', options=options)
optimized_job = estimator.run(t_qc, t_obs, parameter_values)

# Get optimized result and plot 
optimized_result = optimized_job.result()
optimized_result.values