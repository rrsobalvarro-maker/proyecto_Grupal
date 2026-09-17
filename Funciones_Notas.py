Classes = []
grades = []


def readstudents():
    name = input("Ingrese el nombre del estudiante: ")
    return name


def ChooseOp():
    print("\n--- REGISTRO DE ESTUDIANTES ---")
    print("1. Registrar asignatura y nota")
    print("2. Ver resultados y cerrar el programa")

    while True:
        try:
            op = int(input("Seleccione una opcion: "))

            if op == 1 or op == 2:
                return op
            else:
                print("Ingrese una opcion entre 1 y 2.")

        except ValueError:
            print("Ingrese un valor numerico.")


def registerGrade():
    Class = input("Ingrese el nombre de la asignatura: ")

    while True:
        try:
            grade = float(input("Ingrese su calificacion: "))

            if grade >= 0 and grade <= 100:
                Classes.append(Class)
                grades.append(grade)
                print("Nota registrada correctamente.")
                break
            else:
                print("La calificacion debe ser entre 0 y 100.")

        except ValueError:
            print("Debe ingresar un valor numerico.")


def showGrades():
    print("\n--- RESULTADOS DEL ESTUDIANTE ---")

    for Class, grade in zip(Classes, grades):
        print(Class, "-", grade)