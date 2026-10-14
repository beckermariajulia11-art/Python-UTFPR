
"""CT-002: rejeição de credenciais inválidas."""
# pylint: disable=not-callable,duplicate-code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    usuario = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    usuario.send_keys("usuario_invalido")

    senha = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    senha.send_keys("senha_errada")

    botao = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type=submit]")
        )
    )
    botao.click()

    mensagem = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your username is invalid!" in mensagem
    assert driver.current_url.endswith("/login")

    driver.save_screenshot("ct002.png")
    print("CT-002 APROVADO:", mensagem)
    print("URL:", driver.current_url)

finally:
    driver.quit()
