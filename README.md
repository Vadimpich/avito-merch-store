# Avito Merch Store | Pichurin Vadim

### **📌 Описание проекта**
Avito Merch Store — это сервис, который позволяет пользователям обмениваться монетками и приобретать на них мерч. Пользователи могут переводить монеты друг другу, покупать товары и проверять свой баланс через API.

---

## **📦 Запуск проекта в Docker**

### 🔹 **Шаг 1: Клонируем репозиторий**
```bash
git clone https://github.com/your-repo/avito-merch-store.git
cd avito-merch-store
```

### 🔹 **Шаг 2: Запускаем контейнеры**
```bash
docker-compose up --build
```
✅ **Запустятся:**
- **PostgreSQL** на `localhost:5432`
- **FastAPI** на `localhost:8080`
- **Swagger UI** на `http://localhost:8080/docs`

### 🔹 **Шаг 3: Остановка контейнеров**
```bash
docker-compose down
```

---

## **🧪 Запуск тестов и линтера**

### 🔹 **Запуск тестов (`pytest`)**
```bash
docker-compose up tests
```
✅ Будут запущены все тесты с покрытием кода.

### 🔹 **Запуск линтера (`flake8`)**
```bash
docker-compose up lint
```
✅ Проверяет код на ошибки стиля и форматирования.

---


## 📖 **Swagger UI** (Документация API)
📌 Автоматически сгенерированная FastAPI документация доступна по адресу [http://localhost:8080/docs](http://localhost:8080/docs) (после запуска сервера)

---

## **📈 Нагрузочное тестирование (`locust`)**
🔹 Запускаем сервер FastAPI:
```bash
docker-compose up -d fastapi
```
🔹 Запускаем locust:
```bash
locust -f load_test.py
```
🔹 Открываем **`http://localhost:8089`** и задаём нагрузку.

⚠️ Для корректной работы нагрузочного тестирования необходимо выдать пользователю 'loadtest' большое кол-во монет (для переводов и покупок)

---
## **📌 Вопросы и проблемы**:
### 🔹 Не указано, где хранить товары
Было принято решение хранить товары в словаре в файле *app/services/merch_data.py* как мок-данные. Это позволило избежать дополнительного усложнения логики (так как ассортимент товаров фиксирован), а также обеспечить более быструю работу с товарами, так как доступ к словарю происходит мгновенно без SQL-запросов.

