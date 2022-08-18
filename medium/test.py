a= [ [ "1","2","3"],["4","5","6"] , ["7","8","9"] ]
print(a) 

b =[ [ sub[i] for sub in a ] for i in range(3) ]
print(b)