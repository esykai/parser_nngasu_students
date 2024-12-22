from core.courses_extractor import UserCourses
from core.login_history_extractor import UserLoginInfo
from core.page_fetcher import WebScraper
from core.profile_parser import UserProfile


class UserProfileFetcher:
    def __init__(self, url, headers, cookies):
        self.scraper = WebScraper(url, headers, cookies)
        self.user_profile = None
        self.user_courses = None
        self.user_login_info = None

    async def fetch_profile(self):
        """Получаем и обрабатываем профиль пользователя"""
        try:
            await self.scraper.fetch_page()
            if not self.scraper.soup:
                print("Ошибка: Не удалось загрузить страницу.")
                return

            self.user_profile = UserProfile(self.scraper.soup)
            self.user_courses = UserCourses(self.scraper.soup)
            self.user_login_info = UserLoginInfo(self.scraper.soup)
        except Exception as e:
            print(f"Ошибка при обработке профиля: {e}")

    def display_info(self):
        """Выводим информацию о пользователе"""
        try:
            name = self.user_profile.extract_name()
            email = self.user_profile.extract_email()
            courses = self.user_courses.extract_courses()
            login_info = self.user_login_info.extract_login_info()

            print("Имя пользователя:", name)
            print("Адрес электронной почты:", email)
            print("Курсы:", courses)
            print("Информация о входах в систему:", login_info)
        except Exception as e:
            print(f"Ошибка при выводе информации: {e}")
