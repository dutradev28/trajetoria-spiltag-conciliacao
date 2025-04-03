from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class ExtractBradesco:
    
    def __init__(self):
        try:
            load_dotenv()
            self.CSS_OVERLAY_BRADESCO = os.getenv("CSS_OVERLAY_BRADESCO")
            self.CSS_EXTRATO_BRADESCO = os.getenv("CSS_EXTRATO_BRADESCO")
            self.CSS_IFRAME_EXTRATO = os.getenv("CSS_IFRAME_EXTRATO")
            self.CSS_ULTIMOS_LANCAMENTOS_BRADESCO = os.getenv("CSS_ULTIMOS_LANCAMENTOS_BRADESCO")
            self.CSS_IFRAME_EXTRATO_1 = os.getenv("CSS_IFRAME_EXTRATO_1")
            self.CSS_ULTIMOS30_DIAS_BRADESCO = os.getenv("CSS_ULTIMOS30_DIAS_BRADESCO")
            self.CSS_CONTACORRENTE_BRADESCO = os.getenv("CSS_CONTACORRENTE_BRADESCO")
            self.CSS_SALVAR_ARQUIVO = os.getenv("CSS_SALVAR_ARQUIVO")
            self.CSS_IFRAME_ARQUIVO = os.getenv("CSS_IFRAME_ARQUIVO")
            self.CSS_IFRAME_PDF = os.getenv("CSS_IFRAME_PDF")
            
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo .env {e}")
        
    def extract_bradesco(self, driver):
        try:
            
            try:
                overlay = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_OVERLAY_BRADESCO))
                )
                if overlay.is_displayed():
                    overlay.click()
            except:
                pass  
            saldos_extratos = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_EXTRATO_BRADESCO))
            )
            saldos_extratos.click()
            
            WebDriverWait(driver, 30).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, self.CSS_IFRAME_EXTRATO))
            )
                        
            ultimos_lancammentos = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_ULTIMOS_LANCAMENTOS_BRADESCO))
            )
            ultimos_lancammentos.click()
            driver.switch_to.default_content()
            
            WebDriverWait(driver, 30).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, self.CSS_IFRAME_EXTRATO_1))
            )
            
            ultimos_30_dias = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_ULTIMOS30_DIAS_BRADESCO))
            )
            ultimos_30_dias.click()
            time.sleep(2)
            conta = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_CONTACORRENTE_BRADESCO))
            )
            conta.click()
            time.sleep(2)
            salvar_arquivo = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_SALVAR_ARQUIVO))
            )
            salvar_arquivo.click()
            driver.switch_to.default_content()
            time.sleep(3)
            
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, self.CSS_IFRAME_ARQUIVO))
            )
            pdf = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.CSS_IFRAME_PDF))
            )
            pdf.click()
            driver.switch_to.default_content()
            time.sleep(3)
            
        except Exception as e:
            raise Exception(f"Erro ao baixar extrato bancario bradesco: {e}")