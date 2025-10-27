import streamlit as st
from datetime import datetime, timedelta
from datetime import datetime, time
#分成c1,c2两列

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
         
     
        
    
     

   

     
     
     
                              
         
     
    
     
     
      
    
