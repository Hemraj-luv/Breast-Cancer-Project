# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:55:31 2019

@author: Hemraj
"""

import tkinter
from tkinter import Label, Entry, Button
from tkinter import messagebox
import numpy as np
print(dir(sklearn))

from sklearn import model_selection,  neighbors
import pandas as pd

class breast_cancer():
    def rules(self):
        a = """#      Attribute                               Domain
           -- -----------------------------------------
           1. Clump Thickness               1 - 10
           2. Uniformity of Cell Size      1 - 10
           3. Uniformity of Cell Shape  1 - 10
           4. Marginal Adhesion           1 - 10
           5. Single Epithelial Cell Size 1 - 10
           6. Bare Nuclei                         1 - 10
           7. Bland Chromatin               1 - 10
           8. Normal Nucleoli                 1 - 10
           9. Mitoses                               1 - 10
         """
        messagebox.showinfo("Guidelines for parameters are as follows:-",a)

    def quit_window(self):
        if messagebox.askokcancel("Quit", "You want to quit now? "):
            root.destroy()

    def actionPerformed(self):

        if ( self.T1.get() == '' or self.T2.get() == '' or self.T3.get() == '' or self.T4.get() == '' or self.T5.get() == '' or self.T6.get() == '' or self.T7.get() == '' or self.T8.get() == '' or self.T9.get() == ''):
            messagebox.showerror("error", "Fill all the fields")

        elif (int(self.T1.get()) > 10 or int(self.T2.get()) > 10 or int(self.T3.get()) > 10 or int(
                self.T4.get()) > 10 or int(self.T5.get()) > 10 or int(self.T6.get()) > 10 or int(
                self.T7.get()) > 10 or int(self.T8.get()) > 10 or int(self.T9.get()) > 10):
            messagebox.showerror("error", "Values should be in 1 to 10")

        else:
            patient_measures = np.array(
                [self.T1.get(), self.T2.get(), self.T3.get(), self.T4.get(), self.T5.get(), self.T6.get(),
                 self.T7.get(), self.T8.get(), self.T9.get()])
            patient_measures = patient_measures.reshape(1, -1)
            prediction = clf.predict(patient_measures)
            print(prediction)

            if (prediction == 4):
                self.panel1 = Label(root, bg='red', width=30, height=10)
                self.panel2 = Label(root, text="Malignant", font=('arial', 10, 'bold'), width=10, height=1)
                self.panel1.place(x=350, y=390)
                self.panel2.place(x=420, y=550)


            elif (prediction == 2):
                self.panel = Label(root, bg='green', width=30, height=10)
                self.panel2 = Label(root, text="Benign", font=('arial', 10, 'bold'), width=7, height=1)
                self.panel.place(x=350, y=390)
                self.panel2.place(x=420, y=550)

            else:
                self.panel = Label(root, text='NO RESULT', bg='yellow', width=30, height=10)
                self.panel.place(x=600, y=200)

    def __init__(self, root):

        self.label = Label(root, text='Classification Of Breast Cancer Tumor', font=('arial', 30, 'bold'), bg='AZURE',fg='black')
        self.label.pack()

        self.label_1 = Label(root, text='Clump Thickness :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=90)

        self.T1 = Entry(root, textvariable='t1', bd=2)
        self.T1.place(x=180, y=90)

        self.label_1 = Label(root, text='Uniform Cell Size :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=140)

        self.T2 = Entry(root, textvariable='t2', bd=2)
        self.T2.place(x=180, y=140)

        self.label_1 = Label(root, text='Uniform Cell Shape :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=190)

        self.T3 = Entry(root, textvariable='t3', bd=2)
        self.T3.place(x=180, y=190)

        self.label_1 = Label(root, text='Marginal Adhesion :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=240)

        self.T4 = Entry(root, textvariable='t4', bd=2)
        self.T4.place(x=180, y=240)

        self.label_1 = Label(root, text='Single Epi Cell Size :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=290)

        self.T5 = Entry(root, textvariable='t5', bd=2)
        self.T5.place(x=180, y=290)

        self.label_1 = Label(root, text='Bare Nuclei :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=340)

        self.T6 = Entry(root, textvariable='t6', bd=2)
        self.T6.place(x=180, y=340)

        self.label_1 = Label(root, text='Bland Chromation :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=390)

        self.T7 = Entry(root, textvariable='t7', bd=2)
        self.T7.place(x=180, y=390)

        self.label_1 = Label(root, text='Normal Nucleoli :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=440)

        self.T8 = Entry(root, textvariable='t8', bd=2)
        self.T8.place(x=180, y=440)

        self.label_1 = Label(root, text='Mitosis :',bg="lightseagreen", font=('arial', 10, 'bold'), fg='black')
        self.label_1.place(x=30, y=490)

        self.T9 = Entry(root, textvariable='t9', bd=2)
        self.T9.place(x=180, y=490)

        self.button1 = Button(root, width=6, text='ENTER',bg="AZURE", command=self.actionPerformed, font=('arial', 12), bd=3)
        self.button1.place(x=450, y=200)

        self.button2 = Button(root, width=6, text='QUIT',bg="AZURE", command=self.quit_window, font=('arial', 12), bd=3)
        self.button2.place(x=450, y=300)

        acc_button = Button(root, text="RULES", bg="AZURE", font=('arial', 10), command=self.rules,bd=3)
        acc_button.place(x=530, y=70)

        root.mainloop()


df = pd.read_csv('breast-cancer-wisconsin.txt')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)


def print_acc():
    accuracy2 = float(accuracy)
    panel_acc = Label(root, text=float(accuracy2),bg="AZURE", font=('arial', 10, 'bold'), width=20, height=2)
    panel_acc.place(x=180, y=550)


root = tkinter.Tk()
root.title("Classification")
path1 = ("py.ico")
root.iconbitmap(path1)
root.minsize(600,600)
root.config(bg="lightseagreen")
acc_button = Button(root, text="CHECK ACCURACY",bg="AZURE", font=('arial', 10), command=print_acc)
acc_button.place(x=30, y=550)

m = breast_cancer(root)
root.mainloop()
