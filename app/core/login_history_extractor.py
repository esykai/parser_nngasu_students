class UserLoginInfo:
    def __init__(self, soup):
        self.soup = soup

    def extract_login_info(self):
        """Извлекаем информацию о последних входах в систему"""
        try:
            login_info = {}
            login_section = self.soup.find_all('section', class_='node_category')
            for section in login_section:
                if 'Входы в систему' in section.text:
                    entries = section.find_all('dl')
                    for entry in entries:
                        dt = entry.find('dt')
                        dd = entry.find('dd')
                        if dt and dd:
                            login_info[dt.get_text()] = dd.get_text().replace('\xa0', ' ')
            return login_info
        except Exception as e:
            print(f"Ошибка при извлечении информации о входах: {e}")
            return {}
