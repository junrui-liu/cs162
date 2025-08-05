type LinkedList = +{
    'empty: (),
    'node: (Nat, LinkedList)
}


def Len: LinkedList -> Nat =  \l.
    match l {
        'empty (): 0,
        'node (_, b): Len b + 1
    }


type BinaryTree = +{
    'empty: (),
    'node: (Nat, BinaryTree, BinaryTree)
}

def Flip: BinaryTree -> BinaryTree = \t.
    match t {
        'empty (): 'empty (),
        'node (a, l, r): 'node (a, Flip r, Flip l)
    }


main : Nat = 0