# HabitTracker

Como parte de continuar practicando Python y poner en pactica dicho aprendizaje desarrollo esta aplicacion sencilla.


in order to run flask in a virtual enviroment:
primero necesito crear el folder con el ambiente virtual:
    python3 -m venv .venv

luego para inciar el uso del ambiente virtual se ejecuta
  - . .venv/bin/activate (para Linux/Mac)
  - . .venv/Scripts/activate (para Windows)

por ultimo para que Flask sepa cual es el proyecto que estamos ejecutando, se actualizan las siguientes variables, la segunda no es obligatoria es para aclarar que se encuentra en desarrollo.
  - export FLASK_APP=app.py
  - export FLASK_ENV=development

A este punto el ambiente virtual probablemente no tenga instalado ninguna de las bibliotecas necesarias para correr el programa, por lo que deberia ejecutarse el archivo requirements.txt:
    pip install requirements.txt