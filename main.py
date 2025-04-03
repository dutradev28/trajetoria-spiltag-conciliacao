from src.components.loginComponents.create_webdriver import CreateWebdriver
from src.components.loginComponents.login_bradesco import LoginBradesco
from src.components.loginComponents.login_sofisa import LoginSofisa
from src.components.loginComponents.login_pagbank import LoginPagBank
from src.components.loginComponents.login_bb import LoginBB
from src.components.extractComponents.extract_bradesco import ExtractBradesco


def main():
    try:
        webdriver = CreateWebdriver()
        login_bb = LoginBB()
        login_bradesco = LoginBradesco()
        login_sofisa = LoginSofisa()
        login_pagbank = LoginPagBank()
        extract_bradesco = ExtractBradesco()
        
        driver = webdriver.create_driver()
        print("Chrome iniciado com sucesso")
        
        #login_bb.login_bb(driver)
        login_bradesco.login_bradesco(driver)
        #login_sofisa.login_sofisa_matriz(driver)
        #login_pagbank.login_pagbank(driver)
        
        extract_bradesco.extract_bradesco(driver)
        
        
        print("Login realizado com sucesso!")
        
    except Exception as e:
        raise Exception(f"Erro ao executar rpa: {e}")
    
if __name__ == "__main__":
    main()
