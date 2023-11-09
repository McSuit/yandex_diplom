import configuration
import requests
import data


def post_new_order_and_get_status_code():  # создает новый заказ и возвращает код ответа
    order_response = requests.post(configuration.URL_SERVICE +
                                   configuration.CREATE_ORDER_PATH,
                                   json=data.order_body,
                                   headers=data.order_headers)  # запрос на создание заказа
    track = order_response.json()["track"]  # сохранение трека заказа
    info_response = requests.get(configuration.URL_SERVICE +
                                 configuration.GET_ORDER_INFO_PATH +
                                 str(track))  # запрос на получения заказа по треку
    return info_response.status_code  # возврат кода ответа
