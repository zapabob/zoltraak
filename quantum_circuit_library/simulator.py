import numpy as np

def シミュレーションする(回路):
    状態 = np.zeros(2**回路.量子ビット数, dtype=complex)
    状態[0] = 1.0
    
    for ゲート, 量子ビット in 回路.ゲート列:
        # ゲートを状態に適用する処理を実装
        pass
    
    return 状態