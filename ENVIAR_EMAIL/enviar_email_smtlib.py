# Construir la estructura del email
from email.message import EmailMessage 
# conectar con el servidor y enviarlo
import smtplib 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#Python image Library
from PIL import ImageTk, Image


"------------INTERFAZ TKINTER------------"
ventana =Tk()
ventana.title("---DaniZetaK---")
ventana.geometry("335x402")
ventana.resizable(0,0)
ventana.config(bd=10)


# Título del software
Label(ventana, text="Send messages",
      fg="light blue",
      font=("Roboto", 16,"bold"),
      padx=5,pady=5).grid(row=0,
                          column=0,
                          columnspan=2)


# Lista con los e-mails de los profesores
emails = ("programacionsabattini@gmail.com",
          "fjcoronati@gmail.com",
          "carlosdanielortiz61@gmail.com",
          "danielprogramacion53@gmail.com",
          "lafortaleza246@gmail.com")


# Logo del GMAIL
imagen_gmail=Image.open("aprovar.jpeg")
nueva_imagen=imagen_gmail.resize((265, 95))
render=ImageTk.PhotoImage(nueva_imagen)
label_imagen= Label(ventana,
                    image= render)
label_imagen.image=render
label_imagen.grid(row=1,
                  column=0,
                  columnspan=2)


# Variables para usar
destinatario=StringVar(ventana)
asunto=StringVar(ventana)


# Titulo del e-mail
Label(ventana,
      text="danielprogramacion53@gmail.com",
      fg="gray",
      font=("Arial", 10,"bold"),
      padx=5,pady=5).grid(row=2,
                          column=0,
                          columnspan=2,
                          pady=5)


# Tenemos la ventana para que el usuario ingrese el correo
Label(ventana,
      text="Dirigido a:",
      fg="black", font=("Arial", 10, "bold"),
      padx=5, pady=5).grid(row=3, column=0)


# Agregamos el menu para seleccionar el destinatario
historial = ttk.Combobox(ventana, values=emails, width=31, textvariable=destinatario)
historial.grid(row=3, column=1)


# Es el asunto del mensaje
Label(ventana,
      text="Asunto:",
      fg="black",
      font=("Arial", 10,"bold"),
      padx=5,
      pady=5).grid(row=4,
                   column=0)


Entry(ventana,
      textvariable=asunto,
      width=34).grid(row=4,
                     column=1)


Label(ventana, text="Mensaje:",
      fg="black",
      font=("Arial",
            10,
            "bold"),
      padx=5,pady=5).grid(row=5,
                          column=0)


mensaje=Text(ventana,
             height=5,
             width=28,
             padx=5,
             pady=5)


mensaje.grid(row=5,
             column=1)


mensaje.config(font=("Arial",
                     9),
               padx=5,
               pady=5)



"------------ENVIO DE CORREO------------"
def enviar_email():
    remitente = "danielprogramacion53@gmail.com"
    
    
    # Estrutura de email
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario.get()
    email["Subject"] = asunto.get()
    email.set_content(str(mensaje.get(1.0,
                                      'end')))


    # Envio de email
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    smtp.login(remitente, "e o c g f g l z w b v f g d m e")
    smtp.sendmail(remitente, destinatario.get(), email.as_string())
    messagebox.showinfo("Exito!",
                        "Tu mensaje llegó exitosamente")
    smtp.quit()


"------------BOTON------------"


Button(ventana,
       text="Send",
       command=enviar_email,
       height=2,
       width=10,
       bg="red",
       fg="white",
       font=("Arial",
             11,
             "bold")).grid(row=6,
                           column=0,
                           columnspan=2,
                           padx=5,
                           pady=10)


ventana.mainloop()