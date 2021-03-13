dicts = [   
    {'name':'','midg':0,'prog':0,'finalg':0,'passg':0},
    {'name':'','midg':0,'prog':0,'finalg':0,'passg':0},
    {'name':'','midg':0,'prog':0,'finalg':0,'passg':0},
    {'name':'','midg':0,'prog':0,'finalg':0,'passg':0},
    {'name':'','midg':0,'prog':0,'finalg':0,'passg':0},
        ]
finalgrades = []
for i in range(5):
    
    dicts[i]['name'] = input('Please enter student name')
    dicts[i]['midg'] = float(input('Please enter midterm grade'))
    dicts[i]['prog'] = float(input('Please enter project grade'))
    dicts[i]['finalg'] = float(input('Please enter final grade'))
    dicts[i]['passg'] = dicts[i]['midg']*0.3 + dicts[i]['prog']*0.3 + dicts[i]['finalg']*0.4  
    finalgrades.append(dicts[i]['passg'])
 
finalgrades.sort(reverse=True)
print(finalgrades)
a = input()