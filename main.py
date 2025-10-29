def calcular_media(notas):
  if len(notas) == 0:
      return 0
  return sum(notas) / len(notas)

def obter_notas_aluno():
  notas = []
  while True:
      try:
        
          nota = float(input("Digite uma nota (ou -1 para encerrar): "))
          if nota == -1:
              break
          if 0 <= nota <= 10:
              notas.append(nota)
          else:
              print("Por favor, digite uma nota entre 0 e 10.")
      except ValueError:
          print("Por favor, digite um número válido.")

  return notas

def main():
  print("Sistema de Notas Escolares")

  numero_alunos = int(input("Digite o número de alunos: "))

  for i in range(1, numero_alunos + 1):
      print(f"\nAluno {i}:")
      notas_aluno = obter_notas_aluno()

      media_aluno = calcular_media(notas_aluno)
      print(f"A média do Aluno {i} é: {media_aluno:.2f}\n")

if __name__ == "__main__":
  main()
