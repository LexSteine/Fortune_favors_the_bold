def TreeOfLife(H, W, N, tree):
    branchAge = initTree(H, W, tree)
    for i in range(N):
        branchAge = branchGrow(branchAge)
        if i % 2 == 0:
            tree, branchAge = branchCreate(H, W, tree, branchAge)
        else:
            tree, branchAge = branchDelete(H, W, tree, branchAge)
    return tree


def initTree(H, W, tree):
    dictOfBranches = {1: []}
    for i in range(H):
        for j in range(W):
            if tree[i][j] == "+":
                dictOfBranches[1].append([i, j])
    return dictOfBranches


def branchCreate(H, W, tree, branchAge):
    NewTree = []
    if 1 not in branchAge.keys():
        branchAge[1] = []
    for i in range(H):
        NewTree.append("")
        for j in range(W):
            NewTree[i] += "+"
            if tree[i][j] == ".":
                branchAge[1].append([i, j])
    return NewTree, branchAge


def branchGrow(branchAge):
    temp = {}
    for i in branchAge:
        temp[i + 1] = branchAge[i]
    return temp


def branchDelete(H, W, tree, branchAge):
    masDel, agesDel, NewTree = [], [], []
    for i in branchAge.keys():
        if i > 2:
            agesDel.append(i)
    for i in agesDel:
        for j in branchAge[i]:
            appendToDelList(j, masDel)
            if 0 < j[0] < H - 1 and 0 < j[1] < W - 1:
                appendToDelList([j[0] - 1, j[1]], masDel)
                appendToDelList([j[0] + 1, j[1]], masDel)
                appendToDelList([j[0], j[1] - 1], masDel)
                appendToDelList([j[0], j[1] + 1], masDel)
            if j[0] == 0 and j[1] == 0:
                appendToDelList([j[0], j[1] + 1], masDel)
                appendToDelList([j[0] + 1, j[1]], masDel)
            if j[0] == H - 1 and j[1] == W - 1:
                appendToDelList([j[0], j[1] - 1], masDel)
                appendToDelList([j[0] - 1, j[1]], masDel)
            if j[0] == 0 and j[1] == W - 1:
                appendToDelList([j[0], j[1] - 1], masDel)
                appendToDelList([j[0] + 1, j[1]], masDel)
            if j[0] == H - 1 and j[1] == 0:
                appendToDelList([j[0], j[1] + 1], masDel)
                appendToDelList([j[0] - 1, j[1]], masDel)
            if j[0] == 0 and 0 < j[1] < W - 1:
                appendToDelList([j[0] + 1, j[1]], masDel)
                appendToDelList([j[0], j[1] - 1], masDel)
                appendToDelList([j[0], j[1] + 1], masDel)
            if j[0] == H - 1 and 0 < j[1] < W - 1:
                appendToDelList([j[0] - 1, j[1]], masDel)
                appendToDelList([j[0], j[1] - 1], masDel)
                appendToDelList([j[0], j[1] + 1], masDel)
            if 0 < j[0] < H - 1 and j[1] == 0:
                appendToDelList([j[0], j[1] + 1], masDel)
                appendToDelList([j[0] - 1, j[1]], masDel)
                appendToDelList([j[0] + 1, j[1]], masDel)
            if 0 < j[0] < H - 1 and j[1] == W - 1:
                appendToDelList([j[0], j[1] - 1], masDel)
                appendToDelList([j[0] - 1, j[1]], masDel)
                appendToDelList([j[0] + 1, j[1]], masDel)
    for i in branchAge:
        for j in masDel:
            if j in branchAge[i]:
                branchAge[i].remove(j)
    for i in range(H):
        NewTree.append("")
        for j in range(W):
            if [i, j] in masDel or tree[i][j] == ".":
                NewTree[i] += "."
            else:
                NewTree[i] += "+"
    return NewTree, branchAge


def appendToDelList(elem, DelList):
    if elem not in DelList:
        DelList.append(elem)
    pass
