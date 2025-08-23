E = {0,2,4,6,8}
N = {1,2,3,4,5}

print(f'''
Intersection   : {E.intersection(N)}
Union          : {E.union(N)}
Difference     : {E.difference(N)}
Sym Difference : {E.symmetric_difference(N)} 
''')