import re
import urllib


class UserProfile:
    def __init__(self, soup):
        self.soup = soup

    def extract_name(self):
        """Извлекаем имя пользователя"""
        try:
            title_text = self.soup.title.string
            name = title_text.split(":")[0].strip()
            if name == "СДО ННГАСУ":
                profile_pic_tag = self.soup.find('div', class_='profilepic').find('img')
                if profile_pic_tag:
                    name = profile_pic_tag.get('alt', '').strip()
            return name
        except AttributeError:
            print("Ошибка: Не удалось извлечь имя пользователя.")
            return "Неизвестный пользователь"

    def extract_email(self):
        """Извлекаем email пользователя"""
        try:
            email_tag = self.soup.find('a', href=re.compile("mailto:"))
            if email_tag:
                email_encoded = email_tag['href'][7:]  # Убираем "mailto:"
                email = urllib.parse.unquote(bytes(email_encoded, "utf-8").decode("utf-8"))
                if email.startswith("lk@nngasu.ru"):
                    return "не указано"
                return email
            return None
        except Exception as e:
            print(f"Ошибка при извлечении email: {e}")
            return "не указано"
