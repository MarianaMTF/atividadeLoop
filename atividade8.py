for i in range(1,51):
  primo=0
  for aux in i:
    if i%aux==0:
      primo=primo+1
  if primo==2:
    print(i)
