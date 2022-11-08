import streamlit as st
import matplotlib.pyplot as plt

menu = st.sidebar.selectbox('MENU', options = ['라인그래프', '막대그래프', '파이차트'])
if menu == '라인그래프':
    x = ['멜론','유튜브뮤직','지니뮤직','플로', '스포티파이']
    y1 = [751, 443, 375, 254, 35]


    plt.rc('font', family = 'Malgun Gothic')
    plt.title('국내 음악 스트리밍 이용자 수(단위:만명)')
    plt.plot(x, y1, '.-', color = 'blue', label = '이용자 수')
    plt.legend()
    plt.grid(True, linestyle = '--', color = '#BBBBBB')
    plt.ylim(0, 800)
    st.pyplot(plt)

if menu == '막대그래프':
    x = ['멜론', '유튜브뮤직', '지니뮤직', '플로', '스포티파이']
    y = [751, 443, 375, 254, 35]

    plt.bar(x, y, color = 'skyblue', edgecolor = 'black', width = 0.5)
    plt.xlabel('음악 스트리밍 사이트')
    plt.ylabel('이용자 수')

    st.pyplot(plt)

if menu == '파이차트':
    x = ['멜론', '유튜브뮤직', '지니뮤직', '플로', '스포티파이']
    y = [751, 443, 375, 254, 35]
    colorList = ['#F2D7D9', '#D3CEDF', '#9CB4CC', '#748DA6', '#CDF0EA']

    plt.pie(y, labels = x, autopct='%.1f%%', colors = colorList)
    st.pyplot(plt)