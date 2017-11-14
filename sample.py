# -*- coding:utf-8 -*-

# サンプル（１回目の課題）

from matrix import Matrix
from vector import Vector

# 行列とベクトルをキーボードから入力
mat = Matrix.input()
vec = Vector.input()

# 次数を確認
if len(mat) == len(mat[0]) == len(vec):
    N = len(mat)
else:
    print u'次数が異なります'
    quit()


# かけ算を実行
ans = []
for i in range(0, N):
    tmp = 0.0
    for j in range(0, N):
        tmp += mat[i][j] * vec[j]
    ans.append(tmp)

# 答え出力
print '======結果======'
Vector.printVector(ans)
