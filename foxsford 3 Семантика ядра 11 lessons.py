a = []
with open('snow.txt', encoding='utf-8') as f:
    for line in f:
#         for elem in #что выше.split()
        for elem in line.split():
            elem_strip = elem.strip(',.-;:!@#$%^&*-«»""0123456789()[]{}')
            #check
            if len(elem_strip)>=3:
                a.append(elem_strip)
#                 a += elem_strip
#             strip_elem = elem.strip('')
#             if strip_elem:
#                 a.append(strip_elem)
# print(a[:21],end='' )  

d = {}

for elem in a:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1
        
    
#show
cmd = lambda x: -d[x] # d% \n d//10  d any

for w in sorted(d, key=cmd)[:28]:
    print(w, d[w])
