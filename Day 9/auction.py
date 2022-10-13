print("Welcome to the secret auction program.")
end=False
dict_bidder={}
while not end:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    dict_bidder[name]=bid
    cont=input("Are there anyother bidders? Type 'yes' or 'no'.")
    if cont=="no":
        end=True
max_bid=-1
max_name=""
for key in dict_bidder:
    if dict_bidder[key]>max_bid:
        max_bid=dict_bidder[key]
        max_name=key

print(f"The winner is {max_name} with a bid of ${max_bid}")
