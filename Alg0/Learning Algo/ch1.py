def flawed(A):

    my_max = A[0]

    for i, value in enumerate(A):
        if my_max < A[i]:
            my_max = A[i]
    return my_max

# code above have big 0 of 0n
# I have used enumerate to loop through the list 
# if not then I have to use

####  for idx in range(1, len(A)): ####

my_list = range(0,101)

print(flawed(my_list))

