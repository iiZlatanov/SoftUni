data = input()
opening_index = []

for i in range(len((data))):
    ch = data[i]

    if ch == "(":
        opening_index.append(i)#if we have opening parenthesis, this if adds its index in the list named opening index
    elif ch == ")":
        print(data[opening_index[-1]: i + 1])#when we get a closing parenthesis, here we print the data from the index that was in the opening index to the index that was found to be closing parenthesis
        opening_index.pop()#here we clear the index that was taken as an opening parenthesis

