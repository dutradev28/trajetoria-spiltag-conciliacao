from src.components.loginComponents.create_webdriver import CreateWebdriver
from src.components.loginComponents import LoginBradesco
from src.components.loginComponents import LoginSofisa
from src.components.loginComponents import LoginPagBank
from src.components.loginComponents import LoginBB


def main():
    try:
        webdriver = CreateWebdriver()
        login_bb = LoginBB()
        login_bradesco = LoginBradesco()
        login_sofisa = LoginSofisa()
        login_pagbank = LoginPagBank()
        
        driver = webdriver.create_driver()
        print("Chrome iniciado com sucesso")
        
        login_bb.login_bb(driver)
        login_bradesco.login_bradesco(driver)
        login_sofisa.login_sofisa_matriz(driver)
        login_pagbank.login_pagbank(driver)
        
        print("Login realizado com sucesso!")
        
    except Exception as e:
        raise Exception(f"Erro ao executar rpa: {e}")
    
if __name__ == "__main__":
    main()
