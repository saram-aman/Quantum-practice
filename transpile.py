from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

backend = service.backend('ibm_nazca')
target = backend.target

# Transpile the circuit
pm = generate_preset_pass_manager(
        target=target, 
        optimization_level=3
     )
t_qc = pm.run(qc)

# Map the observable according to the transpile layout
t_obs = obs.apply_layout(t_qc.layout)