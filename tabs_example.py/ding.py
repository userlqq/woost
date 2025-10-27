import streamlit as st
import pandas as pd    #  导入Pandas并用pd代替
import numpy as np    # 导入numpy并用np代表它

st.title(":blue[***广西职业师范学院***]")
tab1, tab2, tab3 ,tab4,tab5,tab6,tab7= st.tabs(["数字档案", "图片切换", "音乐播放器","南宁美食图","实例视频","丛林总动员","个人简历"])

with tab1:
    st.title('学生 小强-档案')

    st.header("学生信息",anchor='introduction')
    st.markdown('''
             学号:123456789

              性别：男

              年龄:17
              
              年级:高二三班
              
              精神:正常''')


    st.title('兴趣爱好&技能')

    st.subheader('爱好')
        # 定义列布局，分成3列
    c1, c2, c3 = st.columns(3)
    c1.metric(label="书法", value="80%", delta="100%")
    c2.metric(label="唱歌", value="76%", delta="100%")
    c3.metric(label="羽毛球", value="97%", delta="100%")

    st.subheader('技能')
    c1, c2, c3 = st.columns(3)
    c1.metric(label="c语言", value="60%", delta="100%")
    c2.metric(label="python", value="56%", delta="100%")
    c3.metric(label="简介计算机", value="99%", delta="100%")

    st.header("任务日志",anchor='introduction')


    import streamlit as st  
    import pandas as pd

    data = {
        '日期':["2025-10-5", "2025-10-10", "2025-10-16"],
        '任务':["学生数字档案", "课程管理系统", "数据图表展示"],
        '状态':["✔️完成","⭕进行中", "❌未完成"],
        '难度':["一般","简单","较难"]
    }

    # 定义数据框所用的索引
    index = pd.Series(['01', '02', '03'], name='  ')
    # 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)

    st.subheader('任务表')
    st.table(data)

    st.header("最新代码成果",anchor='introduction')

with tab2:
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

        

with tab3:
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

with tab4:
    st.title(":red[🍚南宁美食]")
    st.header("南宁美食地图")
    #准备地图坐标点数据经度、纬度
    map_data={
        'longitude':[108.437870,108.278592,108.374932,108.374267,108.378977],
        'latitude':[22.769158,22.781611,22.765947,22.765353,22.765393],
    }

    st.map(pd.DataFrame(map_data))
    # 定义数据,以便创建数据框
    data = {
        '1号门店':[200, 150, 180,120,145,125,133,178,165,188,179,135],
        '2号门店':[120, 145, 123,165,189,124,125,145,123,156,158,158],
        '3号门店':[110, 100, 160,120,130,164,157,159,211,230,146,145],
        '4号门店':[200, 210, 215,195,189,178,189,186,185,145,165,145],
        '5号门店':[300, 256, 250,145,155,233,146,146,198,168,250,146]
    }

    df = pd.DataFrame(data)
    # 定义数据框所用的新索引
    index = pd.Series(['01','02', '03','04','05','06','07','08','09','10','11','12'], name='月份')
    # 将新索引应用到数据框上
    df.index = index

    st.header(":red[门店数据]")
    #展示数据
    st.table(df)
    #折线图
    st.line_chart(df)
    #柱形图
    st.bar_chart(df)
    #面积图
    st.area_chart(df)

with tab5:
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


with tab6:
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

with tab7:
    c1,c2=st.columns([2,2])
    with c1:
         st.header('个人简历生成器')
         st.markdown('***')
         st.subheader('个人信息表')
         name = st.text_input('姓名：', '光头强')
         unit = st.text_input('单位：', '狗熊岭')
         number = st.text_input('电话：', '12345678910')
         email = st.text_input('邮箱：', '123456789@qq.com')
         date = st.text_input('出生年月：', '2000.10')
         st.subheader('性别')
         check_1=st.checkbox('女',value=False)
         check_2=st.checkbox('男',value=True)
         st.subheader('学历')
         education=st.selectbox('学历选择',['大专及以下','本科','硕士','其他'])
         st.subheader("工作经验")
         values = st.slider(
         '时间',
         0, 50, (0, 10))
         st.write('你选择的范围是：', values)

         st.subheader("期望薪资范围")
         values = st.slider(
         '薪资',
        0, 9000, (6500, 9000))
         st.write('你选择的范围是：', values)
         st.subheader("个人简介")
         init_text = '光头强（Logger Vick），别称“强子”“强哥”，是动画《熊出没》系列中的男主角之一，'\
                    '曾经是一名伐木工和猎人 ，后来转行成了一名导游,光头强常年穿着黄色背心和蓝色裤子，留着'\
                    '平头短发，外形休闲。不戴眼镜，眼睛较大，嘴唇上方有一撇小胡子，显得较为成熟。在生活中，'\
                   '李老板经常催促光头强交付木头并存在拖欠工资的情况，导致光头强多次过年时无法回家。光头强具备多种技能，'\
                   '包括跳舞、游泳、钓鱼、唱歌和发明等。他心地善良，尤其孝敬父母，这一点在《熊出没》系列动画中多次体现。'\
                   '光头强的日常生活丰富多样，他有时会策划新的砍树计划，有时会照顾宠物肥波，有时也会帮助森林里的动物们，'\
                  '还会尝试新的赚钱点子。在某些情节中，光头强会遇到不幸的情况，例如在《熊出没之秋日团团转》第八集中，他'\
                  '因被投诉虐待动物而与动物们和好，但在向检察院报告时泄露了目的，结果被动物们巧妙利用，被不知情的调查员带走。'

         st.text_area(label='：', value=init_text,
                height=200, max_chars=500)
         
         st.subheader("最佳工作时间")
         w1 = st.time_input("8:30-12:00","15:30-18:30")

         photo=st.file_uploader("上传你的照片")
         if photo is not None:
            hhh_rnv=photo.getvalue()
        

    with c2:
        st.subheader("简历实时预览")
        st.markdown('***')
        st.set_page_config(page_title="个人简历生成器", page_icon="", layout="wide")
        st.image(hhh_rnv,width=300)
        
        a1,a2=st.columns([2,1])
        with a1:
             st.write('姓名:',name)
             st.write('单位: ',unit)
             st.write('电话: ',number)
             st.write('邮箱: ',email)
             st.write('出生年月: ',date)

             st.markdown('***')
             st.subheader("个人简介")
             st.text_area(label='：', value=init_text,
                height=300, max_chars=500)

    st.markdown('***')
             




