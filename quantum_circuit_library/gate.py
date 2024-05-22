import numpy as np

class ゲート:
    def __init__(self, 行列):
        self.行列 = 行列
    
    def 適用する(self, 状態, 量子ビット):
        # 状態にゲートを適用する処理を実装
        pass

def 𝐗():
    return ゲート(np.array([[0, 1], [1, 0]]))

def 𝐘():
    return ゲート(np.array([[0, -1j], [1j, 0]]))

def 𝐙():
    return ゲート(np.array([[1, 0], [0, -1]]))

def 𝐇():
    return ゲート(np.array([[1, 1], [1, -1]]) / np.sqrt(2))

def 𝐂𝐍𝐎𝐓():
    return ゲート(np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]))