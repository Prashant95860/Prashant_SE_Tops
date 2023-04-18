def perfect(n):
    sum = 0
    for x in range(1,n):
        if n % x== 0:
            sum += x
    if(sum==n):
        print("Number is perfect")
    else:
        print("Number is not perfect")


perfect(6)
