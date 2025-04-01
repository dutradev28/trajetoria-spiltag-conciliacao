from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os


class LoginSofisa:
    
    def __init__(self):
        try:
            load_dotenv()
            self.URL_SOFISA = os.getenv("URL_SOFISA")
            self.CODE_SOFISA_MATRIZ = os.getenv("CODE_SOFISA_MATRIZ")
            self.CODE_SOFISA_FILIAL = os.getenv("CODE_SOFISA_FILIAL")
            self.USERNAME_SOFISA_MATRIZ = os.getenv("USERNAME_SOFISA_MATRIZ")
            self.USERNAME_SOFISA_FILIAL = os.getenv("USERNAME_SOFISA_FILIAL")
            self.PASSWORD_SOFISA = os.getenv("PASSWORD_SOFISA")
            self.XPATH_CODE_SOFISA = os.getenv("XPATH_CODE_SOFISA")           
            self.XPATH_USERNAME_SOFISA = os.getenv("XPATH_USERNAME_SOFISA")
            self.XPATH_BTN_CONTINUAR_SOFISA = os.getenv("XPATH_BTN_CONTINUAR_SOFISA")
            self.XPATH_KEYBOARD_CONTAINER = os.getenv("XPATH_KEYBOARD_CONTAINER")
            self.XPATH_BTN_ENTRAR_SOFISA = os.getenv("XPATH_BTN_ENTRAR_SOFISA")
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo .env {e}")
        
        
    def login_sofisa_matriz(self, driver):
        try:
            print("Inicializando login banco sofisa matriz...")
            driver.get(self.URL_SOFISA)
            
            input_code = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_CODE_SOFISA))
            )
            input_code.send_keys(self.CODE_SOFISA_MATRIZ)
            
            input_username = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_USERNAME_SOFISA))
            )
            input_username.send_keys(self.USERNAME_SOFISA_MATRIZ)
            
            btn_continuar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_CONTINUAR_SOFISA))
            )
            btn_continuar.click()
            
            keyboard_container = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_KEYBOARD_CONTAINER))
            )
            
            for char in self.PASSWORD_SOFISA: 
                
                lines = keyboard_container.find_elements(By.XPATH, ".//div[@class='hg-row']")
                
                char_encontrado = False
                
                for line in lines:
                    try:
                        keys = line.find_elements(By.XPATH, ".//div[contains(@class, 'hg-button')]")
                        
                        for key in keys:                        
                            if key.text.strip().lower() == char.lower():
                                key.click()
                                
                                char_encontrado = True
                                break
                        if char_encontrado:
                            break
                    except Exception as e:
                        print(f"Erro ao procurar tecla: {e}")
                        continue
                if not char_encontrado:
                    print(f"Caractere '{char} não encontrado no teclado virtual")
            btn_entrar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_ENTRAR_SOFISA))
            )
            btn_entrar.click()
            
            print("Login realizado com sucesso ao banco sofisa matriz!")
        except Exception as e:
            raise Exception(f"Erro ao realizar o login banco sofisa: {e}")
        
    def login_sofisa_filial(self, driver):
        try:
            print("Inicializando login banco sofisa filial...")
            driver.get(self.URL_SOFISA)
            
            input_code = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_CODE_SOFISA))
            )
            input_code.send_keys(self.CODE_SOFISA_FILIAL)
            
            input_username = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_USERNAME_SOFISA))
            )
            input_username.send_keys(self.USERNAME_SOFISA_FILIAL)
            
            btn_continuar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_CONTINUAR_SOFISA))
            )
            btn_continuar.click()
            
            keyboard_container = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_KEYBOARD_CONTAINER))
            )
            
            for char in self.PASSWORD_SOFISA: 
                
                lines = keyboard_container.find_elements(By.XPATH, ".//div[@class='hg-row']")
                
                char_encontrado = False
                
                for line in lines:
                    try:
                        keys = line.find_elements(By.XPATH, ".//div[contains(@class, 'hg-button')]")
                        
                        for key in keys:                        
                            if key.text.strip().lower() == char.lower():
                                key.click()
                                
                                char_encontrado = True
                                break
                        if char_encontrado:
                            break
                    except Exception as e:
                        print(f"Erro ao procurar tecla: {e}")
                        continue
                if not char_encontrado:
                    print(f"Caractere '{char} não encontrado no teclado virtual")
            btn_entrar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_BTN_ENTRAR_SOFISA))
            )
            btn_entrar.click()
            
            print("Login realizado com sucesso ao banco sofisa filial!")
        except Exception as e:
            raise Exception(f"Erro ao realizar o login banco sofisa: {e}")
            
            
            
            