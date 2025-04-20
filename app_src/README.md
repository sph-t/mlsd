# Как запустить демо
1. poetry install --no-root
2. cd app_src
3. poetry run streamlit run app.py

# Запуск докер образа

# Инструкция по развертыванию приложения

## Предварительные требования
- [Docker](https://docs.docker.com/get-docker/) (версия 20.10.0+)
- [Docker Compose](https://docs.docker.com/compose/install/) (версия 2.0.0+)

- 1 ГБ свободного места на диске
- Порты 8501 или 8502 должны быть свободны

## Быстрый старт
1. Клонируйте репозиторий:
   ```bash
   git clone git@git.culab.ru:course-projects/mlsd/solutions/f.zakharov.git
   cd f.zakharov
   ```

2. Запустите сборку и запуск:
    ```bash
    docker-compose up --build
    ```

3. Приложение будет доступно по адресу:
   http://localhost:8501