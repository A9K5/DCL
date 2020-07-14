"""
build_tree(int si , int ss ,i nt se)
- si : index of the final array .
- ss : starting index of the array .
- se : ending index of the array .
"""
def build_tree(si,ss,se):
    # print("si,ss,se",si,ss,se)
    if ss==se:
        st[si] = A[ss-1]
        return
    
    mid = (ss+se)//2

    build_tree( 2*si , ss , mid )
    build_tree( 2*si+1 , mid+1 , se )

    st[si] = min( st[2*si] , st[2*si+1] )


"""

update_tree( int si , int ss , int se , int qi )
- si : index of the final array .
- ss : starting index of the array .
- se : ending index of the array .
- qi : index of value to be updated .

"""

def update_tree( si , ss , se , qi ): # qi index of value to be updated
    if ss==se:
        st[si] = A[ss]
        return
    
    mid = (ss+se) //2
    if qi<=mid:
        update_tree(2*si   ,  ss   ,mid   ,qi)
    else:
        update_tree(2*si+1 , mid+1 ,  se  ,qi)
    st[si] = min( st[2*si] , st[2*si+1] )

"""

query( int si , int ss , int se , int qs , int qe)
- si : index of the final array .
- ss : starting index of the array .
- se : ending index of the array .
- qs : starting index of the range query .
- qe : ending index of the range query .

"""
def query(si,ss,se,qs,qe):
    # print("si,ss,se,qs,qe",si,ss,se,qs,qe)
    if qs > se or qe <ss:
        return INF
    if ss>=qs and se<=qe:
        return st[si]
    mid = ( ss + se )//2
    l = query(2*si  , ss    , mid, qs , qe )
    r = query(2*si+1, mid+1 , se , qs , qe )
    return min(l,r)

"""

- A : Input index .
- st : Created Segment tree for input .

"""

A = [4,3,-1,2,8]
INF = int(1e9)
st = [ INF for _ in range(4*len(A)) ]
# length og the final output list(Array) to be sorted later.

build_tree(1,1,len(A))
print(st)

print( query(1,1,5,3,5) )

# Update Code.
A[2] = 10
update_tree(1,1,5,3)

# Check the status after the update.
print( "st" , st )
print( "A"  , A  )
print( query(1,1,5,3,5) )

"""
- ss : starting index of input array (Start of Array) .
- se : ending index of input array (End of Array) .
"""