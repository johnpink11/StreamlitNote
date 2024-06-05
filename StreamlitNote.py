import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime
st.title('John的Streamlit笔记')


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
st.markdown('---')

st.header("Draw a line chart(画折线图)")

st.code('''chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)''')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

st.markdown('这里传入的参数为`DataFrame`对象，也可以自己指定以下参数:')
st.markdown('- `x`用来指定横坐标的参数 \n - `y`用于指定所要画出的那些数据 \n - `color`指定每组数据的颜色')
st.markdown("**Example:**")
st.code('''chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['col1', 'col2', 'col3']
)
st.line_chart(chart_data, x="col1", y=["col2", "col3"], color=["#FFOOOO", "#0000FF"])''')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['col1', 'col2', 'col3']
)

st.line_chart(
              chart_data, 
              x="col1", y=["col2", "col3"],
              color=["#FFOOOO", "#0000FF"]
)

st.header("Checkboxes")

st.code('''if is_checked:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    chart_data
''')

is_checked = st.checkbox('Show dataframe')
if is_checked:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    chart_data

st.markdown('`st.checkbox`是一个选择框, 这个函数会返回一个bool值, 如果被选中返回`true`, 未被选中返回`false`')

st.header("Selectbox")
st.markdown('`selectbox`可以用来提供选择, 同时返回用户的选择')


st.code('''option = st.selectbox("What is your favoriate animal?",
            ('Cat', 'Dog', 'Elephant','Pig'))

st.write('Your favoriate animal is ', option)
''')

option = st.selectbox("What is your favoriate animal?",
            ('Cat', 'Dog', 'Elephant','Pig'))

st.write('Your favoriate animal is ', option)


st.header('Multiselect(多选框)')
st.markdown('`st.multiselect`允许用户选择多个选项, 返回一个可迭代对象, 内容为用户选择的选项')

st.code('''options = st.multiselect(
     'What are your favorite colors',
     ['Cat', 'Dog', 'Elephant','Pig'],
     ['Cat', 'Dog'])


st.markdown("**Your favorite animal list:**")
for option in options:
    st.markdown(f"- {option}")''')

options = st.multiselect(
     'What are your favorite colors',
     ['Cat', 'Dog', 'Elephant','Pig'],
     ['Cat', 'Dog'])


st.markdown("**Your favorite animal list:**")
for option in options:
    st.markdown(f"- {option}")

st.header("Layout(布局)")

st.header("SideBar")
st.markdown("`st.sidebar`可以创建一个侧边栏, 而侧边栏添加内容需要对`st.sidebar`调用方法")
st.markdown("例如想要在侧边栏添加一个`selectbox`，则需要调用`st.sidebar.selectbox`")

st.code('''add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
''')

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.subheader("Column")
st.markdown('`st.column`可以将App的布局进行分栏, 从而可以利用其对App布局')

st.code('''left_column, right_column = st.columns(2)

left_column.button('Press me!')
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")''')

left_column, right_column = st.columns(2)

left_column.button('Press me!')
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")

st.subheader("expander(创建可折叠块)")

st.code('''with st.expander("What is a prime number?"):
    st.markdown("Prime number is an integer which only has 1 and itself as its factors.")
''')

with st.expander("What is a prime number?"):
    st.markdown("Prime number is an integer which only has 1 and itself as its factors.")

st.markdown("> *种一棵树最好的时间是十年前，其次是现在。*")
st.markdown('---')

st.header("Show progress(为过程展示进度条)")

st.markdown("`st.progress`可以创建一个进度条，其用法如下")
st.code('''import time
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f"{i + 1}%") 
  bar.progress(i + 1)
  time.sleep(0.1)
''')

# import time 
# # # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f"{i + 1}%") 
#   bar.progress(i + 1)
#   time.sleep(0.1)


st.header("`st.latex`(书写数学公式)")
st.latex(r'''
a^2 + b^2 = c^2
''')
st.markdown("`st.latex`与`st.code`用法完全相同，只不过传入的字符串要是LaTeX的格式")


st.header("Caching(缓存数据)")
st.markdown("对于一个读取数据或者生成数据的过程，如果每次streamlit页面刷新都要重新加载一边,则会严重影响加载速率，利用`cache`对函数进行缓存，保存函数运行结果")
st.markdown("Example:")
st.code('''@st.cache_data
def long_running_function(param1, param2):
    return ...
''')
st.markdown('当一个函数被修饰为`st.cache_data`时，Streamlit会记录这个函数的以下内容\n')
st.markdown('- 函数名`long_running_function\n - 输入参数(`param1`, `param2`) \n - 函数体内的代码')

st.markdown("当Streamlit运行这个`long_running_function`函数时, Streamlit并不是直接执行函数体中的代码，而是检查此输入参数下该函数的数据有没有被缓存，如果已经缓存过，则直接返回已有的数据")

st.markdown("**Example:**")
st.code('''@st.cache_data
def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df



df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")''')

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df



df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

st.markdown("试试点击Rerun, 页面会很快的重新加载，上面代码从一个url读取大量数据，如果不使用`st.cache_data`缓存数据，则每次页面刷新都要重新读取")
