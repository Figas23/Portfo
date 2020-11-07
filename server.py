from flask import Flask, render_template, request, url_for, redirect  #render_template-> let us sent the html file
import csv
app = Flask(__name__)
print(__name__)


#A pasta templates e statis são criadas para a flask app saber onde procurar


@app.route('/')     # Isto é um decorator
def my_home():
    return render_template('index.html')

#set FLASK_APP=server.py -> meto isto no terminal e depois vai me dar um link http:...
#Se meter este link no browser vai me aparecer uma pagina a dizer: "Hello, World!" -> criamos o nosso Servidor

#set FLASK_ENV=development -> Para activar debugger -> assim não precisamos de tar a recomeçar o servidor


#Outro Router. /favicon são aqueles item (imagem pequenina) nos diferentes separadores do browser:
#Não sei pq o meu pc não me deixa descarregar estas imagens .ico por isso vou só meter o código que tem de se fazer:
#Devia transferir a tal imagem (item) para o ficheiro "static" mas não a consigo descarregar
#@app.route('/favicon.ico')
#def blog():
 #   return 'My dog\'s name is Shady'


#Em vez de estar sempre a criar estes Router novos para cada página vamos tentar fazer duma forma mais dinâmica:

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


#Para este nosso portfolio tambem não queremos a parte dos components por isso vamos remove-la dos html files


#Senão iamos ter de criar um router novo para cada pagina nova:

#Router about:
#@app.route('/about.html')
#def about():
 #   return render_template('about.html')

#Router Index:
#@app.route('/index.html')
#def index():
 #   return render_template('index.html')

#Router para os contacts:
#@app.route('/contact.html')
#def contact():
 #   return render_template('contact.html')

#Router para os works:
#@app.route('/works.html')
#def works():
 #   return render_template('works.html')

#Router para os components:
#@app.route('/components.html')
#def components():
 #   return render_template('components.html')


#Criar função para guardar na database.txt a informação que o servidor recebe do utilizador so site (que manda um email)
def write_to_file(data):
    with open("database.txt", mode ='a') as database:     #'a' -> append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {email}, {subject}, {message}")


#Agora criar uma função que em vez de importar para um ficheiro .txt importe para um ficheiro .csv (melhor)
def write_to_csv(data):
    with open("database.csv", newline='', mode ='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter =',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



# Criar um router para os utilizadores me contactarem (da pagina contact do site):

@app.route('/submit_form', methods=['POST', 'GET'])     #get -> browser want us to send information
def submit_form():                                      #post -> browser want us to save information
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            "Did not save to database"
    else:
        return "Something went wrong. Try again"




#Comandos que podem ser importantes:
    # set FLASK_APP=server.py
    # flask run

# No entanto só no meu PC consigo aceder a http://127.0.0.1:5000/ pois é um local host =>igual a localhost:5000/


#Uma forma de por o meu site online:

# git clone https://github.com/Figas23/Portfo.git -> para clonar o ficheiro para o github

#Agora se eu for ao meu Web_Server vai estar lá o file Portfo

