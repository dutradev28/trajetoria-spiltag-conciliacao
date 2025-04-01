from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import random


class LoginBradesco:
    
    def __init__(self):
        try:
            load_dotenv()
            self.URL_BRADESCO = os.getenv("URL_BRADESCO")
            self.XPATH_USERNAME_BRADESCO = os.getenv("XPATH_USERNAME_BRADESCO")
            self.USERNAME_BRADESCO = os.getenv("USERNAME_BRADESCO")
            self.PASSWORD_BRADESCO = os.getenv("PASSWORD_BRADESCO")
            self.XPATH_PASSWORD_BRADESCO = os.getenv("XPATH_PASSWORD_BRADESCO")
            self.XPATH_BTN_ACESSAR_BRADESCO = os.getenv("XPATH_BTN_ACESSAR_BRADESCO")
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo .env {e}")
        
    def login_bradesco(self, driver):
        
        try:            
            
            print("Iniciando acesso ao internet banking Bradesco...")
            
            driver.get(self.URL_BRADESCO)
            
            input_username = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_USERNAME_BRADESCO))
            )
            input_username.send_keys(self.USERNAME_BRADESCO)
            
            input_password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_PASSWORD_BRADESCO))
            )
            input_password.send_keys(self.PASSWORD_BRADESCO)
            
            btn_entrar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_ACESSAR_BRADESCO))
            )

            actions = ActionChains(driver)

            actions.move_to_element_with_offset(
                btn_entrar, 
                random.uniform(-5, 5),  
                random.uniform(-5, 5)   
            )
            actions.pause(random.uniform(0.1, 0.3))

            actions.click_and_hold()

            actions.pause(random.uniform(0.05, 0.2))

            actions.release()

            actions.perform()
            
            time.sleep(18)
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']"))
            )
            
            checkbox_recaptcha = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-border"))
            )
            checkbox_recaptcha.click()
            
        except Exception as e:
            raise Exception(f"Erro ao realizar login bradesco: {e} ")
            
            
            
            
  
            
        
    