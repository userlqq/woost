import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# 模拟学生数据（实际可替换为读取真实数据）
def generate_sample_data():
    majors = ["信息系统", "人工智能", "大数据管理", "工商管理", "电子商务", "财务管理"]
    data = []
    for _ in range(100):
        major = np.random.choice(majors)
        study_hours = np.random.uniform(5, 30)
        attendance = np.random.uniform(0.5, 1.0)
        midterm = np.random.uniform(30, 100)
        homework = np.random.uniform(0.5, 1.0)
        # 简单模拟期末成绩与各因素的线性关系
        final = 0.2 * study_hours + 10 * attendance + 0.5 * midterm + 5 * homework + np.random.normal(0, 5)
        final = max(0, min(100, final))  # 限制在0-100之间
        data.append({
            "学号": f"123{np.random.randint(1000, 9999)}",
            "性别": np.random.choice(["男", "女"]),
            "专业": major,
            "每周学习时长（小时）": study_hours,
            "上课出勤率": attendance,
            "期中考试分数": midterm,
            "作业完成率": homework,
            "期末考试分数": final
        })
    return pd.DataFrame(data)

df = generate_sample_data()

# 设置页面标题
st.title("🎇 期末成绩预测")
st.markdown("请输入学生的学习信息，系统将预测其期末成绩并提供学习建议")

# 输入表单
with st.form("prediction_form"):
    student_id = st.text_input("学号", "12321321")
    gender = st.selectbox("性别", ["男", "女"])
    major = st.selectbox("专业", df["专业"].unique())
    study_hours = st.slider("每周学习时长（小时）", 0.0, 30.0, 10.0, 0.5)
    attendance = st.slider("上课出勤率", 0.0, 1.0, 0.6, 0.05)
    midterm = st.slider("期中考试分数", 0.0, 100.0, 40.0, 1.0)
    homework = st.slider("作业完成率", 0.0, 1.0, 0.7, 0.05)
    submit = st.form_submit_button("预测期末成绩")

# 预测逻辑
if submit:
    # 这里使用和生成模拟数据时相同的线性模型（实际可替换为机器学习模型）
    final_score = 0.2 * study_hours + 10 * attendance + 0.5 * midterm + 5 * homework + np.random.normal(0, 5)
    final_score = max(0, min(100, final_score))
    final_score = round(final_score, 1)
    
    # 显示预测结果
    st.markdown("### 预测结果")
    if final_score >= 60:
        st.success(f"预测期末成绩: {final_score} 分")
        st.image("https://images.unsplash.com/photo-1514446424907-8b0edd78d937?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fDE2OTk3OTg1NTR8&auto=format&fit=crop&w=1770&q=80", 
                 caption="恭喜你，及格啦！", use_column_width=True)
        st.markdown("**学习建议：** 继续保持当前学习状态，考前可针对性复习薄弱知识点，争取更好成绩！")
    else:
        st.error(f"预测期末成绩: {final_score} 分")
        st.image("https://images.unsplash.com/photo-1586281380117-5a60ae2050cc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fDE2OTk3OTg1ODZ8&auto=format&fit=crop&w=1770&q=80", 
                 caption="很遗憾，未及格。", use_column_width=True)
        st.markdown("**学习建议：** 需大幅增加学习时长，重点攻克期中考试薄弱章节，提高作业完成质量，考前进行全面复习！")
