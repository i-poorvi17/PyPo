s=input('enter the string')
s=s.lower()
count=0
for ch in s :
    if ch in 'aeiou':
        count+=1
        print(ch)
print(count)