import requests
from bs4 import BeautifulSoup
import numpy as np

class CrashPredictor:
    def __init__(self, url):
        self.url = url
        self.coefficients = []

    def fetch_coefficients(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Проверка на ошибки HTTP
            soup = BeautifulSoup(response.text, 'html.parser')

            # Пример поиска коэффициентов (необходимо адаптировать под структуру страницы)
            for item in soup.find_all('div', class_='coefficient-class'):  # Замените 'coefficient-class' на правильный класс
                self.coefficients.append(float(item.text.strip()))
            print(f"Получено коэффициентов: {len(self.coefficients)}")
        except Exception as e:
            print(f"Ошибка при получении коэффициентов: {e}")

    def predict_next_coefficient(self):
        if len(self.coefficients) < 5:
            return None, 0  # Невозможно предсказать

        last_five = self.coefficients[-5:]
        prediction = np.mean(last_five)  # Предсказание на основе последних 5 коэффициентов
        accuracy = np.std(last_five) / prediction if prediction != 0 else 0  # Оценка точности
        return prediction, accuracy

    def display_prediction(self):
        prediction, accuracy = self.predict_next_coefficient()
        if prediction is not None:
            print(f"Прогноз следующего коэффициента: {prediction:.2f}")
            print(f"Точность прогноза: {accuracy:.2%}")
        else:
            print("Недостаточно данных для прогноза.")

def main():
    code = input("Введите код доступа: ")
    if code != "085432":
        print("Неверный код доступа.")
        return

    url = "https://1wcght.life/casino/play/1play_1play_fastcrash"  # Замените на актуальный URL
    predictor = CrashPredictor(url)
    
    predictor.fetch_coefficients()
    predictor.display_prediction()

if __name__ == "__main__":
    main()

