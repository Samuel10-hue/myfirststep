def kendall_distance (x , y ) :
 n , pX , pY = len ( x ) , [] , []

    for i in range (0 , n -1) :
       for j in range (i , n ) :
        pX . append (( x [ i ] , x [j ]) )
        pY . append (( y [ i ] , y [j ]) )
    pX . sort ()
    pY . sort ()

    i = j = tau = 0
        while i < len ( pX ) and j < len ( pY ) :
          if pX [ i ] < pY [ j ]: i , tau = i +1 , tau +1
          elif pX [ i ] > pY [j ]: j += 1
            else :
            i , j = i +1 , j +1
    return tau + len ( pX ) - i