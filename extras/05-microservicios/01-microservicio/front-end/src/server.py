import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_books():

#1.Hardcodear la respuesta
    Books = [{"title": "Eragon", "author": "Christopher Paolini"}] 
    return render_template('show_books.html', books=Books)

#2. Encontrar la IP del backend y asignarla
 #   Books = requests.get('http://172.28.0.3:5000/books').json()
 #   return render_template('show_books.html', books=Books)

#3. Mediante el service discovery de Docker
 #   Books = requests.get('http://book-api:5000/books').json()
 #   return render_template('show_books.html', books=Books)

#3. Mediante variable de entorno desde afuera -> ver 02-micromejorado

#Docker automatically injects aliases for the IP addresses of linked containers, assigned as their service names.
#This is known as automatic service discovery.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
