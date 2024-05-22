from qiskit import IBMQ, transpile
from quantum_circuit_library.circuit import 量子回路

def IBMQデバイスで実行する(回路, バックエンド名):
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    backend = provider.get_backend(バックエンド名)
    
    # 量子回路をQiskit形式に変換
    qiskit_circuit = transpile(回路.to_qiskit(), backend)
    
    # デバイスでの実行
    job = backend.run(qiskit_circuit)
    result = job.result()
    counts = result.get_counts(qiskit_circuit)
    
    return counts