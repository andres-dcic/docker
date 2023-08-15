#import requests
import requests,os
from flask import Flask, render_template

BOOK_API_SERVER= os.environ['BOOK_API_SERVER']
app = Flask(__name__)


@app.route('/')
def show_books():
#   El servicio de frontend devuelvo esto...sin consultar al backend
#    Books = [{"title": "Eragon", "author": "Christopher Paolini"}] 
#    return render_template('show_books.html', books=Books)

#   El servicio de fronted ahora si consulta al backend, pero primeramente
#   encontrar que ip esta usando el backend
#    Books = requests.get('http://172.18.0.3:5000/books').json()
#    return render_template('show_books.html', books=Books)

#  Utilizando el service discovery de docker   
#    Books = requests.get('http://book-api:5000/books').json()
#    return render_template('show_books.html', books=Books)

#Utilizando variable de entorno
    Books = requests.get(BOOK_API_SERVER + "/books").json()
    return render_template('show_books.html', books=Books)

#Docker automatically injects aliases for the IP addresses of linked containers, assigned as their service names.
#This is known as automatic service discovery.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
