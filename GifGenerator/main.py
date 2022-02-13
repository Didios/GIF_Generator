from tkinter import Tk, Menu, Label, Button, Canvas
#import pandas as pd


class GifGeneratorApp():

    def __init__(self):
        self.images = []
        self.indexFrame = 0

    def Launch(self):
        # initialisation fenêtre
        self.root = Tk()
        self.root.title("GifGenerator")

        # barre de menu
        menuBar = Menu(self.root)
        
        file = Menu(menuBar, tearoff=0)
        file.add_command(label = "Nouveau", underline = 0, command = self.NewProject)
        file.add_command(label = "Ouvrir", underline = 0, command = self.Open)
        file.add_command(label = "Sauvegarder", underline = 0, command = self.Save)
        file.add_command(label = "Pré-rendu", underline = 0, command = self.Render)
        file.add_command(label = "Exporter", underline = 0, command = self.Export)
        file.add_separator()
        file.add_command(label="Exit", command = self.root.quit)

        option = Menu(menuBar, tearoff=0)
        option.add_command(label = "Couleur", underline = 0, command = self.Color)
        option.add_command(label = "Police", underline = 0, command = self.Font)
        
        menuBar.add_cascade(label = "Fichier", underline = 0, menu = file)
        menuBar.add_command(label = "Insertion", underline = 0, command = self.Insert)
        menuBar.add_command(label = "Image", underline = 0, command = self.Image)
        menuBar.add_cascade(label = "Options", underline = 0, menu = option)
        self.root.config(menu = menuBar)

        self.MainScreen()

        # lancement fenêtre
        self.root.mainloop()

    def NewProject(self):
        pass

    def Open(self):
        pass

    def Save(self):
        pass

    def Render(self):
        pass

    def Export(self):
        pass

    def Insert(self):
        pass

    def Image(self):
        pass

    def Color(self):
        pass

    def Font(self):
        pass

    def Next(self):
        pass

    def Previous(self):
        pass

    def MoveNext(self):
        pass

    def MovePrevious(self):
        pass

    def Delete(self):
        pass

    def MainScreen(self):
        # flèches
        Label(self.root, text = "Précédent").grid(row = 0, column = 0)
        Button(self.root, text = "", command = self.Next, width = 20, height = 5).grid(row = 1, column = 0)

        Label(self.root, text = "Suivant").grid(row = 0, column = 2)
        Button(self.root, text = "", command = self.Previous, width = 20, height = 5).grid(row = 1, column = 2)

        Label(self.root, text = "Déplacer vers le début").grid(row = 2, column = 0)
        Button(self.root, text = "", command = self.MoveNext, width = 20, height = 5).grid(row = 3, column = 0)

        Label(self.root, text = "Déplacer vers la fin").grid(row = 2, column = 2)
        Button(self.root, text = "", command = self.MovePrevious, width = 20, height = 5).grid(row = 3, column = 2)

        # index frame affichage
        self.indexImage = Label(self.root, text = str(self.indexFrame)).grid(row = 4, column = 0)

        # bouton suppr
        Button(self.root, text = "Suppr", command = self.Delete, width = 10, height = 5).grid(row = 4, column = 2)

        # Canvas
        self.imageDisplay = Canvas(self.root, background = "white").grid(row = 0, column = 1, rowspan = 4)
        self.timeline = Canvas(self.root, background = "black", height = 100).grid(row = 4, column = 1)

if __name__ == "__main__":
    app = GifGeneratorApp()
    app.Launch()
