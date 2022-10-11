arr=[[" "," "," "],[" "," "," "],[" "," "," "]]
print(arr)
position=input("Where do you want the list: ")
row=int(position[0])
col=int(position[1])

arr[row][col]="X"
print(arr)