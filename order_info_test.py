# Максим Качмазов, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_new_order_status_code_is_200():  # проверяет возможность получения данных по треку
    track = sender_stand_request.post_new_order_and_get_track()
    status_code = sender_stand_request.get_new_order_status_code(track)
    assert status_code == 200
    
