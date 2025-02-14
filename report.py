import requests
from requests import request


def send_report(detection_result, image_id=None):

    report_endpoint = "http://"

    payload = {
        "image_id": image_id,
        "detection_result": detection_result
    }

    try:
        response = requests.post(report_endpoint, json=payload, timeout=1)
        if response.status_code == 200:
            print("выявлено нарушение, отчет успешно отправлен")
        else:
            print("Ошибка отправки отчёта. Код статуса:", response.status_code)
    except Exception as e:
        print("Ошибка при отправке отчёта:", str(e))