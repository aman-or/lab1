import sys
import requests

from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow


class Weather(QMainWindow):
    def __init__(self):
        super(Weather, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # actions
        self.ui.btn_start.clicked.connect(self.weather_check)
        self.ui.btn_start.clicked.connect(self.get_city_info)

        # Set word wrap for labels
        self.ui.label_2.setWordWrap(True)
        self.ui.lbl_temper.setWordWrap(True)

    def weather_check(self):
        api_key = "1dab56cc2eb7d368875015a88372deb5"

        # requests
        weather_url = (f"http://api.openweathermap.org/data/2.5/weather?q="
                       f"{self.ui.lbl_name.text()}&appid={api_key}&units=metric")
        weather_responce = requests.get(weather_url)
        weather_data = weather_responce.json()

        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            # reload interface
            self.ui.lbl_temper.setStyleSheet("font-size: 45pt; color: white;")
            self.ui.lbl_temper.setText(f"{temperature}°C")
            self.ui.lbl_humid.setText(f"Влажность: {humidity}%")
            self.ui.label_wind.setText(f"Ветер: {wind_speed} м/с")

        else:
            self.ui.lbl_temper.setStyleSheet("font-size: 10pt; color: white;")
            self.ui.lbl_temper.setText('Ошибка получение данных о погоде')
            self.ui.lbl_humid.setText('')
            self.ui.label_wind.setText('')

    def get_city_info(self):
        url = f"https://ru.wikipedia.org/api/rest_v1/page/summary/{self.ui.lbl_name.text()}"
        responce = requests.get(url)

        if responce.status_code == 200:
            data = responce.json()
            title = data.get('title', '')
            extract = data.get('extract', '')
            if title != '':
                self.ui.label_2.setText(f"Информация о городе {title}: \n{extract[:300]}...")
            else:
                print('Ничего не найдено')
                self.ui.label_2.setText("Ничего не найдено")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Weather()
    window.get_city_info()
    window.show()

    sys.exit(app.exec())
