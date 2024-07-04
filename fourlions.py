#Declaração de Variáveis
saldo = 0;
saldo_destino = 0;
usuario_destino = 'nome_qualquer';
variavel_auxiliar = 0;

#Funções do App
def checar_saldo():
  print(f'Seu saldo atual é de R${saldo:,.2f}');

def deposita_valor():
  global saldo;

  print('Por favor, informe qual o valor a ser depositado na sua conta:');
  saldo += float(input());
  print(f'Valor depositado com sucesso! Seu saldo atual é de R${saldo:,.2f}');

def transfere_valor(categoria):
  global saldo, saldo_destino, variavel_auxiliar, usuario_destino;

  if categoria == '2': #Caso o user for "Lojista"
      print('Desculpe, lojistas não têm permissão para realizar transferências, somente receber de outros usuários.');
  else: #Caso o user for "Usuário"
    print('Para quem você deseja transferir?');
    usuario_destino = str(input());
    print(f'Qual valor você deseja transferir para {usuario_destino}?');
    try:
      variavel_auxiliar = float(input());
    except ValueError:
      print('Valor inválido! Operação encerrada.');
      return;
    if variavel_auxiliar > saldo:
      print('Desculpe, você não tem saldo suficiente para realizar essa transferência!');
    else:
      saldo_destino += variavel_auxiliar;
      saldo -= variavel_auxiliar;
      print('Sua transferência foi realizada com sucesso!');
      print(f'Seu saldo é de R${saldo}');
      print(f'O saldo de {usuario_destino} é de R${saldo_destino}');

def sair_do_app():
  print('Obrigado por utilizar nosso App! Até breve =)');

#Inicialização da Interface
print('##########################################');
print('# Bem-vindo(a) ao FourLions Banking App! #');
print('##########################################');
print('Por gentileza informe se você é (1) Usuário ou (2) Lojista:');


categoria = str(input());


#Garantindo que o usuário pertença a uma categoria válida ("Usuário" ou "Lojista")
while categoria != '1' and categoria != '2':
  print('Por gentileza, selecione uma opção válida: (1) Usuário ou (2) Lojista');
  categoria = str(input());

#Loop de utilização da interface
while 1: 
  if(categoria == '1'):
    print('Olá, usuário! Qual operação deseja fazer hoje? (checar saldo, depositar, transferência, sair)');
  elif(categoria == '2'):
    print('Olá, lojista! Qual operação deseja fazer hoje? (checar saldo, depositar, transferência, sair)');

  operacao = str(input());

  #Operação de Checagem de Saldo
  if (operacao == 'checar saldo' or operacao == 'saldo'):
    checar_saldo();
  
  #Operação de Depósito
  elif (operacao == 'depositar' or operacao == 'deposito' or operacao == 'depósito'):
    deposita_valor();
  
  #Operação de Transferência
  elif (operacao == 'transferência' or operacao == 'transferencia' or operacao == 'transferir'):
    transfere_valor(categoria);
  
  #Operação de saída do App
  elif (operacao == 'sair'):
    sair_do_app();
    break;
  
  #Caso a operação escolhida for inválida
  else:
    print('Desculpe, não entendi. Por favor selecione uma operação válida!');

