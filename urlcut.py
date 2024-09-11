import streamlit as st
import pyshorteners

# 페이지 제목
st.title("URL 단축기")

# URL 입력받기
url = st.text_input("긴 URL을 입력하세요:")

# URL을 단축할 함수
def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

# URL이 입력되었을 때
if url:
    try:
        short_url = shorten_url(url)
        st.success(f"단축된 URL: {short_url}")
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")
