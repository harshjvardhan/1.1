from qiskit_ibm_runtime import QiskitRuntimeService
 
# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(channel="ibm_quantum", token="dofkgkjbiodfgmmmjbdfgbkdmdmcjsfgoibnahjernvkjfgfgbnoskdnvjfsjikrwtb", set_as_default=True)
 
# Load saved credentials
service = QiskitRuntimeService()

 from qiskit import QuantumCircuit
 from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
 
 # Create empty circuit
 example_circuit = QuantumCircuit(2)
 example_circuit.measure_all()
 
 # You'll need to specify the credentials when initializing QiskitRuntimeService, if they were not previously saved.
 service = QiskitRuntimeService()
 backend = service.backend("ibmq_qasm_simulator")
 job = Sampler(backend).run(example_circuit)
 print(f"job id: {job.job_id()}")
 result = job.result()
 print(result)
