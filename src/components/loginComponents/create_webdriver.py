from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from dotenv import load_dotenv
import os


class CreateWebdriver:    
    def __init__(self):
        try:
            load_dotenv()
            self.PATH_EXTENSION = os.getenv("PATH_EXTENSION")
            self.USER_DATA_DIR = os.path.join(os.getcwd(), "chrome_profile")
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo .env {e}")
    
    def create_driver(self):
        try:
            os.makedirs(self.USER_DATA_DIR, exist_ok=True)
            chrome_options = Options()
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--enable-unsafe-swiftshader")
            chrome_options.add_argument("--disable-dev-shm-usage")            
            chrome_options.add_argument("--log-level=3")                      
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_extension(self.PATH_EXTENSION)
            chrome_options.add_argument(f"--user-data-dir={self.USER_DATA_DIR}")          
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            return driver
        except Exception as e:
            raise Exception(f"Erro ao criar webdriver: {e}")