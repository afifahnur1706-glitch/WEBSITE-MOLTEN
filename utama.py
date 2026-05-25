import streamlit as st
import pandas as pd
import os
import urllib.parse

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Molten Basketball Store 🏀",
    page_icon="🏀",
    layout="wide"
)

# ==========================
# STYLE WEBSITE
# ==========================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background: linear-gradient(
        135deg,
        #111111,
        #1e1e1e,
        #2d2d2d
    );
}

[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

h1{
    text-align:center;
    color:#ff7a00;
    font-size:55px;
    font-weight:bold;
}

div[data-testid="column"]{
    background:#ffffff;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 6px 15px rgba(0,0,0,0.25);
    margin-bottom:20px;
}

.stButton > button{
    width:100%;
    background:#ff7a00;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-weight:bold;
    font-size:16px;
}

.stButton > button:hover{
    background:#ff5500;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# TITLE
# ==========================
st.title("🏀 Molten Basketball Store")
st.caption("Official Basketball • Premium Quality • Ready Stock 🔥")

st.divider()

# ==========================
# LOAD CSV
# ==========================
csv_file = "data_molten.csv"

if not os.path.exists(csv_file):
    st.error("File data_molten.csv tidak ditemukan!")
    st.stop()

df = pd.read_csv(csv_file)

# ==========================
# VALIDASI KOLOM
# ==========================
required_columns = [
    "nama",
    "harga",
    "ukuran",
    "jenis",
    "gambar"
]

for col in required_columns:
    if col not in df.columns:
        st.error(f"Kolom '{col}' tidak ditemukan!")
        st.stop()

# ==========================
# FILTER UKURAN
# ==========================
ukuran_list = ["Semua"] + list(df["ukuran"].unique())

selected_size = st.selectbox(
    "🏀 Pilih Ukuran Basketball",
    ukuran_list
)

if selected_size != "Semua":
    df = df[df["ukuran"] == selected_size]

st.divider()

# ==========================
# TAMPILKAN PRODUK
# ==========================
cols = st.columns(2)

for index, row in df.reset_index(drop=True).iterrows():

    with cols[index % 2]:

        # GAMBAR
        if os.path.exists(row["gambar"]):
            st.image(
                row["gambar"],
                use_container_width=True
            )
        else:
            st.warning("Gambar tidak ditemukan")

        # NAMA
        st.subheader(row["nama"])

        # HARGA
        harga = f"Rp {row['harga']:,}".replace(",", ".")

        st.markdown(f"## 💸 {harga}")

        # DETAIL
        st.info(f"""
🏀 Ukuran : {row['ukuran']}

🔥 Jenis : {row['jenis']}
""")

        # BUTTON ORDER
        if st.button(
            f"🛒 Order {row['nama']}",
            key=f"order_{index}"
        ):

            st.success(
                f"{row['nama']} berhasil ditambahkan!"
            )

st.divider()

# ==========================
# FOOTER
# ==========================
st.subheader("📞 Hubungi Kami")

col1, col2 = st.columns(2)

with col1:

    st.info("""
🏪 **Molten Basketball Store**

📍 Yogyakarta, Indonesia
""")

with col2:

    nomor = "6281234567890"

    pesan = urllib.parse.quote(
        "Halo admin, saya ingin membeli basketball Molten 🏀"
    )

    wa_link = f"https://wa.me/{nomor}?text={pesan}"

    st.link_button(
        "📱 Pesan via WhatsApp",
        wa_link
    )

st.divider()

st.caption(
    "©️ 2026 Molten Basketball Store — Play Like A Pro 🏀"
)
