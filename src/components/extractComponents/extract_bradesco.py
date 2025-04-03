from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
import time
import shutil


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
            downloaded_file = self.move_and_rename_bradesco_file()
        
            print(f"Extrato processado: {downloaded_file}")
            
        except Exception as e:
            raise Exception(f"Erro ao baixar extrato bancario bradesco: {e}")
        
    def move_and_rename_bradesco_file(self):
    
        try:
            download_dir = os.path.expanduser("~/Downloads")  
            output_dir = os.path.join("src", "outputs")
        
            os.makedirs(output_dir, exist_ok=True)
            
            file_pattern = "Bradesco_"
            
            matching_files = [f for f in os.listdir(download_dir) 
                            if f.startswith(file_pattern) and f.lower().endswith('.pdf')]
            
            if not matching_files:
                raise FileNotFoundError("Nenhum arquivo do Bradesco encontrado na pasta de downloads")
        
            matching_files.sort(key=lambda f: os.path.getmtime(os.path.join(download_dir, f)), 
                            reverse=True)
            
            latest_file = matching_files[0]
            original_path = os.path.join(download_dir, latest_file)
        
            file_size = -1
            while True:
                try:
                    current_size = os.path.getsize(original_path)
                    if current_size == file_size:
                        break  
                    file_size = current_size
                    time.sleep(1)
                except OSError:
                    time.sleep(1)
                    continue
            
            current_month_year = datetime.now().strftime("%m%Y")
            new_filename = f"BRADESCO_{current_month_year}.pdf"
            new_path = os.path.join(output_dir, new_filename)
            
            counter = 1
            while os.path.exists(new_path):
                new_filename = f"BRADESCO_{current_month_year}_{counter}.pdf"
                new_path = os.path.join(output_dir, new_filename)
                counter += 1
            
            shutil.move(original_path, new_path)
            
            print(f"Arquivo movido e renomeado com sucesso: {new_path}")
            return new_path
            
        except Exception as e:
            raise Exception(f"Erro ao mover/renomear arquivo do Bradesco: {str(e)}")