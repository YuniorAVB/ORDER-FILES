import os
import shutil
from tkinter import Button, StringVar, Tk, filedialog, PhotoImage, messagebox
import webbrowser


dir_moved_type_not_found = "OTROS"

array_files_types = [
    {
        "ARCHIVOS TEXTO": ("txt")
    },
    {
        "ARCHIVOS PDF": ("pdf")
    },
    {
        "ARCHIVOS WORD": ("doc", "docx")
    },
    {
        "ARCHIVOS EXCEL": ("xls", "xlsx", "csv")
    },
    {
        "ARCHIVOS PPT": ("ppt", "pps", "pptx", "ppsx")
    },
    {
        "IMAGENES": ("jpg", "jpge", "png", "gif", "svg", "raw", "nef")
    },
    {
        "VIDEOS": ("mp4", "flv", "mpg4", "div", "dvd", "mpe", "mpa", "mpg", "mov", "avi", "asf")
    },
    {
        "MUSICA": ("mp3", "mid", "midi", "wav", "cda", "ogg", "ogm", "flac", "aym")
    },
    {
        "PROGRAMAS DE WINDOWS": ("exe", "msi", "bat", "cat", "dll")
    },
    {
        "PHOTOSHOP": ("psd")
    },
    {
        "ADOBE ILUSTRATOR": ("ai")
    },
    {
        "JAVASCRIPT": ("js")
    },
    {
        "HTML": ("html")
    },
    {
        "CSS": ("css")
    },
    {
        "PHP": ("php")
    },
    {
        "JAVA": ("java", "javac")
    },
    {
        "ISOS": ("iso")
    },
    {
        "COMPRIMIDOS": ("zip", "rar", "tar")
    }


]

gui = Tk()
gui.title("Ordenar Archivos")
windowWidth = 500
windowHeight = 800

gui.resizable(False, False)

positionRight = int(gui.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(gui.winfo_screenheight()/2 - windowHeight/2)
gui.geometry("+{}+{}".format(positionRight, positionDown))

folderPath = StringVar()


def joinDirectory(parent, dir):
    return os.path.join(parent, dir)


def existsDirectory(dir):
    return os.path.exists(dir)


def isFile(path):
    return os.path.isfile(path)


def typeFile(mimetype):
    return mimetype[len(mimetype) - 1]


def dirMovedRoutePath(mimetype):

    rute_moved_file = ""

    for files_types in array_files_types:
        for file_type in files_types:
            for types in files_types[file_type]:

                if types == mimetype:
                    rute_moved_file = file_type

    if rute_moved_file == "":
        rute_moved_file = dir_moved_type_not_found

    return joinDirectory(folderPath.get(), rute_moved_file)


def createDirectorys():

    if existsDirectory(joinDirectory(folderPath.get(), dir_moved_type_not_found)) == False:
        os.mkdir(joinDirectory(folderPath.get(), dir_moved_type_not_found))

    for files_types in array_files_types:

        for file_type in files_types:

            if existsDirectory(joinDirectory(folderPath.get(), file_type)) == False:
                os.mkdir(joinDirectory(folderPath.get(), file_type))


def startOrderDirectory():
    createDirectorys()

    for file in os.listdir(folderPath.get()):

        if isFile(joinDirectory(folderPath.get(), file)):

            route_moved_file = dirMovedRoutePath(
                typeFile(file.split('.')))
            shutil.move(joinDirectory(
                        folderPath.get(), file), route_moved_file)


def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)


def start():

    if folderPath.get() == "":
        messagebox.showwarning(message="Seleccione una Carpeta", title="ERROR")
    else:
        confirm = messagebox.askyesno(
            message="Seguro que desea Ordenar la Carpeta : " + folderPath.get(), title="Mensaje")
        if confirm:
            startOrderDirectory()
            messagebox.showinfo(
                message="Carpeta Ordenado con Exito", title="Mensaje")


def urlOpenYAVBCODE():
    webbrowser.open("https://www.youtube.com/channel/UCCD_MU-c7etLX-0Gv3HcPgg")


def getPathAssets():
    return os.path.join(os.path.dirname(__file__), 'assets')


def __main__():

    try:
        img_1 = PhotoImage(file=joinDirectory(
            getPathAssets(), "img_1_test.png"))

        img_1 = img_1.subsample(1)

        btnFind = Button(
            gui, image=img_1, cursor="hand1", border=0, command=getFolderPath)

        btnFind.pack()

        img_start = PhotoImage(file=joinDirectory(
            getPathAssets(), "img_start.png"))
        img_start = img_start.subsample(2)

        btnStart = Button(gui, image=img_start, cursor="hand1",
                          border=0, command=start)

        btnStart.pack()

        img_by = PhotoImage(file=joinDirectory(getPathAssets(), "by.png"))
        buttonBy = Button(gui, border=0, cursor="hand1",
                          padx=10, pady=10, image=img_by, command=urlOpenYAVBCODE)
        buttonBy.pack(side="right")

        gui.mainloop()

    except:
        messagebox.showwarning(message="Ocurrio un Error", title="ERROR")
        exit()


if __name__ == "__main__":
    __main__()
