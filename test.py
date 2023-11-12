import request


#Улич Марина, 10 когорта "Финальный проект, инженер по тестированию+"
# Тест проверки создания заказа
def test_order_creation():
    creation_response = request.post_new_order()
    track_id = creation_response.json()['track']
    response = request.get_orders_track(track_id)
    assert response.status_code == 200
