print("TIC TAK TOI GAME!!!")
a,b,c,d,e,f,g,h,i = 1,2,3,4,5,6,7,8,9
print(a,b,c)
print(d,e,f)
print(g,h,i)
 
selected = ""
for j in range(1,10):
    user_input = int(input(f"enter your choice\n"))
    #number 1
    if user_input == 1 and selected == "":
        a = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 1 and selected == "o":
        a = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 1 and selected == "x":
        a = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    # number 2
    elif user_input == 2 and selected == "":
        b = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 2 and selected == "o":
        b = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 2 and selected == "x":
        b = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    
    #number 3
    elif user_input == 3 and selected == "":
        c = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 3 and selected == "o":
        c = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 3 and selected == "x":
        c = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    # number 4
    elif user_input == 4 and selected == "":
        d = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 4 and selected == "o":
        d = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 4 and selected == "x":
        d = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    # number 5
    elif user_input == 5 and selected == "":
        e = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 5 and selected == "o":
        e = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 5 and selected == "x":
        e = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    # number6
    elif user_input == 6 and selected == "":
        f = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 6 and selected == "o":
        f = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 6 and selected == "x":
        f = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    # number 7
    elif user_input == 7 and selected == "":
        g = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 7 and selected == "o":
        g = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 7 and selected == "x":
        g = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    # number 8
    elif user_input == 8 and selected == "":
        h = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 8 and selected == "o":
        h = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 8 and selected == "x":
        h = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    # number 9
    elif user_input == 9 and selected == "":
        i = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 9 and selected == "o":
        i = "x"
        selected = "x"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    elif user_input == 9 and selected == "x":
        i = "o"
        selected = "o"
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    
     #winning condition 1 row condition
    if a==b and b==c:
        print(f"{a} win the game")
        break
    if d==e and e==f:
        print(f"{d} win the game")
        break
    if g==h and h==i:
        print(f"{g} win the game")
        break
        #column condition
    if a==d and d==g:
        print(f"{a} win the game")
        break
    if b==e and e==h:
        print(f"{b} win the game")
        break
    if c==f and f==i:
        print(f"{c} win the game")
        break
        #diagnol condition
    if a==e and e==i:
        print(f"{a} win the game")
        break
    if c==e and e==g:
        print(f"{c} win the game")
        break