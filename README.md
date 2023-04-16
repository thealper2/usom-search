# usom-search

USOM veritabanında domain, ip ve url sorgusu yapabilirsiniz.

## Gereksinimler

usom-search aşağıdaki kütüphaneleri kullanır.

* Colorama
* Requests

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/usom-search.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| --domain  | Domain sorgulamasi. |
| --url     | URL sorgulamasi. |
| --ip      | IP sorgulamasi. |
```bash
usage: main.py [-h] [--domain DOMAIN] [--url URL] [--ip IP]

USOM veritabanininda domain, url ve ip sorgulamasi yapabilirsiniz.

options:
  -h, --help       show this help message and exit
  --domain DOMAIN  Domain sorgulamasi
  --url URL        URL sorgulamasi
  --ip IP          IP sorgulamasi
```

## Örnekler

```python
python3 main.py --ip IP_ADDRESS
python3 main.py --url URL_ADDRESS
python3 main.py --domain DOMAIN
```
