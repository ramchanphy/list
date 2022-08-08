question_list=["How many continents are there?","what is the capital of india?","NG mei kaun se cource padhaya jaata hai?"]
options_list=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counseling","tourism","Agriculture"]]
life_line=[["seven","eight"],["bhopal","delhi"],["software engineering","counseling"]]
solution_list1=[1,2,1]
life_line1=5050
i=0
count=0
solution_list=[3,4,1]
while i<len(question_list):
    print("q",i+1,question_list[i]) 
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j+=1
    user=input("choose life line:(y/n)")
    if user=="y":
        k=0
        while k<len(question_list):
            print("q",k+1,question_list[k])
            s=0
            while s<len(life_line[k]):
                print(s+1,life_line[k][s])
                s+=1
            user1=int(input(":enter the number"))
            if user1==solution_list1[i]:
                print("congrates")
            else:
                print("wrong answer")
                break
            k+=1
    elif user=="n":
        user1=int(input("enter the correct option"))
        if user1==solution_list[i]:
            print("correct answer")
        else:
            print("wrong answer")
            break
            
    else:
        print("better luck next time")
        break
        
    i+=1