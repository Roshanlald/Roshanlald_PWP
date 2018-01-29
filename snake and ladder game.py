#snake and ladder game
import random
N=0
while (N<=100):
    roll=input("enter "r" to roll a dice")
    if(roll=='r'):
        r=random.randint(1,6)
        N=N+r
        print("you are in position",N)
        if N==8:
            N=37
            N=N+r
            print("you just climed a ladder and you are in position",N)
        elif N==11:
            N=2
            N=N+r
            print("ooh,you got bitten by a snake and you are in position",N)
        elif N==13:
            N=34
            N=N+r
            print("you just got on a ladder and you are in position",N)
        elif N==25:
            N=4
            N=N+r
            print("oh no a snake bite you and you are in position",N)
        elif N==38:
            N=9
            N=N+r
            print("a snake bite you and now your position is",N)
        elif N==40:
            N=68
            N=N+r
            print("on the ladder and you climed to",N)
        elif N==52:
            N=81
            N=N+r
            print("got on a ladder and now you are in",N)
        elif N==65:
            N=46
            N=N+r
            print("got bite by a snake and your going down to",N)
        elif N==76:
            N=97
            N=N+r
            print("you just climed a ladder and now your position is",N)
        elif N==89:
            N=70
            N=N+r
            print("got bite by a snake and you are now going down to",N)
        elif N==93:
            N=64
            N=N+r
            print("unfortunately got bite by a snake and now you r going down to",N)
    else:
        N<=100
        print("congratulations you have won the game")
