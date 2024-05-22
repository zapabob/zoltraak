import numpy as np

class 量子回路:
    def __init__(self, 量子ビット数):
        self.量子ビット数 = 量子ビット数
        self.ゲート列 = []
        self.状態 = np.zeros(2**量子ビット数, dtype=complex)
        self.状態[0] = 1.0
    
    def ゲートを適用する(self, ゲート, 量子ビット):
        self.ゲート列.append((ゲート, 量子ビット))
        # ゲートを状態に適用する処理を実装
    
    def 測定する(self, 量子ビット):
        # 測定の処理を実装
        pass
    
    def シミュレーションする(self):
        # シミュレーションの処理を実装
        pass