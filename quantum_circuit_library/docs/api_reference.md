量子回路クラス
__init__(self, 量子ビット数)
量子回路を初期化します。

引数:

量子ビット数 (int): 量子ビットの数



𝐇(self, ターゲット)
アダマールゲート(𝐇)を適用します。

引数:

ターゲット (int): ターゲットの量子ビットのインデックス



𝐗(self, ターゲット)
パウリXゲート(𝐗)を適用します。

引数:

ターゲット (int): ターゲットの量子ビットのインデックス



𝐘(self, ターゲット)
パウリYゲート(𝐘)を適用します。

引数:

ターゲット (int): ターゲットの量子ビットのインデックス



𝐙(self, ターゲット)
パウリZゲート(𝐙)を適用します。

引数:

ターゲット (int): ターゲットの量子ビットのインデックス



𝐂𝐍𝐎𝐓(self, 制御, ターゲット)
CNOTゲート(𝐂𝐍𝐎𝐓)を適用します。

引数:

制御 (int): 制御量子ビットのインデックス
ターゲット (int): ターゲット量子ビットのインデックス



測定(self)
量子回路の測定を行います。

戻り値:

結果 (list): 測定結果のビット列



シミュレータークラス
実行(self, 回路)
量子回路をシミュレートします。

引数:

回路 (量子回路): シミュレートする量子回路


戻り値:

結果 (list): シミュレーション結果のビット列