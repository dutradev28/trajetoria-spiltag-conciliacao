from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class LoginSantander:
    
    def __init__(self):
        try:
            load_dotenv()
            self.URL_SANTANDER = os.getenv("URL_SANTANDER")
            self.AGENCIA_SANTANDER = os.getenv("AGENCIA_SANTANDER")
            self.CONTA_SANTANDER = os.getenv("CONTA_SANTANDER")
            self.USERNAME_SANTANDER = os.getenv("USERNAME_SANTANDER")
            self.PASSWORD_SANTANDER = os.getenv("PASSWORD_SANTANDER")
            self.XPATH_AGENCIA_SANTANDER = os.getenv("XPATH_AGENCIA_SANTANDER")
            self.XPATH_CONTA_SANTANDER = os.getenv("XPATH_CONTA_SANTANDER")
            self.XPATH_BTN_ENTRAR_SANTANDER = os.getenv("XPATH_BTN_ENTRAR_SANTANDER")
            self.XPATH_USERNAME_SANTANDER = os.getenv("XPATH_USERNAME_SANTANDER")
            self.XPATH_PASSWORD_SANTANDER = os.getenv("XPATH_PASSWORD_SANTANDER")
            self.XPATH_BTN_CONTINUAR_SANTANDER = os.getenv("XPATH_BTN_CONTINUAR_SANTANDER")
        except Exception as e:
            raise Exception(f"Erro ao carregar .env: {e}")
        
    
    def login_santander(self, driver):
        try:
            print("Iniciando login banco santander")
            
            driver.get(self.URL_SANTANDER)
            
            agencia_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_AGENCIA_SANTANDER))
            )
            agencia_input.send_keys(self.AGENCIA_SANTANDER)
            
            conta_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_CONTA_SANTANDER))
            )
            conta_input.send_keys(self.CONTA_SANTANDER)
            
            btn_entrar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_ENTRAR_SANTANDER))
            )
            btn_entrar.click()
            time.sleep(6)
            username_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_USERNAME_SANTANDER))
            )
            username_input.send_keys(self.USERNAME_SANTANDER)
            
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_PASSWORD_SANTANDER))
            )
            password_input.send_keys(self.PASSWORD_SANTANDER)
            
            btn_continuar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_CONTINUAR_SANTANDER))
            )
            btn_continuar.click()
            
            print("Login santander realizado com sucesso!")
            
        
        except Exception as e:
            raise Exception(f"Erro ao realizar login no banco santander: {e}")
    