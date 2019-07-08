sort(list):
negative=empty
positive=empty
while(list!=empty):
first=pop(list)
if(first>0):
append(positive,first)
else:
append(negative,first)
return concatenate(negative,positive)
