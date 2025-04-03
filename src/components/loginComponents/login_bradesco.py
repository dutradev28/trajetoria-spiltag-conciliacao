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
            self.CSS_USERNAME_BRADESCO = os.getenv("CSS_USERNAME_BRADESCO")
            self.USERNAME_BRADESCO = os.getenv("USERNAME_BRADESCO")
            self.PASSWORD_BRADESCO = os.getenv("PASSWORD_BRADESCO")
            self.CSS_PASSWORD_BRADESCO = os.getenv("CSS_PASSWORD_BRADESCO")
            self.CSS_BTN_ACESSAR_BRADESCO = os.getenv("CSS_BTN_ACESSAR_BRADESCO")
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo .env {e}")
        
    def login_bradesco(self, driver, max_retries=3):
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                print(f"Tentativa de login {retry_count + 1}/{max_retries}...")
                
                driver.get(self.URL_BRADESCO)
                
                input_username = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_USERNAME_BRADESCO))
                )
                input_username.send_keys(self.USERNAME_BRADESCO)
                
                input_password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_PASSWORD_BRADESCO))
                )
                input_password.send_keys(self.PASSWORD_BRADESCO)
                
                btn_entrar = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_BTN_ACESSAR_BRADESCO))
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
                
                time.sleep(6)
                
                try:
                    error_message = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "#modalBoxAlertMessage"))
                    )
                    if error_message.is_displayed():
                        print("Mensagem de erro detectada. Tentando novamente...")
                        retry_count += 1
                        driver.refresh()
                        continue
                except:
                    pass
                  
                time.sleep(20)
                              
                print("Login realizado com sucesso!")
                return True
                    
            except Exception as e:
                print(f"Erro durante o login: {str(e)}")
                retry_count += 1
                if retry_count < max_retries:
                    print("Reiniciando navegador para nova tentativa...")
                    driver.refresh()
                    time.sleep(2)
        
        raise Exception(f"Falha no login após {max_retries} tentativas")
            
            
            
            
  
            
        
    