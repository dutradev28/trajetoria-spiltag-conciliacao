from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ExtractBradesco:
    
    def __init__(self):
        try:
            load_dotenv()
            self.XPATH_EXTRATO_BRADESCO = os.getenv("XPATH_EXTRATO_BRADESCO")
            self.XPATH_ULTIMOS_LANCAMENTOS_BRADESCO = os.getenv("XPATH_ULTIMOS_LANCAMENTOS_BRADESCO")
            self.XPATH_ULTIMOS30_DIAS_BRADESCO = os.getenv("XPATH_ULTIMOS30_DIAS_BRADESCO")
            self.XPATH_CONTACORRENTE_BRADESCO = os.getenv("XPATH_CONTACORRENTE_BRADESCO")
            self.XPATH_SALVAR_ARQUIVO = os.getenv("XPATH_SALVAR_ARQUIVO")
            self.XPATH_IFRAME_ARQUIVO = os.getenv("XPATH_IFRAME_ARQUIVO")
            self.XPATH_IFRAME_PDF = os.getenv("XPATH_IFRAME_PDF")
            
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo .env {e}")
        
    def extract_bradesco(self, driver):
        try:
            saldos_extratos = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_EXTRATO_BRADESCO))
            )
            saldos_extratos.click()
            
            ultimos_lancammentos = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_ULTIMOS_LANCAMENTOS_BRADESCO))
            )
            ultimos_lancammentos.click()
            
            ultimos_30_dias = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_ULTIMOS30_DIAS_BRADESCO))
            )
            ultimos_30_dias.click()
            
            conta = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_CONTACORRENTE_BRADESCO))
            )
            conta.click()
            
            salvar_arquivo = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_SALVAR_ARQUIVO))
            )
            salvar_arquivo.click()
            
            WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.XPATH_IFRAME_ARQUIVO))
            )
            pdf = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH_IFRAME_PDF))
            )
            pdf.click()
            
        except Exception as e:
            raise Exception(f"Erro ao baixar extrato bancario bradesco: {e}")