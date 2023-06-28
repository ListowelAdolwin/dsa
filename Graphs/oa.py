def search(inn, data,n):
    i = 0
    while i < n :
        if (inn[i] == data):
            return i
        i += 1
    return i

# Fills preorder traversal of tree with given
# inorder and postorder traversals in a stack
def fillPre(inn, post, inStrt, inEnd, n):
    global s, postIndex

    if (inStrt > inEnd):
        return

    # Find index of next item in postorder traversal in
    # inorder.
    val = post[postIndex]
    inIndex = search(inn, val, n)
    postIndex -= 1

    # traverse right tree
    fillPre(inn, post, inIndex + 1, inEnd, n)

    # traverse left tree
    fillPre(inn, post, inStrt, inIndex - 1, n)

    s.append(val)

# This function basically initializes postIndex
# as last element index, then fills stack with
# reverse preorder traversal using printPre
def printPreMain(inn, post, n):
    global s

    lenn = n
    postIndex = lenn - 1

    fillPre(inn, post, 0, lenn - 1, n)

    while ( len(s) > 0):
        print(s[-1], end=" ")
        del s[-1]

# Driver code
if __name__ == '__main__':
    s,postIndex = [], 0

    inn =[4,2,7,5,8,1,3,6]
    post =[4,7,8,5,2,6,3,1]

    n=len(inn)
    printPreMain(inn, post,n)
