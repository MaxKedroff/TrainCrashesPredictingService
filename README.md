# сервис для обработки фото
а)порядок запуска локально:
1. pip install -r requirements.txt
2. python app.py
   
б)запуск через docker
1. docker pull maxkedroff2005/trainservice
2. docker run maxkedroff2005/trainservice
## связь с микроконтроллером
осуществляется по эндпоинту 0.0.0.0:5000/api/images POST в body передается файл с изображением
