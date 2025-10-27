import streamlit as st
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
