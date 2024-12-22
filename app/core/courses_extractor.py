class UserCourses:
    def __init__(self, soup):
        self.soup = soup

    def extract_courses(self):
        """Извлекаем курсы пользователя"""
        try:
            courses_section = self.soup.find_all('section', class_='node_category')
            courses = []
            for section in courses_section:
                if 'Информация о курсах' in section.text:
                    links = section.find_all('a')
                    courses = [link.get_text() for link in links]
            return courses
        except Exception as e:
            print(f"Ошибка при извлечении курсов: {e}")
            return []
