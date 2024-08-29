
s_list=[]

def add_item(str):
    s_list.append(str)

def remove_item(str):
    if str in s_list:
        s_list.remove(str)

def search_item(str):
    if str in s_list:
        return bs(0,len(str)-1,str)
    else :
        return False

def display_list():
     print(s_list)

def bs(low , high,word):
    if low==high:
        return word[low]
    mid=(low+high)//2
    left=bs(low,mid,word)
    right=bs(mid+1,high,word)
    temp=""
    temp+=right
    temp+=left
    return temp



while(1):
    opt=int(input("enter the below options \n1 to add item\n2 to remove item\n3 to search item\n4 to display item\n5 to exit:")) 
    if opt==1:
        inp=input("enter item to add:")
        add_item(inp)
        
    elif opt==2:
        inp=input("enter item to remove:")
        remove_item(inp)
    elif opt==3:
        inp=input("enter item to search:")
        print(search_item(inp))
    elif opt==4:
        display_list()
    elif opt==5:
        break
    else:
        print("invalid option try again")
    
        


