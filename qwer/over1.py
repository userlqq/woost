import streamlit as st
import pandas as pd
import plotly.express as px

st.title("专业数据分析")
st.markdown('***')
df=pd.read_csv("student_data_adjusted_rounded.csv",encoding="utf-8")
st.set_page_config(layout='wide')

a1,a2=st.columns([1,2])
with a1:
#按专业分组计算平均分
    grouped_df=df.groupby("专业").agg(
        每周平均学习时长=("每周学习时长（小时）","mean"),
        期中考试平均分=("期中考试分数","mean"),
        期末考试平均分=("期末考试分数","mean")
        ).reset_index()
    st.title('各专业学习数据统计')
    st.dataframe(grouped_df,use_container_width=True)

with a2:
    st.bar_chart(grouped_df.set_index("专业"))
st.markdown('***')

w1,w2=st.columns([1,2])
with w1:
# 统计各专业男女数量
    gender_count = df.groupby(["专业", "性别"]).size().unstack(fill_value=0)
    # 计算总人数和占比
    gender_count["总人数"] = gender_count.sum(axis=1)
    gender_count["男生占比"] = (gender_count["男"] / gender_count["总人数"]).round(3) * 100
    gender_count["女生占比"] = (gender_count["女"] / gender_count["总人数"]).round(3) * 100
    # 重置索引并整理列
    gender_ratio = gender_count[["男生占比", "女生占比"]].reset_index().rename(columns={"专业": "major"})

    st.title("性别比例数据")
    # 表格展示
    st.dataframe(gender_ratio, use_container_width=True)

with w2:
# 可视化（更贴近参考样式的柱状图）
    fig = px.bar(
        gender_ratio,
        x="major",
        y=["男生占比", "女生占比"],
        labels={"value": "占比(%)", "variable": "性别", "major": "专业"},
        title="各专业性别占比分布",
        barmode="group",
        text_auto=True
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown('***')

q1,q2=st.columns([1,2])
with q1:
    grouped_df=df.groupby("专业").agg(
        平均出勤率=("上课出勤率","mean"),
        ).reset_index()
    st.title('课程出勤率排名')
    st.dataframe(grouped_df,use_container_width=True)
with q2:
    st.bar_chart(grouped_df.set_index("专业"))

st.markdown('***')

c1,c2=st.columns([1,2])
with c1:
    # 读取数据（替换为实际路径）
    df = pd.read_csv("student_data_adjusted_rounded.csv")
    # 筛选大数据管理专业数据
    bigdata_df = df[df["专业"] == "大数据管理"]

    # 展示关键指标
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("平均出勤率", f"{bigdata_df['上课出勤率'].mean()*100:.1f}%")
    col2.metric("平均期末成绩", f"{bigdata_df['期末考试分数'].mean():.1f}分")
    col3.metric("及格率", f"{(bigdata_df['期末考试分数']>=60).mean()*100:.1f}%")
    col4.metric("平均学习时间", f"{bigdata_df['每周学习时长（小时）'].mean():.1f}小时")

    # 期末成绩分布直方图
    fig_hist = px.histogram(bigdata_df, x="期末考试分数", nbins=5,title="大数据管理专业期末成绩分布")
    st.plotly_chart(fig_hist, use_container_width=True)

with c2:
    # 期末成绩箱线图
    fig_box = px.box(bigdata_df, y="期末考试分数", title="大数据管理专业期末成绩箱线图")
    st.plotly_chart(fig_box, use_container_width=True)
