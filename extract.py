import subprocess

CHANNELS = [
    ("东森财经", "https://www.youtube.com/watch?v=1I2iq41Akmo"),
    ("东森新闻", "https://www.youtube.com/watch?v=V1p33hqPrUk"),
    ("TVBS新闻", "https://www.youtube.com/watch?v=m_dhMSvUCIc"),
    ("民视新闻", "https://www.youtube.com/watch?v=ylYJSBUgaMA"),
    ("中天新闻", "https://www.youtube.com/watch?v=Tq-w6uMSMgc"),
    ("三立新闻", "https://www.youtube.com/watch?v=0pSsOaSxWhE"),
    ("华视新闻", "https://www.youtube.com/watch?v=KMMHw8rllic"),
    ("台视新闻", "https://www.youtube.com/watch?v=9iRAqBMakXY"),
    ("中视新闻", "https://www.youtube.com/@chinatvnews/live"),
    ("公视新闻", "https://www.youtube.com/watch?v=8hdJ0COTXHI"),
    ("寰宇新闻", "https://www.youtube.com/watch?v=a1YWMrmwXQs"),
    ("非凡电视", "https://www.youtube.com/watch?v=59HqonIWhmk")
]

m3u_content = "#EXTM3U\n"

print("开始批量提取 12 个台湾新闻频道的高清直链...")

for name, url in CHANNELS:
    print(f"正在提取: {name} ...", end="", flush=True)
    try:
        result = subprocess.run(
            ["yt-dlp", "-g", url],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().split("\n")
        if lines and lines[0]:
            stream_url = lines[0]
            m3u_content += f'#EXTINF:-1 tvg-name="{name}" group-title="台湾新闻", {name}\n'
            m3u_content += f"{stream_url}\n"
            print(" 成功！")
        else:
            print(" 失败（无输出）")
    except Exception as e:
        print(f" 跳过")

with open("tw-news-direct.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)

print("\n==================================================")
print("  全部处理完毕！已更新并生成文件：tw-news-direct.m3u")
print("==================================================")
