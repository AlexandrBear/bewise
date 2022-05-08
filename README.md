## bewise
#### Необходимы Docer и Docker Compose
#### 1) Скачать проект.
#### 2) Зайти в папку bewise.
#### 3) Запустить комманду: docker-compose up.
#### 4) Открыть в браузере страницу: http://127.0.0.1:8000/
###  Запуск без Docer:
#### 1) Скачать проект.
#### 2) Зайти в папку bewise/app.
#### 3) Запустить комманду: pip3 install -r requirements.txt
#### 4) Создать базу данных и пользователя в ней.
#### 5) В файле config.py зменить параметр:
####    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:example@mysql/docker_mysql'
####    а) где mysql+mysqlconnector:// остается без изменений если используете MySql,
####       если нет то указать базу + коннектор(установить при помощи pip отдельно),
####    б) root имя пользователя в базе данных,
####    в) example пароль
####    г) mysql путь к базе (localhost)
####    д) docker_mysql имя базы данных
#### 6) Запустить комманду: python3 app.py
#### 7) Открыть в браузере страницу: http://localhost:5000/
