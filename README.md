# Mini Veri Analizi Projesi: Film Verileri

Bu proje, **BİL 242 – Veri Analizi ve Görselleştirme** dersi kapsamında hazırlanmış eğitim amaçlı bir mini projedir. Katılımcılar bir CSV veri seti üzerinde veri tanıma, temizleme, temel istatistiksel analiz ve görselleştirme adımlarını uygular.

> **Not:** `data/movies.csv` dosyası eğitim amacıyla oluşturulmuş sentetik bir veri setidir. Gerçek film istatistiklerini temsil etmez.

## Projenin amaçları

- CSV dosyasını Pandas ile okumak ve incelemek
- Eksik değerleri ve tekrar eden kayıtları tespit etmek
- Sayısal veri tiplerini dönüştürmek
- Ortalama, medyan ve standart sapma gibi ölçüleri hesaplamak
- Seaborn ve Matplotlib ile grafikler oluşturmak
- Bulguları yorumlamak ve kısa rapor hazırlamak

## Kullanılan teknolojiler

- Python 3
- Pandas
- Matplotlib
- Seaborn

## Klasör yapısı

```text
mini_veri_analizi/
├── data/
│   └── movies.csv
├── output/
│   └── (program çalışınca grafikler ve temizlenmiş veri oluşur)
├── analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Kurulum

Öncelikle proje klasörüne girin:

```bash
cd mini_veri_analizi
```

Sanal ortam oluşturmak (önerilir):

```bash
python3 -m venv .venv
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\\Scripts\\activate
```

Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

## Projeyi çalıştırma

```bash
python analysis.py
```

Program; veri setini inceler, temizleme işlemlerini yapar, temel istatistikleri ekrana yazdırır ve aşağıdaki çıktıları `output/` klasörüne kaydeder:

- `movies_cleaned.csv`
- `genre_counts.png`
- `rating_distribution.png`
- `duration_rating.png`

## Öğrenci görevleri

1. Veri setinin satır ve sütun sayısını bulun.
2. Eksik değerleri ve tekrar eden kayıtları tespit edin.
3. Temizleme öncesi ve sonrası kayıt sayılarını karşılaştırın.
4. Film puanlarının ortalamasını, medyanını ve standart sapmasını hesaplayın.
5. Film türlerinin dağılımını inceleyin.
6. En az üç grafik oluşturun.
7. En az üç araştırma sorusu belirleyip cevaplayın.
8. Bulgularınızı 1–2 sayfalık kısa bir raporla açıklayın.

## Örnek araştırma soruları

- Veri setinde en fazla hangi film türü bulunmaktadır?
- Hangi türün ortalama puanı daha yüksektir?
- Film süresi ile puan arasında belirgin bir ilişki var mıdır?
- En yüksek puanlı filmler aynı zamanda en çok oy alan filmler midir?

## Rapor önerisi

Raporunuzda şu başlıkları kullanabilirsiniz:

1. Projenin amacı
2. Veri setinin tanıtımı
3. Veri temizleme işlemleri
4. Temel istatistikler
5. Grafikler
6. Bulguların yorumlanması
7. Sonuç

## Lisans ve kullanım

Bu materyal eğitim ve öğrenme amacıyla hazırlanmıştır. Veri seti sentetiktir; gerçek kişi veya gerçek film değerlendirmeleri içerdiği iddia edilmez.
