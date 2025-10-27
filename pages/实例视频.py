import streamlit as st

st.set_page_config(page_title='视频播放',page_icon='🏔')

#视频网址
video_url=[{
    'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
    'title':'熊出没之丛林总动员',
    'episode':'1'
    },{
    'url':'https://www.w3schools.com/html/movie.mp4',
    'title':'熊出没之丛林总动员',
    'episode':'2'
    },{
    'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',
    'title':'熊出没之丛林总动员',
    'episode':'3'
    }]

if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.video(video_url[st.session_state['ind']]['url'])

def play(arg):
    #点击哪个按钮,就播放那个
    st.text(arg)
    #将传递过来的值赋值给内存中的ind
    st.session_state['ind']=int(arg)-1

c1,c2,c3=st.columns(3)
with c1:
    st.button('第一集',use_container_width=True,on_click=play,args=([1]))
with c2:
    st.button('第二集',use_container_width=True,on_click=play,args=([2]))
with c3:
    st.button('第三集',use_container_width=True,on_click=play,args=([3]))
