import streamlit as st

st.set_page_config(page_title="Vanzo AI Clone - Tool Auto Video", layout="wide")

st.title("🎬 Vanzo AI - Hệ Thống Tạo Video Tự Động")
st.write("Công cụ hỗ trợ làm video kịch bản, mẹ chồng con dâu, thời trang và review sản phẩm tự động.")

# Cột điều khiển bên trái
st.sidebar.header("⚙️ Tùy chọn Kịch Bản")
api_key = st.sidebar.text_input("Nhập API Key (OpenAI / AI)", type="password")
style = st.sidebar.selectbox("Chọn phong cách video", [
    "Mẹ chồng con dâu", 
    "Thời trang trước gương", 
    "Drama đạo lý", 
    "Review sản phẩm đa ngành"
])
character = st.sidebar.selectbox("Chọn nhân vật chính", ["Nữ chính truyền thống", "Mẹ chồng khó tính", "Cô gái hiện đại"])

st.sidebar.divider()
if st.sidebar.button("✨ Tự động sinh kịch bản AI", type="primary"):
    st.sidebar.success("Đã tạo kịch bản và phân cảnh thành công!")

# Khu vực hiển thị phân cảnh ở giữa
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Phân cảnh 1: Mở đầu")
    st.text_area("Lời thoại nhân vật:", "Canh gì mà mặn chát thế này hả con?", key="d1")
    st.text_area("Mô tả hình ảnh (Prompt AI):", "Vietnamese mother and daughter in law in rural kitchen, cinematic lighting, realistic", key="p1")
    st.button("🖼️ Tạo lại hình ảnh Cảnh 1")

with col2:
    st.subheader("📌 Phân cảnh 2: Diễn biến cao trào")
    st.text_area("Lời thoại nhân vật:", "Con nấu đúng công thức mẹ dặn mà mẹ...", key="d2")
    st.text_area("Mô tả hình ảnh (Prompt AI):", "Young Vietnamese woman looking surprised in kitchen, emotional expression", key="p2")
    st.button("🖼️ Tạo lại hình ảnh Cảnh 2")

st.divider()
st.subheader("🎞️ Timeline & Xuất Bản Video")
music_opt = st.select_slider("Chọn nhạc nền cảm xúc:", ["Nhạc nhẹ nhàng", "Nhạc drama kịch tính", "Nhạc vui tươi"])
if st.button("🚀 Render & Xuất Video Hoàn Chỉnh (MP4)", type="primary"):
    st.balloons()
    st.success("Đã hoàn tất quá trình ghép nối video! Sư huynh có thể tải xuống máy.")
