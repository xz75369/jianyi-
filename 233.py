# -*-coding:gbk-*-

import tkinter

root = tkinter.Tk()

root.minsize(280, 500)
root.title = '薛政的简易计算器'

#界面显示主要的实现方式
result = tkinter.StringVar()
result.set(0)
result2 = tkinter.StringVar()
result2.set('')

label = tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd = '9',fg = '#828282', anchor ='se', textvariable = result2)
label.place(width = 280, height = 170)
label2 = tkinter.Label(root,font = ('微软雅黑',30),bg = '#EEE9E9',bd = '9',fg = 'black', anchor ='se', textvariable = result)
label2.place(y = 170, width = 280, height = 60)

#下面是运算数字的界面显示
btn7 = tkinter.Button(root,text = '7',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('7'))
btn7.place(x=0,y=285,width=70,height=55)

btn8 = tkinter.Button(root,text = '8',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('8'))
btn8.place(x=70,y=285,width=70,height=55)

btn9 = tkinter.Button(root,text = '9',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('9'))
btn9.place(x=140,y=285,width=70,height=55)


btn4 = tkinter.Button(root,text = '4',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('4'))
btn4.place(x=0,y=340,width=70,height=55)

btn5 = tkinter.Button(root,text = '5',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('5'))
btn5.place(x=70,y=340,width=70,height=55)

btn6 = tkinter.Button(root,text = '6',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('6'))
btn6.place(x=140,y=340,width=70,height=55)

btn1 = tkinter.Button(root,text = '1',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('1'))
btn1.place(x=0,y=395,width=70,height=55)

btn2 = tkinter.Button(root,text = '2',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('2'))
btn2.place(x=70,y=395,width=70,height=55)

btn3 = tkinter.Button(root,text = '3',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('3'))
btn3.place(x=140,y=395,width=70,height=55)

btn0 = tkinter.Button(root,text = '0',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : press_num('0'))
btn0.place(x=70,y=450,width=70,height=55)

#运算符号的界面实现
btnac = tkinter.Button(root,text = 'AC', bd = 0.5,font = ('黑体',20), fg = 'orange',command = lambda : anjian_shixian('AC'))
btnac.place(x = 0, y =230,width = 70,height = 55)

btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20), fg = '#4F4F4F',bd=0.5,command = lambda : anjian_shixian('b'))
btnback.place(x = 70, y =230,width = 70,height = 55)

btndivid = tkinter.Button(root,text = '÷',font = ('微软雅黑',20), fg = '#4F4F4F',bd=0.5,command = lambda : anjian_shixian('/'))
btndivid.place(x = 140, y =230,width = 70,height = 55)

btnmul = tkinter.Button(root,text = '×',font = ('微软雅黑',20), fg = '#4F4F4F',bd=0.5,command = lambda : anjian_shixian('*'))
btnmul.place(x = 210, y =230,width = 70,height = 55)

btnsub = tkinter.Button(root,text = '－',font = ('微软雅黑',20), fg = '#4F4F4F',bd=0.5,command = lambda : anjian_shixian('-'))
btnsub.place(x = 210, y =285,width = 70,height = 55)

btnadd = tkinter.Button(root,text = '＋',font = ('微软雅黑',20), fg = '#4F4F4F',bd=0.5,command = lambda :anjian_shixian('+'))
btnadd.place(x = 210, y =340,width = 70,height = 55)

btnequl = tkinter.Button(root,text = '=',bg='orange', font = ('微软雅黑',20), fg = '#4F4F4F',bd=0.5,command = lambda : jisuan_jieguo())
btnequl.place(x = 210, y =395,width = 70,height = 110)

btnper = tkinter.Button(root,text = '%',font = ('微软雅黑',20), fg = '#4F4F4F',bd=0.5,command = lambda : anjian_shixian('%'))
btnper.place(x = 0, y =450,width = 70,height = 55)

btnpoint = tkinter.Button(root,text = '.',font = ('微软雅黑',20), fg = '#4F4F4F',bd=0.5,command = lambda : anjian_shixian('.'))
btnpoint.place(x = 140, y =450,width = 70,height = 55)








##以下为主要实现的函数：
list = []
anxianum = False
anxiajia = False

def press_num(num):
    global list
    global anxiajia

    if anxiajia == False:
        pass
    else:
        result.set(0)
        anxiajia = False

    old_num = result.get()
    if old_num == '0':
        result.set(num)
    else:
        new_num = old_num + num
        result.set(new_num)




def anjian_shixian(sign):
    global list
    global anxiajia

    num = result.get()
    list.append(num)
    list.append(sign)

    anxiajia = True


    if sign == 'AC':
        list.clear()
        result.set(0)

    if sign == 'b':
        a = num[:-1]
        list.clear()
        result.set(a)


def jisuan_jieguo():
    global list
    global anxianum

    yunsuanfu = result.get()
    list.append(yunsuanfu)

    shuju = ''.join(list)
    jieguo = eval(shuju)

    result.set(jieguo)
    result2.set(shuju)
    list.clear()



root.mainloop()