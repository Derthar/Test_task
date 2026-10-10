import socket
import json
import pytest
from credentials import Credentials


@pytest.fixture(scope="class")
def get_signals():
    # коннектимся
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((Credentials.HOST_NAME, Credentials.PORT))

    # Получаем и обрабатываем данные
    data = s.recv(4096).decode('utf-8')
    signals = json.loads(data)

    yield signals

    s.close()