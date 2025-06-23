import numpy as np

len_all = 332
index_pairs = {
    1: [np.arange(24, 31), np.arange(81, 88)],
    2: [np.arange(37, 40), np.arange(68, 71)],
    3: [np.arange(42, 46), np.arange(64, 68)],
    4: [np.arange(46, 49), np.arange(60, 63)],
}
index_unpaired = {
    1: np.arange(34, 38),
    2: np.arange(40, 42),
    3: np.arange(49, 60),
    4: np.arange(63, 64),
    5: np.arange(71, 78),
}
# 收集所有已用到的索引
pairs_front = set()
pairs_back = set()
unpaired = set()
for v in index_pairs.values():
    pairs_front.update(v[0])
    pairs_back.update(v[1])
for arr in index_unpaired.values():
    unpaired.update(arr.tolist())

for i in range(1, len_all + 1):
    if i in pairs_front:
        print("(", end="")
    elif i in pairs_back:
        print(")", end="")
    elif i in unpaired:
        print("x", end="")
    else:
        print(".", end="")
