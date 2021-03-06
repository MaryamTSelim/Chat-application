import tkinter
import socket
import _thread
import sys
i = 3
client = 0
def sendMessage ():
    msg = 'client:\t'+txt.get()
    client.send(msg.encode('ascii'))
    global i
    msglbl = tkinter.Label(window,text=msg)
    msglbl['font']=35
    msglbl['bg']='white'
    msglbl['width']=92
    msglbl.grid(columnspan=2,column=0,row=i,padx=5)
    i+= 1

def recievingMessage (c): 
    global i
    while True :
        msg=c.recv(2048).decode('ascii')
        if not msg :
            sys.exit(0)
        msglbl = tkinter.Label(window,text=msg)
        msglbl['font']=35
        msglbl['bg']='white'
        msglbl['width']=92
        msglbl.grid(columnspan=2,column=0,row=i,padx=5)
        i += 1
#Socket Creation
def socketCreation ():    
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    host = '127.0.0.1'
    port = 7510
    c.connect((host,port))
    global client
    client = c
    send['command'] = sendMessage
    _thread.start_new_thread(recievingMessage, (c,) )


#Creating a window
window = tkinter.Tk()
window.title('client')
window['bg']='gray98'
window['padx']=10
window['pady']=10
#Adding Elements
#Entry
txt = tkinter.Entry(window)
txt['width']=100
txt['relief']=tkinter.GROOVE
txt['bg']='white'
txt['fg']='green'
txt['font']=35
txt.grid(column=0,row=1,padx=5,pady=15)
#Button
send = tkinter.Button(window,text="send")
send['relief']=tkinter.GROOVE
send['bg']='white'
send['fg']='green'
send['activebackground']='ivory3'
send['padx']=3
send['font']=35
send.grid(column=1,row=1,padx=5,pady=15)
#Lable
lbl = tkinter.Label(window,text='Starting Chat Application')
lbl['font']=35
lbl['bg']='white'
lbl['width']=92
lbl.grid(columnspan=2,column=0,row=2,padx=5)
_thread.start_new_thread(socketCreation, () )


window.mainloop()