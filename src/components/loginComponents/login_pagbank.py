from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class LoginPagBank:
    
    def __init__(self):
        try:
            load_dotenv()
            self.URL_PAGBANK= os.getenv("URL_PAGBANK")
            self.USERNAME_PAGBANK = os.getenv("USERNAME_PAGBANK")
            self.PASSWORD_PAGBANK = os.getenv("PASSWORD_PAGBANK")
            self.XPATH_USERNAME_PAGBANK = os.getenv("XPATH_USERNAME_PAGBANK")
            self.XPATH_BTN_CONTINUAR_PAGBANK = os.getenv("XPATH_BTN_CONTINUAR_PAGBANK")
            self.XPATH_FORM_PASSWORD_PAGBANK = os.getenv("XPATH_FORM_PASSWORD_PAGBANK")
            self.XPATH_BTN_ENTRAR_PAGBANK = os.getenv("XPATH_BTN_ENTRAR_PAGBANK")
            
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo .env {e}")
        
    def login_pagbank(self, driver):
        try:
            print("Inicializando login pagbank...")
            
            driver.get(self.URL_PAGBANK)
            
            input_username = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_USERNAME_PAGBANK))
            )
            input_username.send_keys(self.USERNAME_PAGBANK)
            
            btn_continuar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_CONTINUAR_PAGBANK))
            )
            btn_continuar.click()
            
            form = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_FORM_PASSWORD_PAGBANK))
            )
            
            inputs = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"{self.XPATH_FORM_PASSWORD_PAGBANK}//input"))
            )
            for index, char in enumerate(self.PASSWORD_PAGBANK):
                
                current_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"{self.XPATH_FORM_PASSWORD_PAGBANK}//input[{index+1}]"))
                )
                current_input.clear()
                current_input.send_keys(char)
                time.sleep(0.2)
            
            btn_entrar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_ENTRAR_PAGBANK))
            )
            btn_entrar.click()
                
        except Exception as e:
            raise Exception(f"Erro ao realizar login pagbank: {e}")
                
                
            