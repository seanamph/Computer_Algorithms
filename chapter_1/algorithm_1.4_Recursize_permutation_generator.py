def Perm(a, k , n):
  if(k == n):
    printall(a) # Output permutation 
  else:
    # a[k:n] has more than one permutation 
    # Generate these recursively.
    for i in range(k,n,1):
      t=a[k]
      a[k] = a[i]
      a[i] = t
      Perm(a,k+1,n)
      # All permutations of a[k+1:n] 
      t=a[k]
      a[k] = a[i]
      a[i] = t

def printall(a):
  s = ""
  for i in range(0,len(a),1):
    s = s + (F"{a[i]}")
  print(s)
    

Perm(["a","b", "c"], 0 , 3)