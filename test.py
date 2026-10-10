
class TestCase4:
    def test_quantity(self, get_signals):
        assert len(get_signals) == 10, "Количество сигналов не соответствует ТЗ"

    def test_ids_and_names(self, get_signals):
        """
        Проверяем валидность ID и Имен сигналов.
        Так как эталонной БД в ТЗ нет, имитируем список ожидаемых ID и Имен.
        Принимаем, что данные приходят в виде списка списков: [ID, Name, Value, Quality, Time]
        """
        signals_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        signals_names = ["Signal_1", "Signal_2", "Signal_3", "Signal_4", "Signal_5", "Signal_6", "Signal_7",
                         "Signal_8", "Signal_9", "Signal_10"]
        for signal in get_signals:
            # принимаем что сигналы идут в виде списка списков
            assert signal[0] in signals_ids, "Получен сигнал с неизвестным ID"
            assert signal[1] in signals_names, 'Получен сигнал с неизвестным именем'

    def test_sine_waves(self, get_signals):
        for signal in get_signals:
            # Тут принимаем что у нас есть признак по которому мы определяем синусоиды,
            # либо мы знаем их ID, либо в данных есть флажок
            if signal[6] == "sine wave":
                assert -1 <= signal[3] <= 1, 'Сигнал-синусоида выходит за пределы допустимых значений'

