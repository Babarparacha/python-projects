
scores=[]
while True:
    score=input("enter a text score (or 'done):")
    if score.lower()=='done':
        print("goodbye")
        break
    
    scores.append(float(score)) 
    average=sum(scores)/len(scores)
    print(f"average score :{average:1f}")
    if average>=90:
     print("grade A") 
    elif average>=80:
     print("grade B") 
    elif average>=70:
     print("grade C") 
    else:
     print("grade D or fail") 