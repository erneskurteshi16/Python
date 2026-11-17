for nr in range(100):
    print(nr) # numron prej 0 deri 99 (total 100 numra)

    print("------------"*4)
    for i in range(-10,11):
        print(i) # numron prej nr te pare deri tek i dyti -1

print("------------"*4)
for step in range(0,15,5):
    print(step) # numron prej nr te pare deri tek i dyti -1 por kalon per aq sa e kemi stepin


seasons=['Spring','Summer','Autumn','Winter',
             'Spring','Summer','Autumn','Winter',
             'Spring','Summer','Autumn','Winter',
             'Spring','Summer','Autumn','Winter',
             'Spring','Summer','Autumn','Winter',
             'Spring','Summer','Autumn','Winter',]
for season in seasons:
    print(season) #iteration over a list

print("------------" * 4)
for i in range(0,len(seasons),5):
        print(seasons[i])


print("------------"*4)
word='computer works for us!'
words=word.split(' ')
for c in words:
        print(c)


logs=['Executed1','Executed2','Executed3','Error','Executed4','Executed5',]
for log in logs:
    if log=='Error':
        break # nderpren teresisht ciklin (loop)
    else:
        print(log)

print("------------"*4)
for log in logs:
    if log=='Error':
        continue #vazhdon ciklin duke injoruar kete hap
    else:
        print(log)

