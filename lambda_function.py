Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
... import random
... 
... def lambda_handler(event, context):
...     mesajlar = [
...         "Bulut bilişim, geleceğin dilidir!",
...         "Hata yapmaktan korkma, her hata yeni bir öğrenme fırsatıdır.",
...         "AWS servislerini öğrenmek sana kapılar açar.",
...         "Serverless mimari ile sunucu yönetme derdine son!"
...     ]
...     
...     secilen_mesaj = random.choice(mesajlar)
...     
...     return {
...         'statusCode': 200,
...         'body': json.dumps({
...             'mesaj': secilen_mesaj,
...             'durum': 'Basarili'
...         }, ensure_ascii=False)
