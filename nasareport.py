import requests
import pandas as pd
from datetime import datetime, timedelta

# 1. CẤU HÌNH KẾT NỐI API NASA
API_KEY = "DEMO_KEY"  # Thay bằng API Key cá nhân của bạn sau khi đăng ký tại api.nasa.gov
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"

# Lấy mốc thời gian 3 ngày gần nhất để test dữ liệu thực tế
end_date = datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")

params = {
    "start_date": start_date,
    "end_date": end_date,
    "api_key": API_KEY
}

print(f"Đang kết nối tới NASA NEO API ({start_date} đến {end_date})...")
response = requests.get(BASE_URL, params=params)

# 2. XỬ LÝ VÀ LỌC DỮ LIỆU
if response.status_code == 200:
    raw_data = response.json()
    neo_list = []
    
    # Duyệt qua từng ngày trong dữ liệu trả về
    for date_key, objects in raw_data["near_earth_objects"].items():
        for obj in objects:
            # Trích xuất các thông số quan trọng nhất
            close_approach = obj["close_approach_data"][0]
            
            neo_info = {
                "Ngày tiếp cận": date_key,
                "Tên tiểu hành tinh": obj["name"],
                "Đường kính tối đa (m)": round(obj["estimated_diameter"]["meters"]["estimated_diameter_max"], 2),
                "Vận tốc (km/h)": round(float(close_approach["relative_velocity"]["kilometers_per_hour"]), 2),
                "Khoảng cách tới Trái Đất (km)": round(float(close_approach["miss_distance"]["kilometers"]), 2),
                "Cảnh báo nguy hiểm": "CÓ" if obj["is_potentially_hazardous_asteroid"] else "An toàn"
            }
            neo_list.append(neo_info)
            
    # Chuyển sang dạng bảng DataFrame của Pandas để dễ phân tích
    df = pd.DataFrame(neo_list)
    
    # Sắp xếp theo khoảng cách gần Trái Đất nhất
    df_sorted = df.sort_values(by="Khoảng cách tới Trái Đất (km)", ascending=True)
    
    # 3. XUẤT BÁO CÁO KẾT QUẢ RA MÀN HÌNH
    print("\n" + "="*55)
    print("KẾT QUẢ PHÂN TÍCH DỮ LIỆU NASA (DÙNG ĐỂ BÁO CÁO)")
    print("="*55)
    print(f"- Tổng số tiểu hành tinh ghi nhận: {len(df_sorted)}")
    
    hazardous_count = len(df_sorted[df_sorted["Cảnh báo nguy hiểm"] == "CÓ"])
    print(f"- Số lượng thuộc diện cảnh báo nguy hiểm: {hazardous_count}")
    
    closest_obj = df_sorted.iloc[0]
    print(f"- Vật thể bay gần Trái Đất nhất: {closest_obj['Tên tiểu hành tinh']} (Cách {closest_obj['Khoảng cách tới Trái Đất (km)']:,.0f} km)")
    
    print("\nTop 5 vật thể tiếp cận gần nhất:")
    print(df_sorted.head(5).to_string(index=False))
    
    # 4. LƯU RA FILE CSV & JSON ĐỂ NỘP CHO NHÓM TRƯỞNG / ĐƯA LÊN WEB
    df_sorted.to_csv("nasa_neo_report.csv", index=False, encoding="utf-8-sig")
    df_sorted.to_json("nasa_neo_data.json", orient="records", force_ascii=False, indent=4)
    print("\n[HOÀN TẤT] Đã xuất 2 file 'nasa_neo_report.csv' và 'nasa_neo_data.json' vào thư mục làm việc.")

else:
    print(f"Lỗi kết nối API. Mã lỗi: {response.status_code}")
    import requests
import pandas as pd
from datetime import datetime, timedelta

# 1. CẤU HÌNH KẾT NỐI API NASA
API_KEY = "DEMO_KEY"  # Thay bằng API Key cá nhân của bạn sau khi đăng ký tại api.nasa.gov
BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"

# Lấy mốc thời gian 3 ngày gần nhất để test dữ liệu thực tế
end_date = datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")

params = {
    "start_date": start_date,
    "end_date": end_date,
    "api_key": API_KEY
}

print(f"Đang kết nối tới NASA NEO API ({start_date} đến {end_date})...")
response = requests.get(BASE_URL, params=params)

# 2. XỬ LÝ VÀ LỌC DỮ LIỆU
if response.status_code == 200:
    raw_data = response.json()
    neo_list = []
    
    # Duyệt qua từng ngày trong dữ liệu trả về
    for date_key, objects in raw_data["near_earth_objects"].items():
        for obj in objects:
            # Trích xuất các thông số quan trọng nhất
            close_approach = obj["close_approach_data"][0]
            
            neo_info = {
                "Ngày tiếp cận": date_key,
                "Tên tiểu hành tinh": obj["name"],
                "Đường kính tối đa (m)": round(obj["estimated_diameter"]["meters"]["estimated_diameter_max"], 2),
                "Vận tốc (km/h)": round(float(close_approach["relative_velocity"]["kilometers_per_hour"]), 2),
                "Khoảng cách tới Trái Đất (km)": round(float(close_approach["miss_distance"]["kilometers"]), 2),
                "Cảnh báo nguy hiểm": "CÓ" if obj["is_potentially_hazardous_asteroid"] else "An toàn"
            }
            neo_list.append(neo_info)
            
    # Chuyển sang dạng bảng DataFrame của Pandas để dễ phân tích
    df = pd.DataFrame(neo_list)
    
    # Sắp xếp theo khoảng cách gần Trái Đất nhất
    df_sorted = df.sort_values(by="Khoảng cách tới Trái Đất (km)", ascending=True)
    
    # 3. XUẤT BÁO CÁO KẾT QUẢ RA MÀN HÌNH
    print("\n" + "="*55)
    print("KẾT QUẢ PHÂN TÍCH DỮ LIỆU NASA (DÙNG ĐỂ BÁO CÁO)")
    print("="*55)
    print(f"- Tổng số tiểu hành tinh ghi nhận: {len(df_sorted)}")
    
    hazardous_count = len(df_sorted[df_sorted["Cảnh báo nguy hiểm"] == "CÓ"])
    print(f"- Số lượng thuộc diện cảnh báo nguy hiểm: {hazardous_count}")
    
    closest_obj = df_sorted.iloc[0]
    print(f"- Vật thể bay gần Trái Đất nhất: {closest_obj['Tên tiểu hành tinh']} (Cách {closest_obj['Khoảng cách tới Trái Đất (km)']:,.0f} km)")
    
    print("\nTop 5 vật thể tiếp cận gần nhất:")
    print(df_sorted.head(5).to_string(index=False))
    
    # 4. LƯU RA FILE CSV & JSON ĐỂ NỘP CHO NHÓM TRƯỞNG / ĐƯA LÊN WEB
    df_sorted.to_csv("nasa_neo_report.csv", index=False, encoding="utf-8-sig")
    df_sorted.to_json("nasa_neo_data.json", orient="records", force_ascii=False, indent=4)
    print("\n[HOÀN TẤT] Đã xuất 2 file 'nasa_neo_report.csv' và 'nasa_neo_data.json' vào thư mục làm việc.")

else:
    print(f"Lỗi kết nối API. Mã lỗi: {response.status_code}")
    