question_list=["How many continents are there?","what is the capital of india?","NG mei kaun se cource padhaya jaata hai?"]
options_list=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counseling","tourism","Agriculture"]]
life_line=[["seven","eight"],["bhopal","delhi"],["software engineering","counseling"]]
solution_list2=[1,2,1]
lifeline=5050
solution_list=[3,4,1]
i=0
count=0
while i<len(question_list):
    print("q",i+1,question_list[i])
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j+=1
    user=int(input("enter the number"))
    if user==solution_list[i]:
        print("congrates")
    elif user==5050:
        if count==0:
            k=0
            while k<len(life_line[i]):
                print(k+1,life_line[i][k])
                k+=1
            count+=1
            user2=int(input("enter the number"))
            if user2==solution_list2[i]:
                print("correct")
            else:
                print("wrong")
        else:
            print("you already use 5050 chances")
            num=int(input("enter the number:"))
            if num==solution_list[i]:
                print("right answer")
            else:
                print("wrong answer")
                break
    else:
        print("your answer is wrong")
        break
    i+=1
                