def FibHelper: (Nat, Nat) -> Nat -> Nat = \p. \n.
    let (x, y) = p in
    if n == 0 then x
    else FibHelper (y, x+y) (n-1)

def Fib: Nat -> Nat = FibHelper (0, 1)

type MyBool = +{
    'true: (),
    'false: ()
}

def Negate: MyBool -> MyBool = \{
    'true: 'false,
    'false: 'true
}

main: Nat = Fib 10