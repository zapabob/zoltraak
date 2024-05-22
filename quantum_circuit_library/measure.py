
import numpy as np

def 測定する(状態, 量子ビット):
    prob_0 = np.sum(np.abs(状態[::2])**2)
    prob_1 = np.sum(np.abs(状態[1::2])**2)
    
    if np.random.rand() < prob_0:
        状態[1::2] = 0
        状態 /= np.sqrt(prob_0)
        return 0
    else:
        状態[::2] = 0
        状態 /= np.sqrt(prob_1)
        return 1