import configuration
import requests
import data


def post_new_order_and_get_track():  # создает новый заказ и возвращает трек
    order_response = requests.post(configuration.URL_SERVICE +
                                   configuration.CREATE_ORDER_PATH,
                                   json=data.order_body,
                                   headers=data.order_headers)
    return order_response.json()["track"]


def get_new_order_status_code(track):  # получение данных о заказе и возвращает код ответа
    info_response = requests.get(configuration.URL_SERVICE +
                                 configuration.GET_ORDER_INFO_PATH +
                                 str(track))
    return info_response.status_code
