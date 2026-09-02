import os
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    print("錯誤：找不到環境變數 MONGO_URI，請在啟動時設定。")
    sys.exit(1)

try:
    print("正在嘗試連線到 MongoDB Atlas...")
    client = MongoClient(MONGO_URI)
    

    client.admin.command('ping')
    print("✅ 成功！Python 程式已順利連線上雲端 MongoDB Atlas！")
    

    db = client["test_db"]
    collection = db["test_collection"]
    

    print("\n🔍 正在從雲端資料庫撈取所有資料...")
    

    cursor = collection.find()
    

    count = 0
    for document in cursor:
        count += 1
        print(f"第 {count} 筆資料：", document)
        
    print(f"\n🎉 撈取完畢！總共成功抓到 {count} 筆資料。")
    

except ConnectionFailure:
    print("❌ 連線失敗：請檢查白名單設定，或帳號密碼是否正確。")
except Exception as e:
    print(f"❌ 發生其他錯誤: {e}")
