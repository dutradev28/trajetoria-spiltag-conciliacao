from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
import time
import shutil

class ExtractSofisa:
    
    def __init__(self):
        try:
            load_dotenv()
            self.XPATH_CONTACORRENTE_SOFISA = os.getenv("XPATH_CONTACORRENTE_SOFISA")
            self.XPATH_EXTRATO_SOFISA = os.getenv("XPATH_EXTRATO_SOFISA")
            self.XPATH_IFRAME_SOFISA = os.getenv("XPATH_IFRAME_SOFISA")
            self.XPATH_DIAS_SOFISA = os.getenv("XPATH_DIAS_SOFISA")
            self.XPATH_30DIAS_SOFISA = os.getenv("XPATH_30DIAS_SOFISA")
            self.XPATH_SALVAREXCEL_SOFISA = os.getenv("XPATH_SALVAREXCEL_SOFISA")
            self.XPATH_LI_SAIR_SOFISA = os.getenv("XPATH_LI_SAIR_SOFISA")
            self.XPATH_SAIR_SOFISA = os.getenv("XPATH_SAIR_SOFISA")
        except Exception as e:
            raise Exception(f"Erro ao carregar .env: {e}")
        
    
    def extract_sofisa_matriz(self, driver):
        try:
            conta_corrente = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_CONTACORRENTE_SOFISA))
            )
            conta_corrente.click()
            
            extrato = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_EXTRATO_SOFISA))
            )
            extrato.click()
            
            time.sleep(2)            
            
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.XPATH_IFRAME_SOFISA))
            )
            
            dias_select = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_DIAS_SOFISA))
            )
            driver.execute_script("arguments[0].click();", dias_select)
            
            dias_30 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_30DIAS_SOFISA))
            )
            driver.execute_script("arguments[0].click();", dias_30)
            
            time.sleep(2)
            
            salvar_excel = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_SALVAREXCEL_SOFISA))
            )
            salvar_excel.click()
            driver.switch_to.default_content()
            time.sleep(2)
            
            li_sair = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_LI_SAIR_SOFISA))
            )
            driver.execute_script("arguments[0].click();", li_sair)
            
            btn_sair = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_SAIR_SOFISA))
            )
            driver.execute_script("arguments[0].click();", btn_sair)
            
        except Exception as e:
            raise Exception(f"Erro ao baixar extrato sofisa matriz: {e}")
        
    def extract_sofisa_filial(self, driver):
        try:
            conta_corrente = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_CONTACORRENTE_SOFISA))
            )
            conta_corrente.click()
            
            extrato = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_EXTRATO_SOFISA))
            )
            extrato.click()
            
            time.sleep(2)            
            
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.XPATH_IFRAME_SOFISA))
            )
            
            dias_select = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_DIAS_SOFISA))
            )
            driver.execute_script("arguments[0].click();", dias_select)
            
            dias_30 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_30DIAS_SOFISA))
            )
            driver.execute_script("arguments[0].click();", dias_30)
            
            time.sleep(2)
            
            salvar_excel = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_SALVAREXCEL_SOFISA))
            )
            salvar_excel.click()
            driver.switch_to.default_content()
            time.sleep(2)
            
            li_sair = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_LI_SAIR_SOFISA))
            )
            driver.execute_script("arguments[0].click();", li_sair)
            
            btn_sair = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_SAIR_SOFISA))
            )
            driver.execute_script("arguments[0].click();", btn_sair)
            
        except Exception as e:
            raise Exception(f"Erro ao baixar extrato sofisa matriz: {e}")