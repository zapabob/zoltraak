from quantum_circuit_library.circuit import 量子回路

def ショアのアルゴリズム(N):
    量子ビット数 = len(bin(N)) - 2
    回路 = 量子回路(3 * 量子ビット数)
    
    # 量子フーリエ変換
    for i in range(量子ビット数):
        回路.ゲートを適用する(𝐇(), [i])
        for j in range(i):
            回路.ゲートを適用する(𝐂𝐑𝐤(π / 2**(i - j)), [j, i])
    
    # 変調加算
    for i in range(量子ビット数):
        回路.ゲートを適用する(𝐂𝐌𝐀𝐃𝐃(a**i % N), [i, 量子ビット数, 2 * 量子ビット数])
    
    # 逆量子フーリエ変換
    for i in range(量子ビット数 - 1, -1, -1):
        for j in range(i):
            回路.ゲートを適用する(𝐂𝐑𝐤(-π / 2**(i - j)), [j, i])
        回路.ゲートを適用する(𝐇(), [i])
    
    # 測定
    結果 = 回路.測定する(range(量子ビット数))
    
    # 連続分数展開
    r = 0
    for i in range(量子ビット数):
        r += 結果[i] * 2**i
    分母 = 2**量子ビット数
    k = 連続分数展開(r / 分母)
    
    # 最大公約数を計算
    p = math.gcd(a**k - 1, N)
    q = N // p
    
    return p, q