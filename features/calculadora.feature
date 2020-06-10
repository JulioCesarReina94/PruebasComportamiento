Feature: Calculadora

Scenario Outline: Obtener sumatoria
  Given a <valorUno> <valorDos> a sumar
  When el resultado suma los valores
  Then el <resultado> de los valores es correcto

  Examples: names
  | valorUno | valorDos | resultado |
  | 3        | 10       | 13        |
  | 8        | 23       | 31        |
          