import streamlit as st

st.set_page_config(layout='wide')

# 使用with语法
with st.sidebar:
    st.title('菜单栏')
    add_radio = st.radio(
        "选择页面",
        ("项目介绍", "专业数据分析", "成绩预测")
    )

st.title("学生成绩分析与预测系统")
st.markdown('***')
st.subheader("项目概述")
st.markdown('本系统是一个专注于学生成绩分析的平台,通过数据整合与模型'\
            '算法,利用数据可视化和机器学习技术,为教育者和学生提供一个'\
            '良好的学习教育平台,能更直观的知道自己的不足之处')
st.subheader("主要特点:")
st.markdown('''
     - 数据可视化
     - 成绩专业分析
     - 智能预测
     - 学习建议
     ''')

st.markdown('***')
st.subheader("项目目标")

a1,a2,a3=st.columns([2,2,2])
with a1:
    st.markdown("目标一")
    st.text('分析影响目标')
    st.markdown('''
    - 识别关键学习指标
    - 探索成绩相关因素
    - 提供数据支持决策
    ''')

with a2:
    st.markdown("目标二")
    st.text('可视化展示')
    st.markdown('''
    - 专业对比分析
    - 性别差异分析
    - 学习模式识别、对比
    ''')

with a3:
    st.markdown("目标三")
    st.text('成绩预测')
    st.markdown('''
    - 机器学习模型
    - 个性化识别、预测
    - 及时干预警告
    ''')
    
st.markdown('***')
st.subheader("技术架构")
b1,b2,b3,b4=st.columns(4)
with b1:
    technology=st.selectbox('前端框架',['Streamlit'])

with b2:
     technology=st.selectbox('数据处理',['Pandas','Numpy'])
     
with b3:
     technology=st.selectbox('建模工具',['Scikit-learn'])

with b4:
     technology=st.selectbox('部署环境',['Sreamlit Cloud'])
     
    


            

            

            
    



