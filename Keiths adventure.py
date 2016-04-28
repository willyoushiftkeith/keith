
# coding: utf-8

# In[1]:

print("Hi, My name is Keet")


# In[2]:

r=0
while(r==0):
    x=input("will you shift me? (y/n)")
    if(x=="y"):
        print("Keet is about to kiss you")
    else:
        print("Oh...")
        y=input("sure?(y/n)")
        if(y=="n"):
            w=input("so you do want to?")
            if(w=="y"):
                print("prepare your mouth")
                print("Welcome to the meat canyon")
            else:
                print("GAME OVER")
                z=input("Would you like to play again?(y/n)")
                if(z=="y"):
                    r=0
                else:
                    r=1
        else:
            print("GAME OVER")
            z=input("Would you like to play again?(y/n)")
            if(z=="y"):
                r=0
            else:
                r=1


# In[ ]:



