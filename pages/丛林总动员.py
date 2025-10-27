import streamlit as st

st.set_page_config(page_title='视频播放',page_icon='🏔')

#视频网址
video_url=[{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/00/04/31990810400/31990810400-1-192.mp4?e=ig8euxZM2rNcNbRghWdVhwdlhWN1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=161998f786d44e5a864781202e3f611h&deadline=1761303418&mid=0&gen=playurlv3&os=cosovbv&og=ali&nbs=1&uipk=5&oi=771356656&upsig=38bb528832d1e1fee52a711ee820dad7&uparams=e,platform,trid,deadline,mid,gen,os,og,nbs,uipk,oi&bvc=vod&nettype=0&bw=974009&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1.mp4',
    'title':'熊出没之丛林总动员',
    'episode':'06-乌龙拍档'
    },
     {
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/73/12/31991071273/31991071273-1-192.mp4?e=ig8euxZM2rNcNbRgnwdVhwdlhWN3hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&mid=0&uipk=5&trid=f1959dfbf89840c084b7d731f0a45cfh&gen=playurlv3&os=cosovbv&og=hw&platform=html5&oi=771356656&deadline=1761303725&upsig=0db4bad705cececf7fda91beb9848b22&uparams=e,nbs,mid,uipk,trid,gen,os,og,platform,oi,deadline&bvc=vod&nettype=0&bw=1032348&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1.mp4',
    'title':'熊出没之丛林总动员',
    'episode':'07-至尊权杖'
    },
    {
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/95/93/31991399395/31991399395-1-192.mp4?e=ig8euxZM2rNcNbR1hWdVhwdlhWR1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&uipk=5&platform=html5&deadline=1761303903&gen=playurlv3&trid=39f86f9a6c2a4fcd8dd8f58ec6b169dh&mid=0&oi=771356656&os=cosovbv&og=hw&upsig=6a987890b77e193d31848609a3934aca&uparams=e,nbs,uipk,platform,deadline,gen,trid,mid,oi,os,og&bvc=vod&nettype=0&bw=889136&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1.mp4',
    'title':'熊出没之丛林总动员',
    'episode':'08-熊二的蜂蜜'
    }
]

if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.video(video_url[st.session_state['ind']]['url'])
st.title(video_url[st.session_state['ind']]['title']+'-第'+ video_url[st.session_state['ind']]['episode']+'集')

def play(arg):
    #点击哪个按钮,就播放那个
    st.text(arg)
    #将传递过来的值赋值给内存中的ind
    st.session_state['ind']=int(arg)

for i in range(len(video_url)):
    st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))

