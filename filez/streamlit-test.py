import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit 示例应用')
st.write('这是一个使用Streamlit构建的简单数据可视化应用。')
st.header('1. 滑块输入')
age = st.slider('请选择您的年龄', 0, 100, 25)
st.write(f'您选择的年龄是: {age}')
st.header('2. 文本输入')
name = st.text_input('请输入您的姓名', '张三')
st.write(f'您好, {name}!')

st.header('3. 图表展示')
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=['A', 'B', 'C'])
st.line_chart(chart_data)

st.header('4. 地图展示')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

st.header('5. 多选框')
if st.checkbox('显示数据'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['A', 'B', 'C'])

    chart_data


# 在侧框中添加内容
st.sidebar.title("侧框")
st.sidebar.header("这是一个侧框")

# 添加侧框中的选项
option = st.sidebar.selectbox(
    "你选择哪个选项？",
    ("选项 1", "选项 2", "选项 3")
)

# 根据选择的选项显示内容
st.header('6. 进度条')
import time

'开始加载...'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  latest_iteration.text(f'加载进度 {i+1}%')
  bar.progress(i+1)
  time.sleep(0.1)

'加载完成!'