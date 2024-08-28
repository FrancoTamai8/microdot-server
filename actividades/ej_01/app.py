# Aplicacion del servidor
from microdot import Microdot, send_file

do_connect()
app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/<dir>/<file>')
async def index(request, dir, file):
    return send_file("/" + dir+ "/" + file)

app.run(port=80)