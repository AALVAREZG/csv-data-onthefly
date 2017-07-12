
'''list of function'''
values=[1,2,3]
original_values = values
funcs=[sum, min, max]
for f in funcs:
    value=f(values)
    print(value)

'''map and reduce'''
#M=map(lambda x: (float(x),1), (x['tip_amount'] for x in csv.DictReader(io.StringIO(urllib.request.urlopen(url).read().decode('utf-8')))))
#R = reduce(lambda x, y: (x[0] + y[0], x[1] + 1), M) 

'''list comprenhension'''
print(values)
new_val = 5
funcs2=[]
values=[f((values[i],new_val)) for i,f in enumerate(funcs)]
print(values)
'''generator'''
generator=(f(original_values) for f in funcs)
print(generator)
for f in generator:
    print(f)

'''dicts'''
values=[15,5,1]
operations = [sum, max, min]

d = dict()
for i,op in enumerate(operations):
    d[op.__name__] = values[i]
print("dictionary created: ", d)


dn = {op.__name__:val for op,val in zip(operations,values)}
print("new dictionary created in pythonic way: ", dn)

'''strings to list'''
input="""Card read UID: 67,149,225,43
Size: 8
Sector 8 [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"""
#find index position of 'Sector' text and select from this using slices.
inputn = input[input.index('Sector')+9:] 
DATA = [int(item) for item in inputn[1:-1].split(',')]
DATAm = list(map(int, inputn[1:-1].split(',')))
print((DATA))
print('Data Map: ', DATAm) 
print('test map:', '-'.join(map(str, range(10))))
print(sum(DATA))

'''list'''
a=[8,2,3,4,5]
b=[6,7,8,9,10]
c=(a,b)
print('list c: ', c)
#list c:  ([8, 2, 3, 4, 5], [6, 7, 8, 9, 10])
d=(*a,*b)
print('list d: ', d)
#list d:  (8, 2, 3, 4, 5, 6, 7, 8, 9, 10)
e=[[i, j] for i, j in zip(a,b)]
print('list e: ', e)
#list e:  [[8, 6], [2, 7], [3, 8], [4, 9], [5, 10]] --->list of list
f=list(zip(a,b))
print('list f: ', f)
#list f:  [(8, 6), (2, 7), (3, 8), (4, 9), (5, 10)] --->list of tuples