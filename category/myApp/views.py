from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.db import connection

sqlStatements = []
with open('myApp/_SQLs', 'r', encoding='utf-8') as readSqlCursor:
    sqlStatement = readSqlCursor.readlines()

a_line = ""

for line in sqlStatement:
    a_line += line
sqlStatements = a_line.split('#')

def index(request):
    return render(request, 'myApp/main.html')


def createTable(request):
    createStatements = []
    with open('myApp/_createTable', 'r', encoding='utf-8') as readSqlCursor:
        createStatements = readSqlCursor.readlines()

    a_line = ""

    for line in createStatements:
        a_line += line
    statements = a_line.split('#')

    with connection.cursor() as cursor:
        for statement in statements:
            cursor.execute(statement)
    return render(request, 'myApp/main.html')

def insertData(request):
    insertStatements = []
    with open('myApp/_insertData', 'r', encoding='utf-8') as readSqlCursor:
        insertStatements = readSqlCursor.readlines()

    a_line = ""

    for line in insertStatements:
        a_line += line
    statements = a_line.split("#")

    with connection.cursor() as cursor:
        for statement in statements:
            cursor.execute(statement)
    return render(request, 'myApp/main.html')


def select1(request):
    outputRecords = []
    print(sqlStatements[0])
    with connection.cursor() as cursor:
        cursor.execute(sqlStatements[0])
        fetchResultCategories = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultCategories:
            eachRow = {'diskSize': temp[0]}
            outputRecords.append(eachRow)

    return render(request, 'myApp/main.html', {"select1": outputRecords})


def select2(request):
    outputRecords = []
    print(sqlStatements[1])
    with connection.cursor() as cursor:
        cursor.execute(sqlStatements[1])
        fetchResultCategories = cursor.fetchall()

        print(fetchResultCategories)

        connection.commit()
        connection.close()

        for temp in fetchResultCategories:
            eachRow = {'maker': temp[0], 'averageSpeed': temp[1]}
            outputRecords.append(eachRow)

    return render(request, 'myApp/main.html', {"select2": outputRecords})


def select3(request):
    outputRecords = []
    print(sqlStatements[2])
    with connection.cursor() as cursor:
        cursor.execute(sqlStatements[2])
        fetchResultCategories = cursor.fetchall()

        print(fetchResultCategories)

        connection.commit()
        connection.close()

        for temp in fetchResultCategories:
            eachRow = {'price': temp[0]}
            outputRecords.append(eachRow)

    return render(request, 'myApp/main.html', {"select3": outputRecords})


def select4(request):
    outputRecords = []
    print(sqlStatements[3])
    with connection.cursor() as cursor:
        cursor.execute(sqlStatements[3])
        fetchResultCategories = cursor.fetchall()

        print(fetchResultCategories)

        connection.commit()
        connection.close()

        for temp in fetchResultCategories:
            eachRow = {'model': temp[0], 'price': temp[1]}
            outputRecords.append(eachRow)

    return render(request, 'myApp/main.html', {"select4": outputRecords})


# def display(request):
#     outputCategories = []
#     outputOfQuery1 = []
#     with connection.cursor() as cursor:
#         sqlQueryCategories = "SELECT model, screen, price FROM Laptop;"
#         cursor.execute(sqlQueryCategories)
#         fetchResultCategories = cursor.fetchall()
#
#         sqlQuery1 = "SELECT model, type FROM Printer WHERE price>100;"
#         cursor.execute(sqlQuery1)
#         fetchResultQuery1 = cursor.fetchall()
#
#         connection.commit()
#         connection.close()
#
#         for temp in fetchResultCategories:
#             eachRow = {'model': temp[0], 'screen': temp[1], 'price': temp[2]}
#             outputCategories.append(eachRow)
#
#         for temp in fetchResultQuery1:
#             eachRow = {'model': temp[0], 'type': temp[1]}
#             outputOfQuery1.append(eachRow)
#
#     return render(request, 'myApp/index.html', {"categories": outputCategories, "output1": outputOfQuery1})
#
#
# from .forms import CategoriesForm
#
#
# def inputData(request):
#     if request.method == "POST":
#         form = CategoriesForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CategoriesForm()
#     return render(request, "myApp/input.html", {'form': form})
