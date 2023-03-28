def TowersOfHanoi(n, x, y, z):
  # Move the top n disjs from tower x to tower y
  if n >= 1:
    TowersOfHanoi(n-1,x,z,y)
    print(F"#{n} move top disk from tower " + x + " to top of tower " + y)
    TowersOfHanoi(n-1,z,y,x)

TowersOfHanoi(3, "A", "B", "C")