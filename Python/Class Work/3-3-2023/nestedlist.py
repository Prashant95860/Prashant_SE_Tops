quiz = {
    1 :{
        "que" : "Most popular programming language?",
        "ans" : "PYTHON"
        },
    2 : {
        "que" : "Who is prime minister of india?",
        "ans" : "NARENDRA MODI"
       
        }
    }


for i in range(1,len(quiz)+1):
    print(quiz[i]["que"])
    ans = input("Enter Answer : ").upper()
    if ans == quiz[i]["ans"]:
        print("Right Answer")
    else:
        print("Wrong Answer")


    # if answer will print in lower or uppar after ans ".lower()" is used.
