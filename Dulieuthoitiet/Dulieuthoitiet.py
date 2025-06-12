import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
import os

folder_path = "D:/New folder/Dữ liệu thời tiết đã tổng hợp"
output_folder = os.path.dirname(os.path.abspath(__file__))

all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

df_list = []
for file in all_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    df_list.append(df)
combined_df = pd.concat(df_list, ignore_index=True)
combined_df.to_csv("du_lieu_thoi_tiet_tong_hop.csv", index=False)
print("du_lieu_thoi_tiet_tong_hop.csv")

df = pd.read_csv("D:/New folder/du_lieu_thoi_tiet_tong_hop.csv")
print(df.head())

date_col_candidates = ['Date', 'Ngay', 'Thoi_gian', 'Thang_Nam', 'ThoiGian', 'ngay', 'date']
found_date_col = None
for col in df.columns:
    if col in date_col_candidates:
        found_date_col = col
        break
if not found_date_col:
    raise ValueError("Không tìm thấy cột ngày tháng trong dữ liệu!")
if found_date_col != 'Date':
    df = df.rename(columns={found_date_col: 'Date'})

#XỬ lý dữ liệu
required_cols = ['Date', 'T', 'U', 'R', 'Sh', 'Dia_diem']
df = df.dropna(subset=required_cols)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df = df[(df['T'] > -50) & (df['T'] < 60)]
df = df[(df['U'] >= 0) & (df['U'] <= 100)]
df = df[(df['Sh'] >= 0) & (df['Sh'] < 24)]
df = df[(df['R'] >= 0)]

# Thêm cột tháng-năm 
df['Thang_Nam'] = df['Date'].dt.to_period('M').astype(str)

# Gộp dữ liệu 
temp_monthly = df.groupby(['Dia_diem', 'Thang_Nam'])['T'].mean().reset_index()
humidity_monthly = df.groupby(['Dia_diem', 'Thang_Nam'])['U'].mean().reset_index()
rain_monthly = df.groupby(['Dia_diem', 'Thang_Nam'])['R'].sum().reset_index()
sunhour_pivot = df.pivot_table(index='Dia_diem', columns='Thang_Nam', values='Sh', aggfunc='mean')

fig, axs = plt.subplots(3, 2, figsize=(22, 18))
fig.suptitle('So sánh thời tiết giữa các thành phố', fontsize=20)

# 1. Lineplot: Nhiệt độ trung bình theo tháng
sns.lineplot(data=temp_monthly, x='Thang_Nam', y='T', hue='Dia_diem', marker='o', ax=axs[0, 0])
axs[0, 0].set_title('Nhiệt độ trung bình theo tháng')
axs[0, 0].set_xlabel('Tháng-Năm')
axs[0, 0].set_ylabel('Nhiệt độ (°C)')
axs[0, 0].tick_params(axis='x', rotation=45)

# 2. Lineplot: Độ ẩm trung bình theo tháng
sns.lineplot(data=humidity_monthly, x='Thang_Nam', y='U', hue='Dia_diem', marker='o', ax=axs[0, 1])
axs[0, 1].set_title('Độ ẩm trung bình theo tháng')
axs[0, 1].set_xlabel('Tháng-Năm')
axs[0, 1].set_ylabel('Độ ẩm (%)')
axs[0, 1].tick_params(axis='x', rotation=45)

# 3. Barplot: Tổng lượng mưa từng tháng
sns.barplot(data=rain_monthly, x='Thang_Nam', y='R', hue='Dia_diem', ax=axs[1, 0])
axs[1, 0].set_title('Tổng lượng mưa từng tháng')
axs[1, 0].set_xlabel('Tháng-Năm')
axs[1, 0].set_ylabel('Tổng lượng mưa (mm)')
axs[1, 0].tick_params(axis='x', rotation=45)

# 4. Heatmap: Số giờ nắng trung bình mỗi tháng
sns.heatmap(sunhour_pivot, cmap='YlOrRd', annot=True, fmt=".1f", ax=axs[1, 1])
axs[1, 1].set_title('Số giờ nắng trung bình mỗi tháng')
axs[1, 1].set_xlabel('Tháng-Năm')
axs[1, 1].set_ylabel('Thành phố')

# 5. Boxplot: Phân phối nhiệt độ giữa các thành phố
sns.boxplot(data=df, x='Dia_diem', y='T', ax=axs[2, 0])
axs[2, 0].set_title('Phân phối nhiệt độ giữa các thành phố')
axs[2, 0].set_xlabel('Thành phố')
axs[2, 0].set_ylabel('Nhiệt độ (°C)')

# 6. Scatter plot: Nhiệt độ vs Độ ẩm (gộp vào figure tổng hợp)
sns.scatterplot(data=df, x='T', y='U', hue='Dia_diem', ax=axs[2, 1])
axs[2, 1].set_title('Mối quan hệ giữa Nhiệt độ và Độ ẩm')
axs[2, 1].set_xlabel('Nhiệt độ (°C)')
axs[2, 1].set_ylabel('Độ ẩm (%)')

plt.tight_layout(rect=[0, 0, 1, 0.97])
fig.set_size_inches(26, 20)
fig.savefig(os.path.join(output_folder, "du_lieu_thoi_tiet_tong_hop.png"))
plt.show()

# Trực quan hóa dữ liệu từng thành phố 
cities = df['Dia_diem'].unique()
n_cities = len(cities)
fig_city, axs_city = plt.subplots(4, n_cities, figsize=(6*n_cities, 20))
fig_city.suptitle('Trực quan hóa từng thành phố', fontsize=22)

for idx, city in enumerate(cities):
    city_df = df[df['Dia_diem'] == city]
    city_month = city_df.groupby('Thang_Nam').agg({
        'T': 'mean',
        'U': 'mean',
        'R': 'sum',
        'Sh': 'mean'
    }).reset_index()
    # Nhiệt độ 
    sns.barplot(data=city_month, x='Thang_Nam', y='T', ax=axs_city[0, idx], color='tomato')
    axs_city[0, idx].set_title(f'Nhiệt độ TB - {city}')
    axs_city[0, idx].set_xlabel('Tháng-Năm')
    axs_city[0, idx].set_ylabel('Nhiệt độ (°C)')
    axs_city[0, idx].tick_params(axis='x', rotation=45)
    # Độ ẩm 
    sns.barplot(data=city_month, x='Thang_Nam', y='U', ax=axs_city[1, idx], color='deepskyblue')
    axs_city[1, idx].set_title(f'Độ ẩm TB - {city}')
    axs_city[1, idx].set_xlabel('Tháng-Năm')
    axs_city[1, idx].set_ylabel('Độ ẩm (%)')
    axs_city[1, idx].tick_params(axis='x', rotation=45)
    # Lượng mưa
    sns.barplot(data=city_month, x='Thang_Nam', y='R', ax=axs_city[2, idx], color='skyblue')
    axs_city[2, idx].set_title(f'Lượng mưa tổng - {city}')
    axs_city[2, idx].set_xlabel('Tháng-Năm')
    axs_city[2, idx].set_ylabel('Lượng mưa (mm)')
    axs_city[2, idx].tick_params(axis='x', rotation=45)
    # Số giờ nắng 
    sns.barplot(data=city_month, x='Thang_Nam', y='Sh', ax=axs_city[3, idx], color='orange')
    axs_city[3, idx].set_title(f'Số giờ nắng TB - {city}')
    axs_city[3, idx].set_xlabel('Tháng-Năm')
    axs_city[3, idx].set_ylabel('Số giờ nắng')
    axs_city[3, idx].tick_params(axis='x', rotation=45)

plt.tight_layout(rect=[0, 0, 1, 0.97])
fig_city.savefig(os.path.join(output_folder, "trực quan hóa dữ liệu thời tiết.png"))



