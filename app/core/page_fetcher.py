import asyncio
import aiohttp

from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url, headers, cookies):
        self.url = url
        self.headers = headers
        self.cookies = cookies
        self.response = None
        self.soup = None

    async def fetch_page(self):
        """Асинхронно получаем страницу по URL"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url, headers=self.headers, cookies=self.cookies, timeout=10) as response:
                    self.response = await response.text()
                    self.soup = BeautifulSoup(self.response, 'html.parser')
        except asyncio.TimeoutError:
            print(f"Ошибка: Таймаут при запросе к {self.url}")
        except Exception as e:
            print(f"Ошибка: {e}")