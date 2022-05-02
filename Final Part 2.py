from tkinter import *
from tkinter import messagebox
from tkinter import font

import mysql.connector as mysql


def connectUser():
    userName = Entry(main, width=30, bg='#FFF0F5')
    userName['font'] = fontt
    userName.grid(row=0, column=1, padx=20, pady=(10, 0))
    userPass = Entry(main, width=30, bg='#FFF0F5')
    userPass['font'] = fontt
    userPass.grid(row=1, column=1)

    userNameLabel = Label(main, text="First Name", bg='#FFF0F5')
    userNameLabel['font'] = fontt
    userNameLabel.grid(row=0, column=0, pady=(10, 0))
    userPassLabel = Label(main, text="Password", bg='#FFF0F5')
    userPassLabel['font'] = fontt
    userPassLabel.grid(row=1, column=0)

    loginButton = Button(main, text="Login", bg='#FFF0F5', command=lambda: login(userName.get(), userPass.get()))
    loginButton['font'] = fontt
    loginButton.grid(row=2, column=1, pady=(10, 0))


def login(userName, userPass):
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM users WHERE userName = '" + userName + "' AND userPass = '" + userPass + "'")
    result = cursor.fetchall()
    if len(result) == 0:
        messagebox.showerror("Error", "Incorrect username or password")
    else:
        messagebox.showinfo("Success", "Welcome " + userName)
        main.withdraw()
        userWin(getUserId(userName))


def userWin(userId):
    newUserWin = Toplevel(main)
    newUserWin.title("Welcome to your account")

    welcomeLabel = Label(newUserWin, text="Welcome to your Recipes", bg='#FFF0F5')
    welcomeLabel['font'] = fontt
    welcomeLabel.grid(row=0, column=0, columnspan=2, pady=(10, 0))

    showRecipesButton = Button(newUserWin, text="Show Recipes", bg='#FFF0F5',
                               command=lambda: showRecipes(newUserWin, userId))
    showRecipesButton['font'] = fontt
    showRecipesButton.grid(row=1, column=0, pady=(10, 0))

    checkRecipesButton = Button(newUserWin, text="Check Recipes", bg='#FFF0F5',
                                command=lambda: checkRecipes(newUserWin, userId))
    checkRecipesButton['font'] = fontt
    checkRecipesButton.grid(row=1, column=1, pady=(10, 0))

    addRecipesButton = Button(newUserWin, text="Add Recipes", bg='#FFF0F5',
                              command=lambda: addRecipes(newUserWin, userId))
    addRecipesButton['font'] = fontt
    addRecipesButton.grid(row=2, column=0, pady=(10, 0))

    newUserWin.mainloop()


def getUserId(userName):
    cursor = dbase.cursor()
    cursor.execute("SELECT userId FROM users WHERE userName = '" + str(userName) + "'")
    result = cursor.fetchall()
    return result[0][0]


def getAllRecipes(userId):
    action.execute("SELECT recipeName FROM recipes where userRecipe = '" + str(userId) + "'")
    rec = action.fetchall()
    recipeList = []
    for recipe in rec:
        recipeList.append(recipe[0])

    return recipeList


def showRecipes(newUserWin, userId):
    shRecipesWin = Toplevel(newUserWin)
    shRecipesWin.title("Your Recipes")

    recipeList = getAllRecipes(userId)
    clicked = StringVar()
    clicked.set(recipeList[0])

    drop = OptionMenu(shRecipesWin, clicked, *recipeList)
    drop.grid(row=0, column=0, pady=(10, 0))

    showRecipeButton = Button(shRecipesWin, text="Show Recipe", bg='#FFF0F5',
                              command=lambda: showRecipe(shRecipesWin, clicked))

    showRecipeButton['font'] = fontt
    showRecipeButton.grid(row=1, column=0, pady=(10, 0))

    shRecipesWin.mainloop()


def showRecipe(shRecipesWin, clicked):
    q = "SELECT * FROM recipes WHERE recipeName = '" + clicked.get() + "'"
    action.execute(q)
    rec = action.fetchall()
    newStr = "Serving size: " + str(rec[0][3]) + "\n" + "Calories: " + str(rec[0][4]) + "\n" + "Ingredients: " + str(
        rec[0][
            2]) + "\n" + "Instructions:\n " + str(rec[0][5]).replace(".", "\n").replace(". ", "\n") + "\n"

    recLabel = Label(shRecipesWin, text=newStr, bg='#FFF0F5', height=50, width=150)
    recLabel['font'] = fontt
    recLabel.grid(row=10, column=0, pady=(10, 0), sticky=N)


def checkRecipes(newUserWin, userId):
    checkRecipesWin = Toplevel(newUserWin)
    checkRecipesWin.title("Look for Recipes")

    recipeSea = Entry(checkRecipesWin, width=30, bg='#FFF0F5')
    recipeSea['font'] = fontt
    recipeSea.grid(row=0, column=0, padx=20, pady=(10, 0))

    recipeSeaLabel = Label(main, text="Enter Recipe Name or approximation:", bg='#FFF0F5')
    recipeSeaLabel['font'] = fontt
    recipeSeaLabel.grid(row=0, column=0, pady=(10, 0))

    searchButton = Button(checkRecipesWin, text="Search", bg='#FFF0F5',
                          command=lambda: searchRecipe(checkRecipesWin, recipeSea.get(), userId))
    searchButton['font'] = fontt
    searchButton.grid(row=1, column=0, columnspan=2, pady=(10, 0))

    checkRecipesWin.mainloop()


def searchRecipe(checkRecipesWin, recipeName,userId):
    q = "SELECT * FROM recipes WHERE recipeName LIKE '%" + recipeName + "%'" + " OR ingredients LIKE '%" + recipeName + "%'""AND userRecipe = '" + str(userId) + "'"
    action.execute(q)
    rec = action.fetchall()
    if len(rec) == 0:
        Label(checkRecipesWin, text="No recipes found", bg='#FFF0F5', height=50, width=150).grid(row=10, column=0,
                                                                                                 pady=(10, 0))
    else:
        recList = []
        for recipe in rec:
            recList.append(recipe[1])
        clicked = StringVar()
        clicked.set(recList[0])

        drop = OptionMenu(checkRecipesWin, clicked, *recList)
        drop.grid(row=2, column=0, pady=(10, 0))

        showRecipeButton = Button(checkRecipesWin, text="Show Recipe", bg='#FFF0F5',
                                  command=lambda: showRecipe(checkRecipesWin, clicked))
        showRecipeButton['font'] = fontt
        showRecipeButton.grid(row=3, column=0, pady=(10, 0))


def addRecipes(newUserWin, userId):
    addRecipesWin = Toplevel(newUserWin)
    addRecipesWin.title("Add Recipes")

    recipeNameLabel = Label(addRecipesWin, text="Recipe Name", bg='#FFF0F5')
    recipeNameLabel['font'] = fontt
    recipeNameLabel.grid(row=0, column=0, pady=(10, 0))

    recipeName = Entry(addRecipesWin)
    recipeName.grid(row=0, column=1, padx=20, pady=(10, 0))

    ingredientsLabel = Label(addRecipesWin, text="Ingredients", bg='#FFF0F5')
    ingredientsLabel['font'] = fontt
    ingredientsLabel.grid(row=1, column=0, pady=(10, 0))

    ingredients = Entry(addRecipesWin)
    ingredients.grid(row=1, column=1, padx=20, pady=(10, 0))

    servingSizeLabel = Label(addRecipesWin, text="Serving Size", bg='#FFF0F5')
    servingSizeLabel['font'] = fontt
    servingSizeLabel.grid(row=2, column=0, pady=(10, 0))

    servingSize = Entry(addRecipesWin)
    servingSize.grid(row=2, column=1, padx=20, pady=(10, 0))

    caloriesLabel = Label(addRecipesWin, text="Calories", bg='#FFF0F5')
    caloriesLabel['font'] = fontt
    caloriesLabel.grid(row=3, column=0, pady=(10, 0))

    calories = Entry(addRecipesWin)
    calories.grid(row=3, column=1, padx=20, pady=(10, 0))

    instructionsLabel = Label(addRecipesWin, text="Instructions", bg='#FFF0F5')
    instructionsLabel['font'] = fontt
    instructionsLabel.grid(row=4, column=0, pady=(10, 0))

    instructions = Entry(addRecipesWin)
    instructions.grid(row=4, column=1, padx=20, pady=(10, 0))

    addButton = Button(addRecipesWin, text="Add Recipe", bg='#FFF0F5',
                       command=lambda: addRecipe(addRecipesWin, userId, recipeName.get(), servingSize.get(),
                                                 calories.get(), ingredients.get(), instructions.get()))
    addButton['font'] = fontt
    addButton.grid(row=5, column=0, columnspan=2, pady=(10, 0))

    addRecipesWin.mainloop()


def addRecipe(addRecipesWin, userId, recipeName, servingSize, calories, ingredients, instructions):
    q = """INSERT INTO recipes(recipeName, ingredients, servings, calories, instructions,userRecipe) VALUES (%s, %s, 
    %s, %s,%s, %s) """
    action.execute(q, [recipeName, ingredients, servingSize, calories, instructions, str(userId)])
    dbase.commit()
    messagebox.showinfo("Success", "Recipe added!")
    addRecipesWin.destroy()


main = Tk()
main.configure(background='#800000')
fontt = font.Font(family='Courier', size=10, weight='bold')

main.title("Recipe Application")
main.resizable(False, False)

dbase = mysql.connect(
    host="localhost",
    user="root",
    passwd="03232001",
    database="nutritionapp"
)
action = dbase.cursor()
connectUser()
main.mainloop()

#Work on some stuff