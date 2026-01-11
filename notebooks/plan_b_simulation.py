import pandas as pd
import numpy as np
import os
from shapely import wkt

# --- AYARLAR ---
DATA_DIR = "data"
OUTPUT_DIR = "outputs_simulated"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("🚀 PLAN B (Revize): Geometrik Dönüşümlü Simülasyon Başlatılıyor...")

# 1. DOSYALARI YÜKLE
try:
    df_clusters = pd.read_csv(os.path.join(DATA_DIR, "clusters.csv"))
    df_grid = pd.read_csv(os.path.join(DATA_DIR, "grid_locations.csv"))
    df_socio = pd.read_csv(os.path.join(DATA_DIR, "socio_data.csv"))
    print("✅ Metadata dosyaları yüklendi.")
except FileNotFoundError as e:
    print(f"❌ Dosya Eksik: {e}")
    exit()

# ---------------------------------------------------------
# 🛠️ GEOMETRİ DÖNÜŞÜMÜ (POLYGON -> CENTROID)
# ---------------------------------------------------------
print("🌍 Geometri İşleniyor: Polygon -> Point dönüşümü yapılıyor...")

# Fonksiyon: WKT String'i al, Merkez Noktayı (Lat,Lon) virgüllü string olarak döndür
def get_centroid(wkt_string):
    try:
        # String'i geometrik objeye çevir
        poly = wkt.loads(wkt_string)
        # Merkez noktasını al
        pt = poly.centroid
        # Looker Studio formatı: "Latitude,Longitude"
        return f"{pt.y},{pt.x}"
    except:
        return None

# Dönüşümü uygula
if 'geometry' in df_grid.columns:
    df_grid['location_point'] = df_grid['geometry'].apply(get_centroid)
    print("✅ Geometri dönüşümü tamamlandı. Yeni sütun: 'location_point'")
else:
    print("⚠️ UYARI: 'geometry' sütunu bulunamadı!")


# ---------------------------------------------------------
# 🧠 SENARYO 1: SMART FLEX MATEMATİĞİ
# ---------------------------------------------------------
print("🔄 Simülasyon 1: 4GB Paket Analizi...")
# ... (Burası aynı kalıyor, sadece çıktıyı üretiyoruz) ...

hours = list(range(24))
simulation_data = []
avg_monthly_usage_mb = 5760 
daily_usage_mb = avg_monthly_usage_mb / 30

# Cluster Profilleri
profile_business = [0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.4, 0.8, 1.0, 1.0, 1.0, 0.9, 0.8, 0.9, 1.0, 0.9, 0.7, 0.5, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1]
profile_resident = [0.2, 0.1, 0.1, 0.1, 0.1, 0.2, 0.5, 0.7, 0.4, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.5, 0.6, 0.8, 0.9, 1.0, 0.9, 0.7, 0.5, 0.3]
profile_leisure =  [0.6, 0.5, 0.3, 0.1, 0.1, 0.1, 0.2, 0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0, 1.0, 1.0, 0.9, 0.8, 0.7]

for cluster_id, profile in zip([0, 1, 2], [profile_resident, profile_business, profile_leisure]):
    total_weight = sum(profile)
    for h in hours:
        usage_weight = profile[h]
        hourly_mb = (usage_weight / total_weight) * daily_usage_mb
        
        traffic_type = 'Billable (Chargeable)'
        if 1 <= h <= 6: traffic_type = 'Night-Owl (Free Night)'
        elif cluster_id == 1 and 9 <= h <= 18: traffic_type = 'Zone-Zero (Free Office)'
            
        simulation_data.append({
            'Cluster': cluster_id, 'Hour': h, 'Traffic Type': traffic_type, 'Simulated Volume MB': hourly_mb
        })

pd.DataFrame(simulation_data).to_csv(os.path.join(OUTPUT_DIR, '1_smart_flex_simulation.csv'), index=False)
print("💾 1_smart_flex_simulation.csv kaydedildi.")


# ---------------------------------------------------------
# 🗺️ SENARYO 2: VOICE vs DATA HEATMAP (GÜNCELLENDİ)
# ---------------------------------------------------------
print("🔄 Simülasyon 2: Harita Verisi...")

if 'CellID' in df_clusters.columns and 'location_point' in df_grid.columns:
    df_heatmap = df_clusters.copy()
    
    # Grid lokasyonunu (MERKEZ NOKTA) ekle
    df_heatmap = pd.merge(df_heatmap, df_grid[['CellID', 'location_point']], on='CellID', how='left')
    
    # Simülasyon Skorları
    def get_data_score(cluster):
        if cluster == 1: return np.random.randint(80, 100)
        if cluster == 2: return np.random.randint(70, 90)
        return np.random.randint(20, 50)

    def get_voice_score(cluster):
        if cluster == 0: return np.random.randint(60, 90)
        return np.random.randint(40, 70)

    df_heatmap['Data Density Score'] = df_heatmap['Cluster'].apply(get_data_score)
    df_heatmap['Voice Density Score'] = df_heatmap['Cluster'].apply(get_voice_score)
    
    cluster_names = {0: 'Residential', 1: 'Business District', 2: 'Leisure Hub'}
    df_heatmap['District Type'] = df_heatmap['Cluster'].map(cluster_names)

    df_heatmap.to_csv(os.path.join(OUTPUT_DIR, '2_advanced_heatmap.csv'), index=False)
    print("💾 2_advanced_heatmap.csv kaydedildi. (Şimdi Looker Studio'da 'location_point' alanını kullanabilirsin!)")

else:
    print("⚠️ Harita oluşturulamadı: CellID veya location_point eksik.")


# ---------------------------------------------------------
# 📈 SENARYO 3: PER CAPITA
# ---------------------------------------------------------
print("🔄 Simülasyon 3: Per Capita...")

# Sütun isim kontrolü (Senin CSV'ne göre)
# Eğer CSV'de 'POPULATION' yoksa, CSV'deki doğru başlığı buraya yazmalısın.
possible_pop_cols = ['POPULATION', 'population', 'Nüfus'] 
found_pop = next((c for c in possible_pop_cols if c in df_socio.columns), None)

possible_int_cols = ['total_interaction', 'interactions', 'Toplam Etkileşim']
found_int = next((c for c in possible_int_cols if c in df_socio.columns), None)

if found_pop and found_int:
    df_socio['Interactions Per Capita'] = df_socio[found_int] / df_socio[found_pop]
    df_socio = df_socio.replace([np.inf, -np.inf], 0).dropna()
    df_socio = df_socio[df_socio[found_pop] > 1000]
    
    df_socio.to_csv(os.path.join(OUTPUT_DIR, '3_socio_per_capita.csv'), index=False)
    print("💾 3_socio_per_capita.csv kaydedildi.")
else:
    print(f"⚠️ Socio Data Sütun Hatası: '{found_pop}' veya '{found_int}' bulunamadı. CSV başlıklarını kontrol et.")

print("\n🏁 İŞLEM TAMAM! Dosyalar 'outputs_simulated' klasöründe.")