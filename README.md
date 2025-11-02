# Car Evaluation Decision Tree Model

Makine Öğrenmesi ve Karar Destek Sistemleri Uygulaması<br><br>
Bu proje, **UCI Machine Learning Repository**'den alınan *Car Evaluation* veri seti kullanılarak geliştirilmiş bir **Karar ağacı (Decision Tree)** modelini içermektedir.  
Amaç, otomobillerin çeşitli özelliklerine (örneğin fiyat, bakım maliyeti, kapı sayısı, koltuk sayısı vb.) göre **kabul edilebilirlik sınıfını (unacc, acc, good, vgood)** tahmin etmektir.
Sonuçta yüksek doğruluk oranı (%94 civarı) elde edilmiştir.
En önemli belirleyici özellik “safety (güvenlik)” olarak bulunmuştur.

---

# Proje İçeriği

| Dosya Adı | Açıklama |
|------------|-----------|
| `car.data` | UCI veri seti (ham veriler) |
| `car.names` | Veri setine ait attribute açıklamaları |
| `car.c45-names` | Alternatif isimlendirme dosyası (C4.5 formatında) |
| `car_evaluation.py` | Modelin oluşturulduğu Python betiği |
| `car_tree.dot` | Karar ağacının Graphviz biçiminde görsel temsili |
| `.gitignore` | Gereksiz dosyaları git sürümüne dahil etmemek için oluşturulmuştur |

---

# Kullanılan Teknolojiler

- **Python**
- **Scikit-learn** → Karar ağacı sınıflandırıcısı (DecisionTreeClassifier)
- **Pandas** → Veri yükleme ve işleme
- **Graphviz** → Karar ağacını `.dot` dosyası olarak dışa aktarma
- **Spyder IDE / Jupyter Notebook** (geliştirme ortamı)

---

# Modelin Başarımı

Model, veri seti eğitim ve test olarak bölündükten sonra aşağıdaki metriklerle değerlendirilmiştir:

- **Accuracy (Doğruluk):** Modelin genel başarı oranı  
- **Precision / Recall / F1-Score:** Her sınıfın tahmin performansını ölçmek için kullanılan metrikler  

> Not: Değerler `car_evaluation.py` dosyasını çalıştırdığınızda konsol çıktısında görünmektedir.

---

# Modelin İşlevi

Model, karar ağacı algoritmasıyla **veri setindeki kuralları öğrenir** ve bu kurallar doğrultusunda yeni bir aracın hangi kategoride olduğunu tahmin eder.  
Örneğin:
- *low price, high maintenance, 2 doors, 4 seats → unacceptable (unacc)*  
- *med price, low maintenance, 4 doors, 5 seats → acceptable (acc)*  

---

# Nasıl Çalıştırılır

1. Python 3 ve gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas scikit-learn graphviz
   
2. Dosyanın bulunduğu klasöre gidin:
 ```
cd ~/Desktop/car+evaluation

```
4. Script’i çalıştırın:
```
python car_evaluation.py
```

5. **Karar Ağacı Modelini Görüntülemek için:**<br>
`car_tree.dot` dosya içeriğini kopyalayıp https://edotor.net sitesine yapıştırarak anlık olarak görübtüleyebilirsiniz.


# Kaynak
UCI Machine Learning Repository<br>
Car Evaluation Data Set<br>
https://archive.ics.uci.edu/ml/datasets/car+evaluation

# Geliştirici
**Hatice Polat**  
🎓 Akdeniz Üniversitesi — Yönetim Bilişim Sistemleri  
📎 [LinkedIn](https://linkedin.com/in/haticepolatt)
