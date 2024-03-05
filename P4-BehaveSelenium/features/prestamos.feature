# -- FILE: features/example.feature

Feature: Calcular prestamo
        
    Scenario: Calcular el tiempo con interes negativo
        Given La web de prestamos
        When ingreso 750 en puedo pagar
        And ingreso 15.000,00 en importe del prestamo
        And selecciono -2,00% en tipo de interes
        And selecciono mensual en periodo de pago
        Then muestra tiempo necesario de 1,64 anos y 19,66 meses

    Scenario: Calcular el tiempo con interes positivo
        Given La web de prestamos
        When ingreso 750 en puedo pagar
        And selecciono mensual en periodo de pago
        And ingreso 15000 en importe del prestamo
        And selecciono 2 en tipo de interes
        Then muestra tiempo necesario de 1,15 anos y 13,83 meses

    Scenario: Limpiar Formulario
        Given La web de prestamos
        When ingreso 750 en puedo pagar
        And selecciono mensual en periodo de pago
        And ingreso 15000 en importe del prestamo
        And selecciono -2 en tipo de interes
        And pulso en limpiar formulario
        Then muestra tiempo necesario de 0 anos

    Scenario: Importe menor a cuota
        Given La web de prestamos
        When ingreso 750 en puedo pagar
        And selecciono mensual en periodo de pago
        And ingreso 15000 en importe del prestamo
        And selecciono 2 en tipo de interes
        Then muestra ERROR

        Scenario: Probar error strings
        Given La web de prestamos
        When ingreso asdf en puedo pagar
        And selecciono mensual en periodo de pago
        And ingreso 15000 en importe del prestamo
        And selecciono -2 en tipo de interes
        Then muestra ERROR

    Scenario: Prueba de stress
        Given La web de prestamos
        When ingreso 12.341.234,00 en puedo pagar
        And selecciono mensual en periodo de pago
        And ingreso 123.412.341.234.1234,00 en importe del prestamo
        And selecciono -2,00% en tipo de interes
        Then muestra tiempo necesario de 143,46 anos y 1721,57 meses


