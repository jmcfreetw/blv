import requests

# Danh sách kênh gốc của bạn (chưa có ký hiệu)
channels = [
    {
        "name": "⚽ - blv tao thao",
        "logo": "https://i.ibb.co/B2FQqLqj/Photo-1784528515356.png",
        "group": "XemTV",
        "url": "https://hls.cdnfaster-a.live/live/TAOTHAO/index.m3u8?expire=1917964380&sign=6379fc6251248341f0547089859f8ee9"
    },
    {
        "name": "⚽ - blv phi ho",
        "logo": "https://i.ibb.co/B2FQqLqj/Photo-1784528515356.png",
        "group": "XemTV",
        "url": "https://hls.cdnfaster-a.live/live/PHIHO/index.m3u8?expire=2556118740&sign=ebc20a588b7a62eb65d12f7372d39a3f"
    },
    {
        "name": "⚽ - blv co ca",
        "logo": "https://i.ibb.co/B2FQqLqj/Photo-1784528515356.png",
        "group": "XemTV",
        "url": "https://live05.miekgo.app/live/24561735.m3u8?_t=1784389156608"
    },
    {
        "name": "⚽ - blv bi dao",
        "logo": "https://i.ibb.co/B2FQqLqj/Photo-1784528515356.png",
        "group": "XemTV",
        "url": "https://live05.miekgo.app/live/99121525.m3u8?_t=1784391812057"
    },
    {
        "name": "⚽ - blv c2",
        "logo": "https://i.ibb.co/B2FQqLqj/Photo-1784528515356.png",
        "group": "XemTV",
        "url": "https://live05.miekgo.app/live/08552895.m3u8"
    },
    {
        "name": "⚽ - blv 7 up",
        "logo": "https://i.ibb.co/B2FQqLqj/Photo-1784528515356.png",
        "group": "XemTV",
        "url": "https://live05.miekgo.app/live/78905744.m3u8"
    },
    {
        "name": "⚽ - blv sprite",
        "logo": "https://i.ibb.co/B2FQqLqj/Photo-1784528515356.png",
        "group": "XemTV",
        "url": "https://live05.miekgo.app/live/75748097.m3u8"
    }
]

def check_stream_online(url):
    """Hàm kiểm tra xem link m3u8 có phản hồi OK (200) hay không"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            return True
        # Một số server không hỗ trợ HEAD request, thử lại với GET nhẹ
        response = requests.get(url, headers=headers, timeout=5, stream=True)
        return response.status_code == 200
    except Exception:
        return False

def generate_m3u():
    m3u_content = "#EXTM3U\n"
    
    print("Đang kiểm tra trạng thái các luồng phát...\n")
    for item in channels:
        is_online = check_stream_online(item["url"])
        
        # Thêm ký hiệu đèn tương ứng
        if is_online:
            status_tag = "🟢 [ONLINE]"
            print(f"[ONLINE] {item['name']}")
        else:
            status_tag = "🔴 [OFFLINE]"
            print(f"[OFFLINE] {item['name']}")
            
        m3u_content += f'#EXTINF:-1 tvg-logo="{item["logo"]}" group-title="{item["group"]}", {status_tag} {item["name"]}\n'
        m3u_content += f'{item["url"]}\n'

    # Ghi ra file playlist_updated.m3u
    with open("playlist_updated.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print("\n=> Đã cập nhật xong file 'playlist_updated.m3u'!")

if __name__ == "__main__":
    generate_m3u()
