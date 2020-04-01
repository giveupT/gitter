import requests
from bs4 import BeautifulSoup 
import urllib
def gedanye(w):
    gedan= 'https://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=%s'%w          
    return gedan
s = requests.session()
t=0
while t>=0:
    bs = BeautifulSoup(s.get(gedanye(t*35)).content, "lxml")
    t+=1
S=bs.select('ul#m-pl-container li div a.msk')
A,m,B,C,D,E=[],'',[],[],{},{}
for t in S:
    A.append(t['href'])
for y in A:
    for u in y:
        if u in ['1','2','3','4','5','6','7','8','9','0']:
            m+=u
    B.append(m)
    m=''
for i in S:
    C.append(i['title'])
ff=len(C)
for e in range(0,ff):
    E[B[e]]=C[e]    #id对名称的字典
gg= 'https://music.163.com/playlist?id=2819914042' 
s = requests.session()
bs = BeautifulSoup(s.get(gg).content, "lxml")
def musiclist_stat(r):
    musit={}    
    hhh=r.find('ul',{'class':"f-hide"}).find_all('a')
    for tag in hhh:
        musit[tag['href'].strip('/song?id=')]=tag.text
    return musit
A,B=[],[]
D=musiclist_stat(bs)
for u in D:
    A.append(u)
    B.append(D[u])
def xiazai(a,b):
    try:
        song='http://music.163.com/song/media/outer/url?id=%s.mp3'%a
        urllib.request.urlretrieve(song,'C:/Users/lenovo/Desktop/text/%s.mp3'%b)
        print('下载完成，开始播放，等待，并聆听')
    except KeyError:
        print("不能下载哦")
for y in A:
    xiazai(y,B[A.index(y)])
fi=tk.Tk()
fi.title("登陆界面")
label_x=tk.Label(fi,text="用户名:")
label_y=tk.Label(fi,text="密码:")
textbox_1=tk.Text(fi,height=1,width=10)
textbox_2=tk.Text(fi,height=1,width=10)
button=tk.Button(fi,text="确认",command=lambda:querenbut(textbox_1,textbox_2))
button_1=tk.Button(fi,text="退出",command=lambda:tuichu())
fi.geometry('200x100+550+300')
def querenbut(textbox_1,textbox_2):
    a=textbox_1.get('0.1',tk.END)[:-1]
    b=textbox_2.get('0.1',tk.END)[:-1]
    if a==Name["A1"]["用户名"] and b==Name["A1"]["密码"]:
        return fi.destroy(),wc()
    elif a==Name["A2"]["用户名"] and b==Name["A2"]["密码"]:
        return fi.destroy(),wc()
    else:
        return wr()
def tuichu():
    return fi.destroy()
label_x.grid_configure(column=1,row=1,columnspan=1,rowspan=1)
label_y.grid_configure(column=1,row=2,columnspan=1,rowspan=1)
textbox_1.grid_configure(column=2,row=1,columnspan=1,rowspan=1)
textbox_2.grid_configure(column=2,row=2,columnspan=1,rowspan=1)
button.grid_configure(column=1,row=3,columnspan=1,rowspan=1)
button_1.grid_configure(column=2,row=3,columnspan=1,rowspan=1)
fi.mainloop()