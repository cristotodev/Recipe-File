from os import system, listdir, mkdir, rmdir, remove
from pathlib import Path
import glob

RECIPE_EXTENSION = ".txt"
print("Bienvenido a tu Recetario")
work_directory = Path(__file__).parent.resolve()

def total_get_recipes():
    pattern = str(work_directory) + "/**/*" + RECIPE_EXTENSION
    return len(glob.glob(pattern, recursive=True))

def get_categories():
    return listdir(work_directory / "recetas")

def get_recipes(category):
    recipes = listdir(work_directory / "recetas" / category)
    return [str(recipe).replace(RECIPE_EXTENSION, "") for recipe in recipes]

def recipe_content(category, recipe):
    file = open(work_directory / "recetas" / category / recipe, "r")
    content = file.read()
    file.close()
    return content

def select_category(categories):
    for index, category in enumerate(categories):
        print(f"{index+1}: {category}")
            
    categorySelected = -1
    while categorySelected < 0 or categorySelected > len(categories):
        categorySelected = int(input("Seleccione el número de una categoría: "))
        categorySelected -= 1

    return categorySelected

def select_recipe(recipes):
    for index, recipe in enumerate(recipes):
        print(f"{index+1}: {recipe}")
            
    recipeSelected = -1
    while recipeSelected < 0 or recipeSelected > len(recipes):
        recipeSelected = int(input("Seleccione el número de una receta: "))
        recipeSelected -= 1
    
    return recipeSelected

def create_category(new_category):
    mkdir(work_directory / "recetas" / new_category)

def delete_category(category):
    opcion = ""
    while not (opcion.lower() == "n" or opcion.lower() == "y"):
        opcion = input("Esta acción eliminará todas las recetas de la categoría. ¿Estás seguro? (y/n)")
    
    if opcion == "n":
        print("Se ha cancelado la eliminación")
        return
    
    rmdir(work_directory / "recetas" / category)

def create_recipe(category, recipe, content):
    recipe += RECIPE_EXTENSION
    file = open(work_directory / "recetas" / category / recipe, "w")
    file.write(content)
    file.close()

def remove_recipe(category, recipe):
    recipe += RECIPE_EXTENSION
    opcion = ""
    while not (opcion.lower() == "n" or opcion.lower() == "y"):
        opcion = input("Esta acción eliminará la receta. ¿Estás seguro? (y/n)")
    
    if opcion == "n":
        print("Se ha cancelado la eliminación")
        return
    
    remove(work_directory / "recetas" / category / recipe)


print(f"La carpeta de recetas es: {work_directory}")
while True :
    print(f"Total de recetas: {total_get_recipes()}")
    print("Opción 1: Leer una receta")
    print("Opción 2: Crear una nueva receta")
    print("Opción 3: Crear una categoría")
    print("Opción 4: Eliminar una receta")
    print("Opción 5: Eliminar una categoría")
    print("Opción 6: Salir de la aplicación")

    optionSelected = int(input("Eliga una opción: "))

    system("cls")
    match optionSelected:
        case 1:
            categories = get_categories()
            print("Categorías")
            print("--------------------")
            
            categorySelected = select_category(categories)

            print(f"Recetas de la categoría {categories[categorySelected]}")
            print("--------------------")
            
            recipes = get_recipes(categories[categorySelected])
            recipeSelected = select_recipe(recipes)

            print(f"Las instrucciones de la receta {recipes[recipeSelected]} son:")
            print(recipe_content(categories[categorySelected], recipes[recipeSelected]+".txt"))

        case 2:
            categories = get_categories()
            print("Categorías")
            print("--------------------")
            
            categorySelected = select_category(categories)

            recipe_name = input("Introduzca el nombre de la nueva receta: ")
            content = input("Introduzca los pasos de la receta: ")
            create_recipe(categories[categorySelected], recipe_name, content)

        case 3:
            new_category = input("Introduce el nombre de la nueva categoría: ")
            create_category(new_category)

        case 4:
            categories = get_categories()
            print("Categorías")
            print("--------------------")
            
            categorySelected = select_category(categories)

            print(f"Recetas de la categoría {categories[categorySelected]}")
            print("--------------------")
            
            recipes = get_recipes(categories[categorySelected])
            recipeSelected = select_recipe(recipes)

            remove_recipe(categories[categorySelected], recipes[recipeSelected])

        case 5:
            categories = get_categories()
            print("Categorías")
            print("--------------------")
            categorySelected = select_category(categories)

            delete_category(categories[categorySelected])
        case 6:
            print("Adiós")
            break
    
    print("--------------------")