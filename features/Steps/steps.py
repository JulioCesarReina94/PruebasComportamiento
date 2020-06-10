from behave import *
import requests
import json


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
    context.saludo = context.response_body['Resultado']['resultado']

@then('el {resultado} de los valores es correcto')
def step_impl(context, resultado):
	print(resultado)
	print(context.saludo)
	assert (context.saludo == int(resultado))
    
