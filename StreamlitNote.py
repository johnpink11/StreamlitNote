import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime

st.header('John的Streamlit笔记', divider='rainbow')


st.header("st.write")

st.markdown("`st.write`可以在Streamlit应用中输出内容")
st.markdown("`st.write`可以输出的内容包括:")
st.markdown("""- 字符串\n - Python的`dict`对象\n - 输出`pandas`的DataFrame, 将数据显示为表格\n 
- 输出各种绘图库`matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh`等库所作的图表""")

st.subheader('展示文本')
code = '''st.markdown("Hello, World!😎")'''
st.code(code, language="python")

st.markdown("Hello, World!😎")

st.subheader('展示DataFrame')
code = '''df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)'''
st.code(code, language="python")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.subheader('展示图像')
st.markdown("下面我们在画布上随机位置画出随机大小的200个圆圈")

code = '''df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

circles = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(circles)'''

st.code(code, language='python')
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)


@st.cache_data
def generate_circles():
    circles = alt.Chart(df2).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )
    return circles


circles = generate_circles()
st.write(circles)

st.header("Some Widgets")
st.subheader("Slider")

st.code('''age = st.slider('How old are u?', 0, 120, 25)
st.write("After 10 years, you'll be {0} years old.".format(age + 10))''')
age = st.slider('How old are u?', 0, 120, 25)
st.write("After 10 years, you'll be {0} years old.".format(age + 10))

st.write("这里的参数第一个为提示语，后面的参数为`(minimum, maximum, default)`")

st.subheader('Range slider')


st.code('''values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)''')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.write("Range slider与Slider的差别在于其`default`取值为一个二元`tuple`, 第一个值代表Range的`leftside`, 第二个值代表`rightside`")

st.subheader('创建时间范围(Time range)')
st.code('''appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45))
)

st.write("You're scheduled for :", appointment[0], '-', appointment[1])
''')


appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45))
)

st.write("You're scheduled for :", appointment[0], '-', appointment[1])

st.write("将`value`设置为一个开始时间到结束时间的元祖`(start time, end time)`, 就可以设置为一个time slider.")


st.subheader('Datetime slider')

st.code('''start_time = st.slider(
     "When do you start?",
     min_value=datetime(2020, 1, 1, 9, 30),
     max_value=datetime(2050, 12, 31, 23, 59),
     value=datetime(2020, 1, 1, 9, 30),
     format="YY/MM/DD - hh:mm")
st.write("Start time:", start_time)
''')

start_time = st.slider(
     "When do you start?",
     min_value=datetime(2020, 1, 1, 9, 30),
     max_value=datetime(2050, 12, 31, 23, 59),
     value=datetime(2020, 1, 1, 9, 30),
     format="YY/MM/DD - hh:mm")
st.write("Start time:", start_time)

st.write('时间滑条与普通的滑条基本相同，只不过参数类型换为了`datetime`.')