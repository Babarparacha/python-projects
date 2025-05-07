import random
firt_parts=['sky','noor','moon','sun','fire']
last_parts=['aslam','hamid','beiber','collaps','willams']

count=int(input('how many name do you want?'))
for i in range(count):
 first=random.choice(firt_parts)
 last=random.choice(last_parts)
 print(f"{first} {last}")