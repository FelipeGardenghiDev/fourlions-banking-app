#Declaração de Variáveis
saldo = 0;
saldo_destino = 0;
usuario_destino = 'nome_qualquer';
variavel_auxiliar = 0;

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
    print('Olá, usuário! Qual operação deseja fazer hoje? (depositar, checar saldo, transferência, sair)');
  elif(categoria == '2'):
    print('Olá, lojista! Qual operação deseja fazer hoje? (depositar, checar saldo, transferência, sair)');

  operacao = str(input());

  #Operação de Depósito
  if (operacao == 'depositar'):
    print('Por favor, informe qual o valor a ser depositado na sua conta:');
    saldo += int(input());
    print('Valor depositado com sucesso! Seu saldo atual é de R$' + str(saldo));
  
  #Operação de Checagem de Saldo
  elif (operacao == 'checar saldo' or operacao == 'saldo'):
    print('Seu saldo atual é de R$' + str(saldo));
  
  #Operação de Transferência
  elif (operacao == 'transferência' or operacao == 'transferencia' or operacao == 'transferir'):
    if categoria == 2: #Caso o user for Lojista
      print('Desculpe, lojistas não têm permissão para realizar transferências, somente receber de outros usuários.');
    else:
      print('Para quem você deseja transferir?');
      usuario_destino = str(input());
      print('Qual valor você deseja transferir para ' + usuario_destino + '?');
      variavel_auxiliar = int(input());
      if variavel_auxiliar > saldo:
        print('Desculpe, você não tem saldo suficiente para realizar essa transferência!');
      else:
        saldo_destino += variavel_auxiliar;
        saldo -= variavel_auxiliar;
        print('Sua transferência foi realizada com sucesso!');
        print('Seu saldo é de R$' + str(saldo));
        print('O saldo de ' + usuario_destino + ' é de R$' + str(saldo_destino));
  
  #Operação de saída do App
  elif (operacao == 'sair'):
    print('Obrigado por utilizar nosso App! Até breve =)');
    break;
  
  #Caso a operação escolhida for inválida
  else:
    print('Não entendi. Por favor selecione uma operação válida!');

