# Karınca Kolonisi Algoritması ile Yol Optimizasyonu
## Senaryo 5: Ankara Göletleri Su Numunesi Toplama

Bu proje, Ankara'daki 10 farklı göletten su numunesi toplayacak olan Çevre Bakanlığı birimleri için en kısa rotayı Karınca Kolonisi Algoritması (ACO) kullanarak hesaplar.

### Özellikler
- **Google Maps API:** Gerçek sürüş mesafeleri kullanılarak mesafe matrisi oluşturulmuştur.
- **ACO Algoritması:** Karınca sayısı, iterasyon, alpha ve beta gibi parametreler optimize edilebilir.
- **Streamlit Arayüzü:** Rota harita üzerinde görselleştirilir ve mesafe değişim grafiği sunulur.

### Kurulum
1. Gerekli kütüphaneleri kurun: `pip install -r requirements.txt`
2. `.streamlit/secrets.toml` dosyasına kendi Google Maps API anahtarınızı ekleyin.
3. Uygulamayı çalıştırın: `streamlit run app.py`
