import matplotlib.pyplot as plt

def 状態を可視化する(状態):
    量子ビット数 = int(np.log2(len(状態)))
    
    # 状態ベクトルの要素を取得
    確率振幅 = np.abs(状態)**2
    
    # 棒グラフで確率振幅を描画
    plt.figure(figsize=(8, 6))
    plt.bar(range(2**量子ビット数), 確率振幅)
    plt.xlabel('状態')
    plt.ylabel('確率振幅')
    plt.xticks(range(2**量子ビット数), ['|{:0{}b}>'.format(i, 量子ビット数) for i in range(2**量子ビット数)])
    plt.show()