from icrawler.builtin import GoogleImageCrawler
import time

save_dir = '/Users/kittiphat/Downloads/รูปผีตาโขน'

google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir}, downloader_threads=1)

for idx, _ in enumerate(
    google_crawler.crawl(keyword='ผีตาโขน', max_num=300, min_size=(300, 300), file_idx_offset=0)
):
    time.sleep(1)  # หน่วง 1 วินาที ต่อการโหลดแต่ละรูป (ช่วยลดโอกาสโดนแบน)
