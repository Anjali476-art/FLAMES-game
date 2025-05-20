import streamlit as st

st.title("FLAMES")
st.header("Just a Funny Game")
st.image("https://flamesgame.net/wp-content/uploads/2024/09/FLAMES-game-thumbnail.jpg")
st.sidebar.radio("pick your assumed letter in flames",['F','L','A','M','E','S'])
a=list(st.text_input("Enter first name 💖💖💖 ").lower())
b=list(st.text_input("Enter second name 💖💖💖").lower())
for i in a.copy():
    if i in b:
        a.remove(i)
        b.remove(i)
n=len(a+b)
print(a,b,n)
s="flames"
while(len(s)!=1):
    i=n%len(s)-1
    if i==-1:
        s=s[:len(s)-1]
    else:
        s=s[i+1:]+s[:i]
d={'f':'Friends','l':'Love','a':'Affection','m':'marriage','e':'enemies','s':'siblings'}

if st.button ("get results🤞🤞🤞"):
    st.success(d[s])
    st.balloons()
st.select_slider('Rate this game',['bad','average','good','very good','excellent'])
print(s)
