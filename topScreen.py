# CreateData:2023/08/15
# Version:1.0(Phase1)

import streamlit as st
import datetime
import function

d_today = datetime.date.today()

st.title('Python サンプルサイト')
st.text("今日の日付：" + str(d_today))

st.sidebar.title('カテゴリー一覧')

st.sidebar.subheader('【環境準備】')
PythonEnv=st.sidebar.button('Python環境準備')
StreamlitEnv=st.sidebar.button('Streamlit環境準備')

st.sidebar.subheader('【基本】')
Basic_Var=st.sidebar.button('【基本】変数とデータ型')
Basic_IF=st.sidebar.button('【基本】条件分岐（if）')
Basic_Rep=st.sidebar.button('【基本】繰り返し（for,while）')

st.sidebar.subheader('【応用】')

st.sidebar.subheader('【その他】')
PythonErrorList=st.sidebar.button('エラー一覧')
RecoTool=st.sidebar.button('Python学習時おすすめツール')

if PythonEnv:
    function.PythonEnv()

elif StreamlitEnv:
    function.StreamlitEnv()

elif Basic_Var:
    function.Basic_Var()

elif Basic_IF:
    function.Basic_IF()

elif Basic_Rep:
    function.Basic_Rep()

elif RecoTool:
    function.RecoTool()

elif PythonErrorList:
    function.PythonErrorList()

else:
    st.header('概要')
    st.markdown('本サイトではPythonについての説明をメインに行っていきます。  \n'
                '基本から応用、メモ等までを随時更新していく予定です  \n'
                'また、説明ではエディターに「VisualStudioCode」を使用しますが、  \n'
                'プログラム実行可能であれば同じ環境にする必要はありません')