from behave import *
import requests
import json

### SUMAR ###
@given('a {valorUno} {valorDos} a sumar')
def step_impl(context, valorUno, valorDos):
    context.api_url = 'http://localhost:4000/sumar'
    context.request_body = { "numeroUno": valorUno, "numeroDos": valorDos}
    context.headers = {'Accept': 'application/json'}
    print('url :'+context.api_url)

@when('el resultado suma los valores')
def step_impl(context):
    response = requests.post(url=context.api_url, headers=context.headers, json=context.request_body)
    context.response_body = response.json()
    print(context.response_body['Resultado']['resultado'])
    context.sumando = context.response_body['Resultado']['resultado']

@then('el {resultado} de los valores es correcto')
def step_impl(context, resultado):
	print(resultado)
	print(context.sumando)
	assert (context.sumando == int(resultado))
    
### RESTAR  ###
@given('a {valorUno} {valorDos} a restar')
def step_impl(context, valorUno, valorDos):
    context.api_url = 'http://localhost:4000/restar'
    context.request_body = { "numeroUno": valorUno, "numeroDos": valorDos}
    context.headers = {'Accept': 'application/json'}
    print('url :'+context.api_url)

@when('el resultado restar los valores')
def step_impl(context):
    response = requests.post(url=context.api_url, headers=context.headers, json=context.request_body)
    context.response_body = response.json()
    print(context.response_body['Resultado']['resultado'])
    context.restando = context.response_body['Resultado']['resultado']

@then('el {resultado} de la resta es correcto')
def step_impl(context, resultado):
	print(resultado)
	print(context.restando)
	assert (context.restando == int(resultado))

### MULTIPLICAR  ###

@given('a {valorUno} {valorDos} a multiplicar')
def step_impl(context, valorUno, valorDos):
    context.api_url = 'http://localhost:4000/multiplicar'
    context.request_body = { "numeroUno": valorUno, "numeroDos": valorDos}
    context.headers = {'Accept': 'application/json'}
    print('url :'+context.api_url)

@when('el resultado multiplicar los valores')
def step_impl(context):
    response = requests.post(url=context.api_url, headers=context.headers, json=context.request_body)
    context.response_body = response.json()
    print(context.response_body['Resultado']['resultado'])
    context.multiplicando = context.response_body['Resultado']['resultado']

@then('el {resultado} de la multiplicacion es correcto')
def step_impl(context, resultado):
	print(resultado)
	print(context.multiplicando)
	assert (context.multiplicando == int(resultado))

### DIVIDIR  ###

@given('a {valorUno} {valorDos} a dividir')
def step_impl(context, valorUno, valorDos):
    context.api_url = 'http://localhost:4000/dividir'
    context.request_body = { "numeroUno": valorUno, "numeroDos": valorDos}
    context.headers = {'Accept': 'application/json'}
    print('url :'+context.api_url)

@when('el resultado dividir los valores')
def step_impl(context):
    response = requests.post(url=context.api_url, headers=context.headers, json=context.request_body)
    context.response_body = response.json()
    print(context.response_body['Resultado']['resultado'])
    context.dividiendo = context.response_body['Resultado']['resultado']

@then('el {resultado} de la division es correcto')
def step_impl(context, resultado):
	print(resultado)
	print(context.dividiendo)
	assert (context.dividiendo == int(resultado))
