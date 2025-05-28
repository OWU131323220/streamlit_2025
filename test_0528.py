import streamlit as st

st.title("第7回 Streamlit フォーム演習")
st.caption("st.form を使ってサークル入会申し込みフォームを作成しましょう。")

st.markdown("---")
st.subheader("演習: サークル入会申し込みフォーム")
st.write("**課題**: フォームを使って、サークル入会の申し込み情報をまとめて処理するアプリを作成する。")

# st.form ブロックを開始
with st.form(key="circle_application_form"):
    st.subheader("🌸 サークル入会申し込み")
    
    # 基本情報の入力欄
    name = st.text_input("お名前:", value="大妻 花子", key="form_name")
    
    grade_options = ["", "1年生", "2年生", "3年生", "4年生"]
    grade = st.selectbox("学年:", options=grade_options, index=2, key="form_grade")
    
    activity_options = ["", "文化祭", "合宿", "勉強会", "交流会", "ボランティア", "その他"]
    favorite_activity = st.selectbox("好きな活動:", options=activity_options, index=1, key="form_activity")
    
    motivation = st.text_area("意気込み:", 
                             value="新しい友達を作りながら、楽しく活動に参加したいです！", 
                             key="form_motivation")
