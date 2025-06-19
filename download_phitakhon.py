from icrawler.builtin import GoogleImageCrawler
from icrawler.downloader import ImageDownloader
import os
import hashlib
import urllib.parse

# Custom Downloader ให้ใช้ชื่อไฟล์จาก URL จริง
class CustomDownloader(ImageDownloader):
    def get_filename(self, task, default_ext):
        url_path = urllib.parse.urlparse(task['file_url']).path
        original_name = os.path.basename(url_path)
        # บาง url ไม่มีชื่อไฟล์หรือไม่มีนามสกุล
        if '.' not in original_name:
            original_name = original_name + default_ext
        # ป้องกันชื่อซ้ำ
        save_path = os.path.join(self.storage.root_dir, original_name)
        i = 1
        base, ext = os.path.splitext(original_name)
        while os.path.exists(save_path):
            save_path = os.path.join(self.storage.root_dir, f"{base}_{i}{ext}")
            i += 1
        return save_path

save_dir = '/Users/kittiphat/Downloads/รูปผีตาโขน'
max_images_per_kw = 200

keywords = [
    'ผีตาโขน',
    'ผีตาโขนเลย',
    'ผีตาโขนเมืองเลย',
    'phi ta khon',
    'phi ta khon Loei',
    'phi ta khon thailand',
    'ghost festival thailand',
    'loei mask festival',
    'พิธีผีตาโขน',
    'ประเพณีผีตาโขน'
]

print('--- เริ่มดาวน์โหลดภาพจาก Google ---')
for kw in keywords:
    print(f'--- คำค้น: {kw} ---')
    crawler = GoogleImageCrawler(
        storage={'root_dir': save_dir},
        downloader_cls=CustomDownloader,
        downloader_threads=1
    )
    crawler.crawl(keyword=kw, max_num=max_images_per_kw, min_size=(640, 640))

print('--- ดาวน์โหลดภาพเสร็จสิ้น ---')

# 2. เช็คและลบไฟล์ภาพซ้ำ
print('--- กำลังเช็คและลบไฟล์ซ้ำ ---')
hashes = {}
removed = 0
for filename in os.listdir(save_dir):
    filepath = os.path.join(save_dir, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash in hashes:
            os.remove(filepath)
            removed += 1
        else:
            hashes[filehash] = filename

print(f'ลบไฟล์ซ้ำแล้ว {removed} ไฟล์')
print(f'ภาพที่ไม่ซ้ำกันทั้งหมด {len(hashes)} ไฟล์ (อยู่ใน {save_dir})')
