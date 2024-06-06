import streamlit as st
import numpy as np
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

st.title("Build a LLM chat app")
st.markdown("这个示例构建一个简单的在线大语言模型，使其能够在线与用户交互")
st.markdown("下面将介绍一些可能会用到的Streamlit组件")
st.header("Chat elements")

st.subheader("Chat message")
st.markdown("生成message")
with st.echo():
    with st.chat_message("user"):
        st.write("Hello 👋")
        st.line_chart(np.random.randn(30, 3))

st.markdown("`st.chart_message()`可以生成一个信息, 参数指定发出信息的主体")


st.subheader("Chat input")
st.markdown("创建输入组件")

with st.echo():
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"The user has sent: {prompt}")


# st.subheader("Status container")

# 判断number是否为素数
import math

def isPrime(number):
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
# 生成number个素数
@st.cache_data
def generatePrime(number):
    primes = []
    i = 2
    while len(primes) < number:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes

with st.echo():
    with st.status('Generating data...'):
        st.write("Running function...")
        primes = generatePrime(100000)
        df = pd.DataFrame(primes, columns=['Primes'])
        st.write(df)



st.header("Let's begin")

with st.echo():
    with st.chat_message("user"):
        st.write("Helllo 👋")

st.subheader("Create a echo bot first.")
st.markdown("The bot will repeat whatever you say.")

st.title("Echo Bot")
st.markdown("以下代码可以创建一个重复输入的机器人，可以尝试说一段话，机器人会重复您输入的内容")

with st.echo():
    if "message" not in st.session_state:
        st.session_state.message = []

    for message in st.session_state.message:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    # 读取用户的输入
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.message.append({"role": "user", "content": prompt})

        # add response of bot
        response = f"Echo: {prompt}"
        with st.chat_message("ai"):
            st.markdown(response)
        st.session_state.message.append({
            "role": "ai",
            "content": response
        })

st.header("利用OpenAI的API创造chatBot")
st.markdown("利用以上所学习的，以及OpenAI的API创建了一个类似chatGPT的Bot")

if st.button("查看示例"):
    switch_page("chat")