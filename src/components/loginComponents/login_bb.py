from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LoginBB:
    
    def __init__(self):
        try:
            load_dotenv()
            self.URL_BB = os.getenv("URL_BB")
            self.XPATH_CHAVE_J_BB = os.getenv("XPATH_CHAVE_J_BB")
            self.USERNAME_BB = os.getenv("USERNAME_BB")
            self.PASSWORD_BB = os.getenv("PASSWORD_BB")
            self.XPATH_PASSWORD_BB = os.getenv("XPATH_PASSWORD_BB")
            self.XPATH_BTN_ENTRAR_BB = os.getenv("XPATH_BTN_ENTRAR_BB")
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo .env {e}")        
    
        
    def login_bb(self, driver):
        try:
            print("Iniciando login banco do brasil")
            
            chave_j = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_CHAVE_J_BB))
            )
            chave_j.send_keys(self.USERNAME_BB)
            
            senha = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_PASSWORD_BB))
            )
            senha.send_keys(self.PASSWORD_BB)
            
            btn_entrar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_ENTRAR_BB))
            )
            btn_entrar.click()
            
            print("Login realizado com sucesso no BB.")
        except Exception as e:
            raise Exception(f"Erro ao realizar login banco BB: {e}")