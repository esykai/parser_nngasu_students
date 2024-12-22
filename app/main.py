import os
import asyncio

from dotenv import load_dotenv

from core import UserProfileFetcher

# Загружаем конфигурацию из .env файла
load_dotenv()

async def fetch_user_data(user_id, result_list):
    """Запрашиваем и выводим данные для пользователя по его ID асинхронно."""
    url = f"https://lms.nngasu.ru/user/profile.php?id={user_id}"

    cookies = {
        "MoodleSession": os.getenv("MOODLE_SESSION"),
    }

    try:
        # Инициализация и получение данных пользователя с использованием сессии aiohttp
        fetcher = UserProfileFetcher(url, None, cookies)
        await fetcher.fetch_profile()

        name = fetcher.user_profile.extract_name()
        email = fetcher.user_profile.extract_email()
        courses = fetcher.user_courses.extract_courses()
        login_info = fetcher.user_login_info.extract_login_info()

        # Добавляем информацию о пользователе в список
        result_list.append({
            "user_id": user_id,
            "name": name,
            "email": email,
            "courses": courses,
            "login_info": login_info
        })

        print(f"User ID: {user_id}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Courses: {courses}")
        print(f"Login Info: {login_info}")
        print("-" * 40)  # Разделитель для каждого пользователя
    except Exception as e:
        print(f"Error fetching data for user ID {user_id}: {e}")


async def fetch_and_write_data():
    # Создаем пустой список для результатов
    result_list = []

    # Запрашиваем данные для пользователей с ID от 0 до 12000
    for user_id in range(0, 4368):
        await fetch_user_data(user_id, result_list)



# Запускаем асинхронный цикл
asyncio.run(fetch_and_write_data())