def TOH(n, A, B, C):
    if n == 1:
        print("Move 1 from ", A, " to ", C)
    else:
        TOH(n-1, A, C, B)
        print("Move ", n, " from ", A, " to ", C)
        TOH(n-1, B, A, C)

TOH(3 , 'A', 'B', 'C')