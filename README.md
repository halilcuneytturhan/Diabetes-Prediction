

# 🤖 Diyabet Risk Tahmin Uygulaması (Machine Learning)
Bu proje, gerçek hasta verileriyle eğitilmiş bir Random Forest (Rastgele Orman) modelini kullanarak, kullanıcıdan aldığı sağlık değerlerine göre diyabet riski tahmini yapan bir masaüstü uygulamasıdır .Hem veri bilimini hem de kullanıcı dostu bir arayüzü tek bir .exe dosyasında birleştirir.

🚀 Öne Çıkan Özellikler
- Zeki Tahmin: Scikit-learn kütüphanesi ve 100 karar ağaçlı orman modeli ile yüksek doğruluk oranı.
- Hızlı Açılış (Turbo Mode): Model her seferinde yeniden eğitilmez; joblib ile kaydedilmiş "hazır beyin" (.pkl) üzerinden milisaniyeler içinde açılır.
- Hata Yakalama: Yanlış veri girişi (harf, boş bırakma vb.) durumlarında kullanıcıyı uyaran sinir sistemi (try-except).
- Kullanıcı Dostu Arayüz: Tkinter ile geliştirilmiş, anlaşılır ve sade tasarım.
