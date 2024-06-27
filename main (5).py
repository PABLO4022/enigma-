codigo = "6550126 MMR"

def mensagem(codigo):
  dicionario = {
      '6': 'F',
      '5': 'e',
      '50': 'l',
      '1': 'i',
      '26': 'z',
      'MM': '2000',
      'R': '18'
  }
  mensagem = ''.join(dicionario[digit] for digit in ['6', '5', '50', '1','26'])
    
  soma = dicionario['MM'][:2] + dicionario['R'] 
  mensagem += ' ' + soma
  return mensagem 

mensagem = mensagem(codigo)

print("Mensagem codificada:", codigo)
print("Mensagem decodificada:", mensagem)