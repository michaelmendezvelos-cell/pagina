from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Heury</title>
        <style>
            body{
                font-family: Arial;
                background-color: #111;
                color: white;
                padding: 40px;
            }

            h1{
                color: red;
            }

            .caja{
                background: #222;
                padding: 20px;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>

        <h1>Informe sobre la demanda de Roblox de heury</h1>

        <div class="caja">
            <p>
            Roblox ha enfrentado distintas demandas y críticas relacionadas
            con la seguridad de los usuarios, el contenido dentro de la plataforma
            y temas económicos relacionados con desarrolladores.
            </p>

            <p>
            Algunas personas han acusado a la plataforma de no moderar correctamente
            ciertos contenidos y de permitir problemas relacionados con menores
            de edad y compras dentro del juego.
            </p>

            <p>
            Roblox ha respondido mejorando herramientas de seguridad,
            moderación y control parental para proteger a los usuarios.
            </p>
        </div>

    </body>
    </html>
    """

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Heury</h1><p>Informe de Roblox</p>"

app.run(host="0.0.0.0", port=10000)