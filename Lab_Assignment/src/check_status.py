import os
import weaviate
from dotenv import load_dotenv

load_dotenv()

def check_status():
    print("=" * 50)
    print("WEAVIATE & EMBEDDING PIPELINE CHECK")
    print("=" * 50)

    # 1. Kiểm tra API Keys trong .env
    print("\n1. Kiểm tra cấu hình .env:")
    # Load all GEMINI keys
    keys = []
    k = os.getenv("GEMINI_API_KEY", "").strip()
    if k and not k.startswith("your_"):
        keys.append(k)
    for i in range(2, 20):
        k = os.getenv(f"GEMINI_API_KEY_{i}", "").strip()
        if k and not k.startswith("your_"):
            keys.append(k)
    
    print(f"  - Số lượng Gemini API Keys cấu hình thành công: {len(keys)}")
    if not keys:
        print("  ⚠ LƯU Ý: Không tìm thấy Gemini API Key hợp lệ nào! Hãy điền key vào file .env.")

    # 2. Kết nối Weaviate
    weaviate_url = os.getenv("WEAVIATE_URL", "").strip()
    weaviate_key = os.getenv("WEAVIATE_API_KEY", "").strip()
    
    print(f"\n2. Kết nối tới Weaviate Cloud:")
    print(f"  - URL: {weaviate_url}")
    
    try:
        import weaviate.classes.init as wvc_init
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url=weaviate_url,
            auth_credentials=weaviate.auth.Auth.api_key(weaviate_key),
            skip_init_checks=True,
            additional_config=wvc_init.AdditionalConfig(
                timeout_=wvc_init.Timeout(init=60, query=60, insert=120)
            )
        )
        
        collections = client.collections.list_all()
        print("  ✓ Kết nối Weaviate thành công!")
        print(f"  - Các Collections hiện có: {list(collections.keys())}")
        
        collection_name = "DrugLawDocs"
        if collection_name in collections:
            collection = client.collections.get(collection_name)
            res = collection.aggregate.over_all(total_count=True)
            print(f"  - Collection '{collection_name}': ĐÃ TỒN TẠI")
            print(f"    → Số lượng chunks đã index: {res.total_count}")
        else:
            print(f"  - Collection '{collection_name}': CHƯA TỒN TẠI")
            print("    (Nó sẽ tự động được tạo và index khi bạn chạy thành công file 'src/task4_chunking_indexing.py')")
            
        client.close()
    except Exception as e:
        print(f"  ✗ Lỗi kết nối tới Weaviate: {e}")
        
    print("=" * 50)

if __name__ == "__main__":
    check_status()
