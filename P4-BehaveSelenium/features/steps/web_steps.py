# -- FILE: features/steps/web_steps.py
import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('La web de prestamos')
def step_impl(context):
    context.driver.get(context.base_url)
    assert "Gábilos - Calcular el tiempo que necesitamos para devolver un préstamo" in context.driver.title


@when(u'ingreso {monto} en puedo pagar')
def step_impl(context, monto):
    puedo_pagar = context.driver.find_element(By.ID, "p4D6")
    context.driver.execute_script(f'arguments[0].value = "{monto}"', puedo_pagar)
    time.sleep(3)


@when(u'selecciono {periodo} en periodo de pago')
def step_impl(context, periodo):
    temporalidad = context.driver.find_element(By.ID, 'p4E6')
    select_temporalidad = temporalidad.find_element(By.XPATH, f"//option[. = '{periodo}']")
    select_temporalidad.click()

@when('ingreso {importe} en importe del prestamo')
def step_impl(context, importe):
    importe_prestamo = context.driver.find_element(By.ID, 'p4D7')
    context.driver.execute_script(f"arguments[0].value = '{importe}'", importe_prestamo)
    time.sleep(2)

@when('selecciono {interes} en tipo de interes')
def step_impl(context, interes):
    tipo_interes = context.driver.find_element(By.ID, 'p4D8')
    context.driver.execute_script(f"arguments[0].value = '{interes}'", tipo_interes)
    time.sleep(2)
    distract = context.driver.find_element(By.CLASS_NAME, 'ee132')
    distract.click()
    time.sleep(2)

@when('pulso en limpiar formulario')
def step_impl(context):
    boton_limpiar = context.driver.find_element(By.NAME, "button")
    boton_limpiar.click()

@then('muestra tiempo necesario de {anos} anos y {meses} meses')
def step_impl(context, anos, meses):
    distract = context.driver.find_element(By.CLASS_NAME, 'ee132')
    distract.click()
    element1 = context.driver.find_element(By.ID, "p4D12")
    element2 = context.driver.find_element(By.ID, "p4D13")

    anos_encontrados = element1.get_attribute("value")
    meses_encontrados = element2.get_attribute("value")

    print("found value: " + anos_encontrados)

    assert anos_encontrados == anos, f"Esperado: {anos}, encontrado: {anos_encontrados}"
    assert meses_encontrados == meses, f"Esperado: {meses}, encontrado: {meses_encontrados}"

@then('muestra tiempo necesario de {anos} anos')
def step_impl(context, anos):
    distract = context.driver.find_element(By.CLASS_NAME, 'ee132')
    distract.click()
    element1 = context.driver.find_element(By.ID, "p4D12")

    anos_encontrados = element1.get_attribute("value")

    assert anos_encontrados == anos, f"Esperado: {anos}, encontrado: {anos_encontrados}"


@then('muestra ERROR')
def step_impl(context):
    tiempo_necesario_anos = context.driver.find_element(By.ID, 'p4D12')
    tiempo_necesario_meses = context.driver.find_element(By.ID, 'p4D13')

    anos_encontrados = tiempo_necesario_anos.get_attribute("value")
    meses_encontrados = tiempo_necesario_meses.get_attribute("value")


    assert anos_encontrados == "ERROR", f"Esperado: ERROR, encontrado: {anos_encontrados}"
    assert meses_encontrados == "ERROR", f"Esperado: ERROR, encontrado: {meses_encontrados}"