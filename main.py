from Funciones_Notas import *

while True:
    student = readstudents()

    while True:
        op = ChooseOp()

        if op == 1:
            registerGrade()

        elif op == 2:
            if len(grades) > 0:
                print("\nEstudiante:", student)
                showGrades()
                break
            else:
                print("Debe registrar al menos una calificacion.")

    answer = input("\n¿Desea registrar otro estudiante? (s/n): ")

    if answer.lower() == "n":
        print("\nGracias por utilizar el programa.")
        break