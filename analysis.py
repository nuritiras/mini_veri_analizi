import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Proje klasörleri
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "movies.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Grafik görünümü
sns.set_theme(style="whitegrid")

# 1. Veriyi oku ve tanı
df = pd.read_csv(DATA_PATH)

print("\n=== İLK 5 KAYIT ===")
print(df.head())

print("\n=== VERİ SETİ BOYUTU ===")
print(f"Satır: {df.shape[0]}, Sütun: {df.shape[1]}")

print("\n=== VERİ TİPLERİ ===")
print(df.dtypes)

print("\n=== EKSİK DEĞERLER (TEMİZLEME ÖNCESİ) ===")
print(df.isna().sum())

print("\n=== TEKRAR EDEN SATIR SAYISI ===")
print(df.duplicated().sum())

# 2. Veri temizleme
df = df.drop_duplicates().copy()

# Sayısal olması gereken alanları dönüştür.
numeric_columns = ["year", "rating", "votes", "duration"]
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Analiz için gerekli alanları eksik olan satırları kaldır.
# Diğer eksik sayısal değerleri medyan ile doldur.
df = df.dropna(subset=["title", "genre", "rating"]).copy()

for column in ["year", "votes", "duration"]:
    df[column] = df[column].fillna(df[column].median())

df["year"] = df["year"].round().astype(int)
df["votes"] = df["votes"].round().astype(int)
df["duration"] = df["duration"].round().astype(int)

print("\n=== TEMİZLEME SONRASI ===")
print(f"Kalan kayıt sayısı: {len(df)}")
print(df.isna().sum())

# Temizlenmiş veri setini kaydet.
df.to_csv(OUTPUT_DIR / "movies_cleaned.csv", index=False, encoding="utf-8-sig")

# 3. Tanımlayıcı istatistikler
print("\n=== PUAN İSTATİSTİKLERİ ===")
print(df["rating"].describe())

print("\nOrtalama puan:", round(df["rating"].mean(), 2))
print("Medyan puan:", round(df["rating"].median(), 2))
print("Standart sapma:", round(df["rating"].std(), 2))

print("\n=== TÜR SAYILARI ===")
print(df["genre"].value_counts())

genre_rating = (
    df.groupby("genre")["rating"]
      .mean()
      .sort_values(ascending=False)
)
print("\n=== TÜRLERE GÖRE ORTALAMA PUAN ===")
print(genre_rating.round(2))

# 4. Görselleştirme - Bar chart
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="genre", order=df["genre"].value_counts().index)
plt.title("Film Türlerinin Dağılımı")
plt.xlabel("Film Türü")
plt.ylabel("Film Sayısı")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "genre_counts.png", dpi=150)
plt.close()

# 5. Görselleştirme - Histogram
plt.figure(figsize=(9, 5))
sns.histplot(data=df, x="rating", bins=10, kde=True)
plt.title("Film Puanlarının Dağılımı")
plt.xlabel("Film Puanı")
plt.ylabel("Film Sayısı")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "rating_distribution.png", dpi=150)
plt.close()

# 6. Görselleştirme - Scatter plot
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="duration", y="rating", hue="genre", alpha=0.8)
plt.title("Film Süresi ve Puan İlişkisi")
plt.xlabel("Film Süresi (dakika)")
plt.ylabel("Film Puanı")
plt.legend(title="Tür", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "duration_rating.png", dpi=150)
plt.close()

# 7. Ek analiz: En yüksek puanlı 10 film
top_movies = df.nlargest(10, "rating")[["title", "genre", "year", "rating", "votes"]]
print("\n=== EN YÜKSEK PUANLI 10 FİLM ===")
print(top_movies.to_string(index=False))

print("\nAnaliz tamamlandı. Grafikler output/ klasörüne kaydedildi.")
