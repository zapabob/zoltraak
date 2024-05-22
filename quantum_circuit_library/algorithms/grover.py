
from quantum_circuit_library.circuit import 量子回路

def グローバー検索(オラクル, 量子ビット数):
    回路 = 量子回路(量子ビット数)
    
    # 初期状態の準備
    for i in range(量子ビット数):
        回路.ゲートを適用する(𝐇(), [i])
    
    # グローバーのイテレーション
    for _ in range(int(np.pi * np.sqrt(2**量子ビット数) / 4)):
        オラクル(回路)
        回路.ゲートを適用する(𝐇(), range(量子ビット数))
        回路.ゲートを適用する(𝐙(), range(量子ビット数))
        回路.ゲートを適用する(𝐇(), range(量子ビット数))
    
    # 測定
    結果 = 回路.測定する(range(量子ビット数))
    return 結果