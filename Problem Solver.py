#THIS CODE IS CREATED BY PHOENIX(THE OWNER OF GS HERE IS THE GAMING STATION OFFICIAL PAGE LINK https://gamesunlockd.blogspot.com/?m=1), AND ALL UPDATES ON THIS CODE WILL BE PROVIDED ON THE OFFICIAL WEBSITE OF PHOENIX
#THIS CODE IS ENTIRELY MADE FOR EDUCATIONAL PURPOSE ANY MISUSE OF THIS CODE SHALL BE PUNISHED

print("""Hello World
\n""")
name=input("Enter Your Name to contineu\n")
print("Welcome " + name )
value=input("Enter 1 for coordinate solver and 2 for INTEGERS SOLVER\n")
#if you want to add more to this equation solver change this part
value=int(value)
import math
if (value==1):
    ask=input("press 1 if asked for distance between 2 points press 2 if asked for midpoint press 3 if asked for slope\n")
    #if u want to add more to coordinate solver change this part
    ask=int(ask)
    if (ask==1):
        x1=input("enter x coordinates of first points\n")
        x2=input("enter x coordinate of second point\n")
        y1=input("enter y coorinate of first point\n")
        y2=input("enter y coordinate of second point\n")
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        D=(x2-x1)**2 + (y2-y1)**2
        distance=math.sqrt(D)
        print(distance)
    if (ask==2):
        x1=input("enter x coordinates of first points\n")
        x2=input("enter x coordinate of second point\n")
        y1=input("enter y coorinate of first point\n")
        y2=input("enter y coordinate of second point\n")
             



if (value==2):
    ask=input("Enter 1 if asked to simplify or SOLVE ,Enter 2 if asked for word problem\n")
    ask=int(ask)
    if (ask==1):
        import math
        question=(input)("ENTER YOUR QUESTION (ONLY ENTER QUESTION Like 2+2-6 not LETTERS)\n")
        e=eval(question)
        #eval command is used to evaluate
        e=str(e)
        print("The answer is " + e)
        e=int(e)
        while True:
                cmd =input('Do you want to quit? Enter q to quit!\n')
                if cmd == 'q':
                             break

    if (ask==2):
        question=(input)('''Enter the question type number according to the question type HERE ARE THE QUESTION TYPES
        1.A shopkeeper gains rupees 1 on each pen and loses 40 paise.....
        
        2.A certain freezing process requires that the room temperature be lowered from 40 degree celcius....

        3.IN A CLASS TEST CONTAINING 20 QUESTIONS,4 MARKS ARE GIVEN FOR EVERY CORRECT ANSWER AND -2 FOR EVERY INCORRECT
        ANSWER RANJITA ATTEMPS ALL QUESTION AND 12 OF HER ANSWER ARE CORRECT WHAT IS HER TOTAL SCORE......

        4.WHAT WILL BE THE SIGN OF PRODUCT IF WE MULTIPLY 90 NEGATIVE AND 9 POSITIVE INTEGERS.....

        5.THE SUM OF TWO INTEGERS IS -12 IF ONE OF THEM IS 43 FIND OTHER\n''')

        question=int(question)
        if(question==1):
            gain=input("ENTER THE GAIN VALUE IN RUPEES ON EACH PEN\n")
            loss=input("ENTER THE LOSS VALUE IN PAISE ON EACH PENCIL\n")
            sell=input("ENTER THE NUMBER OF PENS HE SOLD \n")
            L=input("ENTER THE TOTAL LOSS OR TOTAL GAIN USE + FOR GAIN AND - FOR LOSS FOR EXAMPLE -1 IS LOSS AND +1 IS GAIN\n")
            gain=int(gain)
            loss=int(loss)
            sell=int(sell)
            L=int(L)
            gainonpen=(gain*sell)
            lossonpencil=(loss/100)
            key=(gainonpen-L)
            Pencils=(key/lossonpencil)
            print("The total number of pencils are \n")
            print(Pencils)
            while True:
                cmd =input('Do you want to quit? Enter q to quit!\n')
                if cmd == 'q':
                             break

        if(question==2):
            initialtemp=input("ENTER THE INITIAL TEMPERATURE\n")
            rate=input("ENTER THE RATE AT WHICH TEMPERATURE WAS LOWERED/INCREASED USE '+' FOR INCREASE AND '-' FOR LOWERED\n")
            time=input("ENTER THE TIME PERIOD FOR WHICH TEMP WAS INCREASING OR DECREASING\n")
            time=int(time)
            initialtemp=int(initialtemp)
            rate=int(rate)
            temp=(initialtemp + rate * time)
            time=str(time)
            print("The temperature after " + time + " hour is \n")
            print(temp)
            while True:
                cmd =input('Do you want to quit? Enter q to quit!\n')
                if cmd == 'q':
                             break

        if(question==3):
            numberofq=input("ENTER THE NUMBER OF QUESTIONS PUT 0 IF NOT GIVEN\n")
            marksgiven=input("ENTER THE MARKS GIVEN FOR EACH CORRECT ANSWER PUT 0 IF NOT GIVEN\n")
            markstaken=input("ENTER THE MARKS GIVEN FOR INCORRECT ANSWER USE '-' SIGN PUT 0 IF NOT GIVEN \n")
            ATTEMPTED=input("ENTER THE QUESTIONS ATTEMPTED IF NOT GIVEN IN QUESTION PUT 0\n")
            correct=input("ENTER THE ANSWERS SHE GOT CORRECT IF NOT GIVEN IN QUESTION PUT 0 \n")
            incorrect=input("ENTER THE QUESTIONS THAT WERE INCORRECT PUT 0 IF NOT GIVEN IN QUESTION\n")
            total=input("ENTER THE TOTAL MARKS GOT IN EXAN \n")
            numberofq=int(numberofq)
            marksgiven=int(marksgiven)
            markstaken=int(markstaken)
            ATTEMPTED=int(ATTEMPTED)
            correct=int(correct)
            incorrect=int(incorrect)
            total=int(total)


            find=input("""WHAT DO YOU WANT TO FIND ENTER THE NUMBER       1.HOW MANY ANSWERS WERE CORRECT
            2.HOW MANY QUESTIONS WERE ATTEMPTED       3.TOTAL SCORE IN EXAM     4.)TOTAL NUMBER OF QUESTIONS \n """)
            find=int(find)
            if(find==1):
                if(incorrect>0):
                    if(ATTEMPTED>0):
                        correct=(ATTEMPTED-incorrect)
                        correct=str(correct)
                        print(correct+"answers were correct\n")
                        while True:
                                 cmd =input('Do you want to quit? Enter q to quit!\n')
                                 if cmd == 'q':
                                             break

                    else:
                        if(total>0):
                            if(marksgiven>0):
                                if(markstaken<0):
                                    key=(total-incorrect*markstaken)
                                    key=int(key)
                                    correct=key/marksgiven
                                    correct=str(correct)
                                    print(correct+" answers were correct \n")
                                    while True:
                                            cmd =input('Do you want to quit? Enter q to quit!\n')
                                            if cmd == 'q':
                                                         break

                else:
                     if(total>0):
                        if(ATTEMPTED>0):
                            if(markstaken>0):
                                incorrect=total/markstaken
                                correct=ATTEMPTED-incorrect
                                correct=str(correct)
                                print(correct+" answers were correct")
                                while True:
                                        cmd =input('Do you want to quit? Enter q to quit!\n')
                                        if cmd == 'q':
                                                    break
                        else:
                            if(marksgiven>0):
                                        correct=total/marksgiven
                                        correct=str(correct)
                                        print(correct + " answers were correct")
                                        while True:
                                            cmd =input('Do you want to quit? Enter q to quit!\n')
                                            if cmd == 'q':
                                                         break
            if(find==2):
                #THIS PART WILL NEED UPDATE IN FUTURE
                if(total>0):
                    if(marksgiven>0):
                        if(markstaken<0):
                            if(correct>0):
                                key=total-(marksgiven*correct)
                                incorrect=key/markstaken
                                incorrect=-(incorrect)
                                ATTEMPTED=correct+incorrect
                                ATTEMPTED=str(ATTEMPTED)
                                print(ATTEMPTED + " questions were attempted")
                                while True:
                                            cmd =input('Do you want to quit? Enter q to quit!\n')
                                            if cmd == 'q':
                                                         break
            if(find==3):
                #THIS PART MAY NEED UPDATE
                    if(correct>0):
                        if(incorrect>0):
                            if(markstaken<0):
                                if(marksgiven>0):
                                    total=(correct*marksgiven)+(incorrect*markstaken)
                                    total=str(total)
                                    print("The total score is " + total + " points \n")
                                    while True:
                                            cmd =input('Do you want to quit? Enter q to quit!\n')
                                            if cmd == 'q':
                                                         break
            if(find==4):
                if(numberofq==ATTEMPTED):
                    if(markstaken<0):
                        if(marksgiven>0):
                            if(correct>0):
                                if(total>0):
                                         key=total-(marksgiven*correct)
                                         incorrect=key/markstaken
                                         incorrect=-(incorrect)
                                         numberofq=(correct+incorrect)
                                         numberofq=str(numberofq)
                                         print("The total number of questions are " + numberofq)
                                         while True:
                                                cmd =input('Do you want to quit? Enter q to quit!\n')
                                                if cmd == 'q':
                                                         break
        if(question==4):
            positive=input("Enter the number of positive integers\n")
            negative=input("Enter the number of negative integers\n")
            positive=int(positive)
            negative=int(negative)
            key=negative/2
            if(key==1):
                print("The sign of the product will be positive")
                while True:
                        cmd =input('Do you want to quit? Enter q to quit!\n')
                        if cmd == 'q':
                                    break
            else:
                print("The sign of the product will be negative")
                while True:
                        cmd =input('Do you want to quit? Enter q to quit!\n')
                        if cmd == 'q':
                                    break
        if(question==5):
            sum=input("Enter the sum of integers if not given put x\n")
            diffrence=input("Enter the diffrence between the two integers if not given put x\n")
            firstint=input("Enter the first integer\n")
            sum=int(sum)
            diffrence=int(diffrence)
            firstint=int(firstint)
            if(sum==1):
                second=(firstint+diffrence)
                second=str(second)
                print("The second number is " + second)




                                

                         





            




            
