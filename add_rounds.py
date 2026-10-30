import json
import csv

# 1. نقرأ ملف المباريات (Book1.csv)
matches_data = []
try:
    with open('Book1.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) # تخطي العنوان
        for row in reader:
            if len(row) < 4: continue
            
            home = row[0].strip()
            score = row[1].strip()
            away = row[2].strip()
            round_num = row[3].strip()
            
            if '-' in score:
                parts = score.split('-')
                hs = parts[0].strip()
                as_ = parts[1].strip()
            else:
                hs = score
                as_ = ''
            
            matches_data.append({
                "home": home,
                "away": away,
                "hs": hs,
                "as": as_,
                "round": round_num
            })
except Exception as e:
    print(f"خطأ في قراءة ملف Book1.csv: {e}")

# 2. نقرأ ملف data.json
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"خطأ في قراءة data.json: {e}")
    exit()

# 3. نحدث المباريات (نضيف حقل round)
if "results" in data:
    for match in data["results"]:
        for m in matches_data:
            if match.get("home") == m["home"] and match.get("away") == m["away"]:
                match["round"] = m["round"]
                break

# 4. نحفظ الملف المحدث
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("تم تحديث المباريات برقم الجولة بنجاح!")