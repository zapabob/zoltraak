import cirq
from quantum_circuit_library.circuit import 量子回路

def Cirqデバイスで実行する(回路, デバイス名):
    # Cirqデバイスを取得
    デバイス = cirq.get_device(デバイス名)
    
    # 量子回路をCirq形式に変換
    cirq_circuit = 回路.to_cirq()
    
    # デバイスでの実行
    result = cirq.run(cirq_circuit, デバイス)
    counts = result.histogram(key='result')
    
    return counts