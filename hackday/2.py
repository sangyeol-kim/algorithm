class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def unique_path_memo(node, memo):
    if (not node):
        return len(memo)

    if node.data in memo:
        memo[node.data] += 1
    else:
        memo[node.data] = 1

    max_path = max(unique_path_memo(node.left, memo),
                   unique_path_memo(node.right, memo))

    memo[node.data] -= 1

    if (memo[node.data] == 0):
        del memo[node.data]

    return max_path


def unique_path(node):

    if (not node):
        return 0

    # hash that store all node value
    Hash = {}

    # return memoax length unique value path
    return unique_path_memo(node, Hash)


# Driver Code
if __name__ == '__main__':
    root = newNode(4)
    root.left = newNode(5)  # L1
    root.right = newNode(6)  # R1
    root.left.left = newNode(4)  # L2
    root.left.left.left = newNode(5)  # L3
    root.right.left = newNode(1)  # RL2
    root.right.right = newNode(6)  # RR6

print(unique_path(root))

# root: 4 left: 5 left: 4 left: 5 / right: 6 left: 1 right: 6

N은 1~50000
모서리 수는 3500 이하


def solution(T):
    height = search_tree(T, 0)
    return height


def search_tree(node, m):
    if node is None:
        return m - 1
    return max(l_count, r_count)




def getHeight(sub_T):
    if sub_T == None:
        return 0
    return max(getHeight(sub_T.l), getHeight(sub_T.r))+1


def solution(T):
    return max(getHeight(T.l), getHeight(T.r))


if T:
    return max(solution(T.l), solution(T.r)) + 1 
return -1
