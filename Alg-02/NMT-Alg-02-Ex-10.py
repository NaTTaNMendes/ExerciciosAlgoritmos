matricula = int(input("Informe a matrícula (AASDDD): "))

dezenaAno = matricula // 100000
matricula = matricula - (dezenaAno * 100000)

unidadeAno = matricula // 10000
matricula = matricula - (unidadeAno * 10000)

semestre = matricula // 1000

ano = (dezenaAno * 10) + unidadeAno

print("Ano de matrícula:",ano,"\nSemestre:",semestre)