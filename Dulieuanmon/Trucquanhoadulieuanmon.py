import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 
output_folder = os.path.dirname(os.path.abspath(__file__))

# Trực quan hóa dữ liệu tháng 1 
df1 = pd.read_excel("d:/New folder/TocDoAnMon_CT3_01Thang.xlsx", sheet_name=0, header=2)
df1.columns = [
    "STT", "Địa điểm", "Tên mẫu", "Ngày đặt mẫu", "Ngày rút mẫu", "Số ngày",
    "Khối lượng ban đầu (g)", "Khối lượng sau lần 1 (g)", "Tốc độ ăn mòn (g/cm2.ngày)",
    "NaN_1", "Ghi chú"
]
df1 = df1.drop(columns=["NaN_1", "Ghi chú"])
df1 = df1.dropna(subset=["Tên mẫu", "Tốc độ ăn mòn (g/cm2.ngày)"])
df1["Tốc độ ăn mòn (g/cm2.ngày)"] = pd.to_numeric(df1["Tốc độ ăn mòn (g/cm2.ngày)"], errors="coerce")
df1 = df1.dropna(subset=["Tốc độ ăn mòn (g/cm2.ngày)"])
df1["Tháng"] = "Tháng 1"

# Trực quan hóa dữ liệu tháng 3
df3 = pd.read_excel("d:/New folder/TocDoAnMon_CT3_03Thang.xlsx")
df3.columns = [
    "STT", "Địa điểm", "Tên mẫu", "Ngày đặt mẫu", "Ngày rút mẫu", "Số ngày",
    "Khối lượng ban đầu (g)", "Khối lượng sau lần 1 (g)", "Tốc độ ăn mòn (g/cm2.ngày)",
    "NaN_1", "Ghi chú"
]
df3 = df3.drop(columns=["NaN_1", "Ghi chú"])
df3 = df3.dropna(subset=["Tên mẫu", "Tốc độ ăn mòn (g/cm2.ngày)"])
df3["Tốc độ ăn mòn (g/cm2.ngày)"] = pd.to_numeric(df3["Tốc độ ăn mòn (g/cm2.ngày)"], errors="coerce")
df3 = df3.dropna(subset=["Tốc độ ăn mòn (g/cm2.ngày)"])
df3["Tháng"] = "Tháng 3"

# Gộp dữ liệu
df_all = pd.concat([df1, df3], ignore_index=True)

fig, axs = plt.subplots(3, 3, figsize=(36, 18))

df1_plot = df1.copy()
# Biểu đồ tháng 1 
sns.barplot(
    data=df1_plot,
    x="Tên mẫu",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    color="skyblue",
    ax=axs[0, 0]
)
for container in axs[0, 0].containers:
    axs[0, 0].bar_label(container, fmt="%.2f", padding=3)
axs[0, 0].set_title("Tốc độ ăn mòn theo mẫu - Tháng 1", fontsize=13, fontweight='bold')
axs[0, 0].set_xlabel("Tên mẫu")
axs[0, 0].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")
axs[0, 0].tick_params(axis='x', rotation=30)
axs[0, 0].grid(axis='y', linestyle='--', alpha=0.7)

sns.boxplot(
    data=df1_plot,
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    color="skyblue",
    ax=axs[0, 1]
)
sns.swarmplot(
    data=df1_plot,
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    color=".25",
    ax=axs[0, 1]
)
axs[0, 1].set_title("Phân bố tốc độ ăn mòn - Tháng 1", fontsize=13, fontweight='bold')
axs[0, 1].set_xlabel("")
axs[0, 1].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")


sns.lineplot(
    data=df1_plot,
    x="Tên mẫu",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    marker="o",
    color="skyblue",
    ax=axs[0, 2]
)
axs[0, 2].set_title("Trung bình tốc độ ăn mòn theo mẫu - Tháng 1", fontsize=13, fontweight='bold')
axs[0, 2].set_xlabel("Tên mẫu")
axs[0, 2].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")
axs[0, 2].tick_params(axis='x', rotation=30)

# Trực quan hóa vẽ biểu đồ tháng 33
df3_plot = df3.copy()

sns.barplot(
    data=df3_plot,
    x="Tên mẫu",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    color="salmon",
    ax=axs[1, 0]
)
for container in axs[1, 0].containers:
    axs[1, 0].bar_label(container, fmt="%.2f", padding=3)
axs[1, 0].set_title("Tốc độ ăn mòn theo mẫu - Tháng 3", fontsize=13, fontweight='bold')
axs[1, 0].set_xlabel("Tên mẫu")
axs[1, 0].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")
axs[1, 0].tick_params(axis='x', rotation=30)
axs[1, 0].grid(axis='y', linestyle='--', alpha=0.7)


sns.boxplot(
    data=df3_plot,
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    color="salmon",
    ax=axs[1, 1]
)
sns.swarmplot(
    data=df3_plot,
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    color=".25",
    ax=axs[1, 1]
)
axs[1, 1].set_title("Phân bố tốc độ ăn mòn - Tháng 3", fontsize=13, fontweight='bold')
axs[1, 1].set_xlabel("")
axs[1, 1].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")

sns.lineplot(
    data=df3_plot,
    x="Tên mẫu",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    marker="o",
    color="salmon",
    ax=axs[1, 2]
)
axs[1, 2].set_title("Trung bình tốc độ ăn mòn theo mẫu - Tháng 3", fontsize=13, fontweight='bold')
axs[1, 2].set_xlabel("Tên mẫu")
axs[1, 2].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")
axs[1, 2].tick_params(axis='x', rotation=30)

# So sánh dữ liệu cả 2 tháng 
sns.barplot(
    data=df_all,
    x="Tên mẫu",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    hue="Tháng",
    ci=None,
    palette="Set1",
    ax=axs[2, 0]
)
for container in axs[2, 0].containers:
    axs[2, 0].bar_label(container, fmt="%.2f", padding=3)
axs[2, 0].set_title("So sánh tốc độ ăn mòn theo mẫu", fontsize=13, fontweight='bold')
axs[2, 0].set_xlabel("Tên mẫu")
axs[2, 0].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")
axs[2, 0].tick_params(axis='x', rotation=30)
axs[2, 0].grid(axis='y', linestyle='--', alpha=0.7)
axs[2, 0].legend(title="Tháng")

sns.boxplot(
    data=df_all,
    x="Tháng",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    palette="Set2",
    ax=axs[2, 1]
)
sns.swarmplot(
    data=df_all,
    x="Tháng",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    color=".25",
    ax=axs[2, 1]
)
axs[2, 1].set_title("Phân bố tốc độ ăn mòn", fontsize=13, fontweight='bold')
axs[2, 1].set_xlabel("Tháng")
axs[2, 1].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")


sns.lineplot(
    data=df_all,
    x="Tên mẫu",
    y="Tốc độ ăn mòn (g/cm2.ngày)",
    hue="Tháng",
    marker="o",
    ax=axs[2, 2]
)
axs[2, 2].set_title("Trung bình tốc độ ăn mòn theo mẫu", fontsize=13, fontweight='bold')
axs[2, 2].set_xlabel("Tên mẫu")
axs[2, 2].set_ylabel("Tốc độ ăn mòn (g/cm²/ngày)")
axs[2, 2].tick_params(axis='x', rotation=30)
axs[2, 2].legend(title="Tháng")

plt.tight_layout()
plt.savefig(os.path.join(output_folder, "so_sanh_thang1_thang3_full.png"), dpi=200)
plt.show()