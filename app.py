import streamlit as st
import numpy as np
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
from aco_logic import AntColonyOptimizer

st.set_page_config(page_title="Ankara Gölet Optimizasyonu", layout="wide")
st.title("🚜 Ankara Göletleri Yol Optimizasyonu (Senaryo 5)")

# Parametreler
st.sidebar.header("Algoritma Ayarları")
n_ants = st.sidebar.slider("Karınca Sayısı", 10, 50, 20)
n_iter = st.sidebar.slider("İterasyon Sayısı", 10, 200, 100)
alpha = st.sidebar.slider("Alpha", 0.1, 5.0, 1.0)
beta = st.sidebar.slider("Beta", 0.1, 5.0, 2.0)
rho = st.sidebar.slider("Buharlaşma", 0.1, 0.9, 0.5)

# Veriler
ponds_data = {
    "Mavi Göl": [39.9042, 32.9967], "Mogan Gölü": [39.7744, 32.7889],
    "Eymir Gölü": [39.8247, 32.8336], "Karagöl": [40.4036, 32.9189],
    "Çamlıdere Barajı": [40.4286, 32.4839], "Kurtboğazı Barajı": [40.2975, 32.6953],
    "Kesikköprü Barajı": [39.3850, 33.6820], "Dikilitaş Göleti": [39.5447, 32.6517],
    "Sorgun Göleti": [40.3958, 32.2597], "Kızılca Göleti": [40.1283, 33.0233]
}
pond_names = list(ponds_data.keys())

# Matrisi Yükle
try:
    dist_matrix = np.load('data/ankara_dist_matrix.npy')
except:
    st.error("HATA: data/ankara_dist_matrix.npy bulunamadı!")
    st.stop()

if st.button("Optimizasyonu Başlat"):
    aco = AntColonyOptimizer(dist_matrix, n_ants, n_iter, alpha, beta, rho)
    best_path, best_dist, history = aco.run()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 En Kısa Rota")
        m = folium.Map(location=[39.9, 32.8], zoom_start=8)
        for name, coord in ponds_data.items():
            folium.Marker(coord, popup=name).add_to(m)
        path_coords = [ponds_data[pond_names[i]] for i in best_path]
        folium.PolyLine(path_coords, color="red", weight=3).add_to(m)
        st_folium(m, width=500)

    with col2:
        st.subheader("📈 Mesafe Grafiği")
        fig, ax = plt.subplots()
        ax.plot(history)
        st.pyplot(fig)

    st.success(f"En kısa mesafe: {best_dist:.2f} km")