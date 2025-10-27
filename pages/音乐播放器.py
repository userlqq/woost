import streamlit as st

#读取音频
st.title('音乐播放器')
music=[
    {
        'url':'https://music.163.com/song/media/outer/url?id=2616468297.mp3',
        'name':'和你等烟花',
        'photo':'https://p1.music.126.net/kqjxcw0rgmTV4MBTTfsyQw==/109951169871520994.jpg',
         'author':'鹭卓'
       
    },
    {
        'url':'https://music.163.com/song/media/outer/url?id=2744358374.mp3',
        'name':'一抹红',
        'photo':'https://p1.music.126.net/BBX-hW-rkH4rfMTDI3UjGQ==/109951171990369335.jpg',
        'author':'王一珩OneSD'
    }
]
#将ind的值存储到streamlit的内存中,如果内存中没有ind,才要设置成0,否则不需要
if 'ind' not in st.session_state:
   st.session_state['ind']=0

#define的定义
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(music)
def prevImg():
    st.session_state['ind']=(st.session_state['ind']-1) % len(music)


#将一行分成两列
c1,c2=st.columns([1,2])

with c1:
    #st.button()按钮,text:按钮的文字,on_click:点击按钮之后要做的事情
   st.image(music[st.session_state['ind']]['photo'])


with c2:
    #st.button()按钮,text:按钮的文字,on_click:点击按钮之后要做的事情
    st.title(music[st.session_state['ind']]['name'])
    st.text(music[st.session_state['ind']]['author'])
    st.audio(music[st.session_state['ind']]['url'],autoplay=True)
   
a1,a2=st.columns([1,2])

with a1:
   st.button('上一首',on_click=prevImg,use_container_width=True)

with a2:
   st.button('下一首',on_click=prevImg,use_container_width=True)
   

    




