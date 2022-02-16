question_list=["How many continents are there?","what is the capital of india?","NG mei kaun se cource padhaya jaata hai?"]
options_list=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counseling","tourism","Agriculture"]]
life_line=[["seven","eight"],["bhopal","delhi"],["software engineering","counseling"]]
solution_list=[1,2,1]
i=0
count=0
solution_list=[3,2,1]
while i<len(question_list):
    print("q",i+1,question_list[i])
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j+=1
    user=int(input("enter the number"))
    if solution_list[i]==user:
        print("congrats!your answer is correct")
    # elif user==5050:
    #     if count==0:
    #         k=0
    #         while k<len(life_line[i]):
    #             print(k+1,life_line[i][j]) 
    #             k+=1
            # count+=1       
    else:
        print("sadly,you answer is wrong")
    i+=1