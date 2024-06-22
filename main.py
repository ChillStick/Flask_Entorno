from flask import Flask
import random

app = Flask(__name__)

lista = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos","Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna", "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo", "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo", "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
         "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos", "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]
lista_img = ["https://fotos.e-consulta.com/facebook07.jpg", "https://forjandofuturos.wordpress.com/wp-content/uploads/2018/10/la_tecnologia_tiene_consecuencias.jpg?w=1000",
             "https://www.merca20.com/wp-content/uploads/2014/09/memes5.jpg", "https://maldita.es/uploads/images/2022/12/63a57adfc42e7meme-tech-1-png.png"]

@app.route("/")
def hello_world():
    return '<p>Hello, World!</p><a href="/randomfacts">Ver dato curioso <a href="/randomimage">Ver imágenes random'

@app.route("/randomfacts")
def random_factores():
    return f"<h2>Dato Aleatorio</h2> <p> {random.choice(lista)} </p><a href='/'>Regresar"

@app.route("/randomimage")
def random_imagenes():
    return f"<h2>Imagenes Random</h2> <img src={random.choice(lista_img)} ><a href ='/'>Regresar"

app.run(debug=True)
