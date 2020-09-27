# Crawler-JS
Dùng scrapy-splash kết hợp lua script để crawl các trang web sử dụng Javascript (websosanh)
```
├── crawl_service
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── run.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       └── websosanh.py
        └── lazada.py
├── requirements.txt
└── scrapy.cfg
```

- Cài đặt Splash 

Cài Docker sau đó chạy 
```
$ sudo docker pull scrapinghub/splash
```
và
```
$ sudo docker run -p 8050:8050 scrapinghub/splash
```
- Cài các thư viện cần thiết khác ( Nên dùng virtualenv )
```
pip install -r requirements.txt
```
- Chạy script 
```
python run.py
```
hoặc 
```
scrapy crawl wss 
scrapy crawl lazada
```
