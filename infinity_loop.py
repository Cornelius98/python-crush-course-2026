#Infinity loop - intentional
while(1):
    print("Infinity loop")
    break


#Infinity loop - accident
k = 0
while (k < 100):
    #k = k + 1
    print(k, " Accidental infinity loop")


#Keyboard infinity loop
isKeyPressed = 0
while(isKeyPressed == 1):
    isKeyPressed = input()