import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os

df = pd.read_excel("D:/New folder/TocDoAnMon_CT3_03Thang.xlsx")
print("Tên cột trong file:", df.columns.tolist())

#xử lý làm sạch dữ liệu 
df.columns = [
    "STT", "Địa điểm", "Tên mẫu", "Ngày đặt mẫu", "Ngày rút mẫu", "Số ngày",
    "Khối lượng ban đầu (g)", "Khối lượng sau lần 1 (g)", "Tốc độ ăn mòn (g/cm2.ngày)",
    "NaN_1", "Ghi chú"
]
df_clean = df.drop(columns=["NaN_1", "Ghi chú"])
df_clean = df_clean.dropna(subset=["Tên mẫu", "Tốc độ ăn mòn (g/cm2.ngày)"])
df_clean["Tốc độ ăn mòn (g/cm2.ngày)"] = pd.to_numeric(df_clean["Tốc độ ăn mòn (g/cm2.ngày)"], errors="coerce")
df_clean = df_clean.dropna(subset=["Tốc độ ăn mòn (g/cm2.ngày)"])

print("Sau khi làm sạch dữ liệu:")
print(df_clean.head())
print("Số dòng dữ liệu còn lại:", len(df_clean))

if df_clean.empty:
    print("Không có dữ liệu sau khi làm sạch. Kiểm tra lại file đầu vào!")
    exit()

order_samples = df_clean.groupby("Tên mẫu")["Tốc độ ăn mòn (g/cm2.ngày)"].mean().sort_values(ascending=False).index


fig, axes = plt.subplots(3, 1, figsize=(13, 18))
fig.suptitle("Dữ liệu tốc độ ăn mòn Tháng 3", fontsize=22, fontweight='bold', y=0.98)
#so sánh tốc độ ăn mòn theo mẫu và địa điểm 
sns.barplot(
    data=df_clean,
    x="Tên mẫu",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    hue="Địa điểm",
    order=order_samples,
    palette="Set2",
    ax=axes[0]
)
axes[0].set_title("Tốc độ ăn mòn theo từng mẫu và địa điểm", fontsize=15, fontweight='bold')
axes[0].set_xlabel("Tên mẫu", fontsize=12)
axes[0].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)", fontsize=12)
axes[0].tick_params(axis='x', rotation=30)
axes[0].legend(title="Địa điểm", fontsize=10)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
for container in axes[0].containers:
    axes[0].bar_label(container, fmt="%.2f", fontsize=8, padding=2)

# So sanhs sự tương quan giữa số ngày và tốc độ ăn mòn 
sns.scatterplot(
    data=df_clean,
    x="Số ngày",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    hue="Địa điểm",
    style="Địa điểm",
    s=90,
    palette="Set2",
    ax=axes[1]
)
axes[1].set_title("Tương quan giữa số ngày và tốc độ ăn mòn", fontsize=15, fontweight='bold')
axes[1].set_xlabel("Số ngày ngâm mẫu", fontsize=12)
axes[1].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)", fontsize=12)
axes[1].grid(True, linestyle='--', alpha=0.7)
axes[1].legend(title="Địa điểm", fontsize=10)

# Phân số sự ăn mòn theo địa điểm 
sns.boxplot(
    data=df_clean,
    x="Địa điểm",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    palette="pastel",
    ax=axes[2]
)
axes[2].set_title("Phân bố tốc độ ăn mòn theo địa điểm", fontsize=15, fontweight='bold')
axes[2].set_xlabel("Địa điểm", fontsize=12)
axes[2].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)", fontsize=12)
axes[2].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0, 1, 0.97])
output_folder = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(output_folder, "ketqua_bieudothang3.png"), dpi=200)
plt.show()