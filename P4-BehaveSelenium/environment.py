"""
Environment for Behave Testing
"""
from os import getenv
from selenium import webdriver

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))
BASE_URL = getenv('BASE_URL', 'https://www.gabilos.com/calculadoras/rentasconstantes/tiempo_para_devolver_prestamo.htm')


def before_all(context):
    """ Executed once before all tests """
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    # Instantiate the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox") # Bypass OS security model
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(context.wait_seconds)
    
    
def after_all(context):
    """ Executed after all tests """
    context.driver.quit()