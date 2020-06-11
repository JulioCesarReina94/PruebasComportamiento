Feature: Calculadora

Scenario Outline: Obtener sumatoria
  Given a <valorUno> <valorDos> a sumar
  When el resultado suma los valores
  Then el <resultado> de los valores es correcto

  Examples: names
  | valorUno | valorDos | resultado |
  | 3        | 10       | 13        |
  | 8        | 23       | 31        |

Scenario Outline: Obtener restar
  Given a <valorUno> <valorDos> a restar
  When el resultado restar los valores
  Then el <resultado> de la resta es correcto

  Examples: names
  | valorUno | valorDos | resultado|
  | 5        | 3        | 2        |
  | 10       | 5        | 5        |
  | 100      | 20       | 80       |
  | 60       | 30       | 30       |

Scenario Outline: Obtener multiplicacion
  Given a <valorUno> <valorDos> a multiplicar
  When el resultado multiplicar los valores
  Then el <resultado> de la multiplicacion es correcto

  Examples: names
  | valorUno | valorDos | resultado|
  | 5        | 2        | 10       |
  | 10       | 5        | 50       |
       
 Scenario Outline: Obtener division
  Given a <valorUno> <valorDos> a dividir
  When el resultado dividir los valores
  Then el <resultado> de la division es correcto

  Examples: names
  | valorUno | valorDos | resultado|
  | 10       | 2        | 5       |
  | 200      | 4        | 50      |   
