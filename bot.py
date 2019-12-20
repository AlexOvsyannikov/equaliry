import time
import vk_api
token = "a2fcc754b6ad21bb0e46eb080769a6cdd96c5fc24194598b3c1f28ea5d08d47eed37d70159a9fec457a79"

vk = vk_api.VkApi(token=token)

vk._auth_token()

a = None
b = None
c = None
i = '@'
comand = 0
while True:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]

            if body.lower() == 'start':
                vk.method("messages.send", {"peer_id": id, 'random_id':0, "message":"""
 Привет, меня зовут Лютик. Я являюсь программой для помощи в обучении математике.
Для начала я выведу список комманд, которые я поддерживаю:
1 - Решить квадратное уравнение через дискриминант
2 - Решить квадратное уравнение через теорему Виета
3 - Разложить выражение на множители
4 - Информация
5 - Прочитать отзывы
6 - Оставить отзыв
7 - Завершить программу """})

            elif body.lower() == '1':
                vk.method("messages.send", {"peer_id": id, 'random_id': 0, "message": 'Отлично, запускаю сценарий решения квадратного уравнения через дискриминант!'})
                vk.method("messages.send", {"peer_id": id, 'random_id': 0, "message": """Введите первый коэффициент (a!=0)"""})
                i = 0


            elif i == 0:
                try:
                    a = int(body)
                    vk.method("messages.send",{"peer_id": id, 'random_id': 0, "message": """Введите второй коэффициент"""})
                    i = 1

                except:
                    vk.method("messages.send",{"peer_id": id, 'random_id': 0, "message": """Ошибка данных"""})

            elif i == 1:
                try:
                    b = int(body)
                    vk.method("messages.send",{"peer_id": id, 'random_id': 0, "message": """Введите третий коэффициент"""})
                    i = 2
                except:
                    vk.method("messages.send", {"peer_id": id, 'random_id': 0, "message": """Ошибка данных"""})

            elif i == 2:
                try:
                    c = int(body)
                    vk.method("messages.send", {"peer_id": id, 'random_id': 0, "message": str(a*b*c)})
                except:
                    vk.method("messages.send", {"peer_id": id, 'random_id': 0, "message": """Ошибка данных"""})
