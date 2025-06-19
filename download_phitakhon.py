from icrawler.builtin import BingImageCrawler

save_dir = '/Users/kittiphat/Downloads/รูปผีตาโขน'

bing_crawler = BingImageCrawler(storage={'root_dir': save_dir}, downloader_threads=1)
bing_crawler.crawl(keyword='ผีตาโขน', max_num=300, min_size=(300, 300))
