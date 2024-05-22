import unittest
from quantum_circuit_library.circuit import 量子回路

class テスト_量子回路(unittest.TestCase):
    def テスト_振幅の合計が1になる(self):
        回路 = 量子回路(2)
        回路.ゲートを適用する(𝐇(), [0])
        状態 = 回路.シミュレーションする()
        self.assertAlmostEqual(np.sum(np.abs(状態)**2), 1.0)
    
    def テスト_ゲートの適用順序が正しい(self):
        回路 = 量子回路(2)
        回路.ゲートを適用する(𝐗(), [0])
        回路.ゲートを適用する(𝐘(), [1])
        状態 = 回路.シミュレーションする()
        self.assertAlmostEqual(状態[3], 1.0)

if __name__ == '__main__':
    unittest.main()