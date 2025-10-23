import streamlit as st

#st.image()总共两个参数,url: 图片地址 caption:图片的备注
st.set_page_config(page_title='动物音乐',page_icon='🦊')
#图片对象数组
images=[
    {
        'url':'https://breedingbusiness.com/wp-content/uploads/2021/07/cutest-small-white-dog-breeds.jpg',
        'parm':'狗'
    },
    {
         'url':'https://www.depthworld.com/wp-content/uploads/2020/09/top-10-interesting-facts-about-goat.jpg',
        'parm':'山羊'
    },
    {
         'url':'https://cdn.pixabay.com/photo/2016/08/25/17/59/tropical-fish-1620235_960_720.jpg',
        'parm':'鱼'
    }
]
#将ind的值存储到streamlit的内存中,如果内存中没有ind,才要设置成0,否则不需要
if 'ind' not in st.session_state:
   st.session_state['ind']=0

#define的定义
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(images)

    

st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])

#将一行分成两列
c1,c2=st.columns(2)

with c1:
    #st.button()按钮,text:按钮的文字,on_click:点击按钮之后要做的事情
    st.button('上一张',on_click=nextImg)

with c2:
    #st.button()按钮,text:按钮的文字,on_click:点击按钮之后要做的事情
    st.button('下一张',on_click=nextImg)

    




