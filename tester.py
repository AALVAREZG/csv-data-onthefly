
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
operations = [sum, max, min]

d = dict()
for i,op in enumerate(operations):
    d[op.__name__] = values[i]
print("dictionary created: ", d)
