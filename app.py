from flask import Flask, request, Markup, render_template

app = Flask(__name__)
global usuario

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    usuario = user_text
    return "Hola: " + user_text + ", un gusto. Ahora puedes comenzar."

@app.route('/')
def index():
    return render_template('index.html')

buttons = [
    Markup('<button onclick="send_message(\'Algoritmos\')" class="custom-btn btn-16">Células</button>'),
    Markup('<button onclick="send_message(\'EstructurasControl\')" class="custom-btn btn-16">Componentes de las células</button>'),
    Markup('<button onclick="send_message(\'Metodologia\')" class="custom-btn btn-16">Funcionamiento de las células</button>'),
    Markup('<button onclick="send_message(\'Masnucleo\')" class="custom-btn btn-16">Mas sobre el nucleo</button>'),
    Markup('<button onclick="send_message(\'salir\')" class="custom-btn btn-16">Salir</button>')
]

butop1 = '<button onclick="send_message(\'op1\')" class="custom-btn btn-16">op1</button>'
butop2 = '<button onclick="send_message(\'op2\')" class="custom-btn btn-16">op2</button>'
butop3 = '<button onclick="send_message(\'op3\')" class="custom-btn btn-16">op3</button>'
butop4 = '<button onclick="send_message(\'op4\')" class="custom-btn btn-16">op4</button>'
butop5 = '<button onclick="send_message(\'op5\')" class="custom-btn btn-16">op5</button>'
regresar = '<button onclick="send_message(\'regresar\')" class="custom-btn btn-16">Regresar</button>'

algoritmos = [
    Markup('<button onclick="send_message(\'significado\')" class="custom-btn btn-16">¿Qué son las células?</button>')
    ]

EstructurasControl = [
    Markup('<button onclick="send_message(\'usocontrol\')" class="custom-btn btn-16">Menbrana celular</button>'),
    Markup('<button onclick="send_message(\'tiposcontrol\')" class="custom-btn btn-16">Citoplasma</button>'),
    Markup('<button onclick="send_message(\'subalgoritmos\')" class="custom-btn btn-16">Nucleo</button>'),
    Markup('<button onclick="send_message(\'pared\')" class="custom-btn btn-16">Pared celular</button>'),
    Markup('<button onclick="send_message(\'maspared\')" class="custom-btn btn-16">Mas acerca de la pared celular</button>'),
    Markup('<button onclick="send_message(\'masmembrana\')" class="custom-btn btn-16">Mas de la menbrana celular</button>'),
    Markup('<button onclick="send_message(\'presion\')" class="custom-btn btn-16">Presion Osmotica</button>'),
    Markup('<button onclick="send_message(\'mascitoplasma\')" class="custom-btn btn-16">Mas del citoplasma</button>'),
    Markup('<button onclick="send_message(\'citoesqueleto\')" class="custom-btn btn-16">Citoesqueleto</button>'),
    Markup('<button onclick="send_message(\'organulos\')" class="custom-btn btn-16">Organulos y mas cosas</button>')
]



Codificacion = [
    Markup('<button onclick="send_message(\'etapasmito\')" class="custom-btn btn-16">Mitocondrias</button>'),
    Markup('<button onclick="send_message(\'endoplasmico\')" class="custom-btn btn-16">Reticulo endoplasmico</button>'),
    Markup('<button onclick="send_message(\'Golgi\')" class="custom-btn btn-16">Aparato de Golgi</button>'),
    Markup('<button onclick="send_message(\'Lisosomas\')" class="custom-btn btn-16">Lisosomas</button>'),
    Markup('<button onclick="send_message(\'Cloroplastos\')" class="custom-btn btn-16">Mitocondrias</button>')
]

Metodologia = [
    Markup('<button onclick="send_message(\'obtencion\')" class="custom-btn btn-16">Obtencion de nutrientes</button>'),
    Markup('<button onclick="send_message(\'metabolismo\')" class="custom-btn btn-16">Metabolismo</button>'),
    Markup('<button onclick="send_message(\'reproduccion\')" class="custom-btn btn-16">Reproduccion</button>'),
    Markup('<button onclick="send_message(\'comunicacion\')" class="custom-btn btn-16">Comunicacion</button>'),
    Markup('<button onclick="send_message(\'eliminacion\')" class="custom-btn btn-16">Eliminacion de desechos</button>')  
]

Masnucleo = [
    Markup('<button onclick="send_message(\'funcionesnucleo\')" class="custom-btn btn-16">Funciones del nucleo</button>'),
    Markup('<button onclick="send_message(\'adn\')" class="custom-btn btn-16">ADN</button>'),
    Markup('<button onclick="send_message(\'arn\')" class="custom-btn btn-16">ARN</button>'),
    Markup('<button onclick="send_message(\'celulaeu\')" class="custom-btn btn-16">Celula Eucariota</button>'),
    Markup('<button onclick="send_message(\'calulapro\')" class="custom-btn btn-16">Celula Procariota</button>'),
    Markup('<button onclick="send_message(\'nucleoide\')" class="custom-btn btn-16">Nucleoide</button>')
]

@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    if message == 'Comenzar':
        return buttons

    elif message == 'Algoritmos':
        texto = "Células"
        info = [f"<p class='comentario burbuja'>{texto}</p>", algoritmos, regresar]
        return info

    elif message == 'significado':
        texto = "Una célula es la unidad más pequeña y básica de la vida. Todas las formas de vida, desde organismos unicelulares como las bacterias hasta organismos multicelulares como los seres humanos, están compuestas por una o más células. Las células realizan todas las funciones necesarias para mantener la vida, como la obtención y utilización de nutrientes, la eliminación de desechos y la reproducción. Las células tienen una variedad de componentes, incluyendo una membrana celular que rodea la célula y regula el movimiento de materiales dentro y fuera de la célula, el núcleo que contiene el material genético de la célula, y el citoplasma, que es el líquido que llena la célula y contiene muchas estructuras subcelulares como los orgánulos."
        info = [f"<p class='comentario burbuja'>{texto}</p>", algoritmos, regresar]
        return info

    elif message == 'funcion':
        texto = "Las células tienen varios componentes, algunos de los cuales son comunes a todos los tipos de células, mientras que otros son específicos de ciertos tipos de células. A continuación se presentan algunos de los componentes comunes de una célula eucariota típica:"
        info = [f"<p class='comentario burbuja'>{texto}</p>", algoritmos, regresar]
        return info


    elif message == 'fundamentos':
        youtube_id = '<iframe width="560" height="315" src="https://www.youtube.com/embed/MNVpJpX8OiE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
        info = [youtube_id, '<br>', algoritmos, regresar]
        return info

    elif message == 'EstructurasControl':
        texto = "Tema de componentes de la celula"
        info = [f"<p class='comentarior burbujar'>{texto}</p>", EstructurasControl, regresar]
        return info

    elif message == 'subalgoritmos':
        texto = "Es el centro de control de la célula, contiene el material genético de la célula, el ADN, y dirige la síntesis de proteínas y la replicación del ADN."
        info = [f"<p class='comentario burbuja'>{texto}</p>", EstructurasControl, regresar]
        return info

    elif message == 'usocontrol':
        texto = "Es una capa delgada y flexible que rodea la célula y la separa del entorno. Regula el intercambio de materiales entre la célula y su entorno."
        info = [f"<p class='comentario burbuja'>{texto}</p>", EstructurasControl, regresar]
        return info
    
    elif message == 'pared':
        texto = "Proporciona soporte y protección a la célula, manteniendo su forma y evitando que se dañe bajo presión osmótica. Además, también puede actuar como una barrera selectiva para el movimiento de sustancias."
        info = [f"<p class='comentario burbuja'>{texto}</p>", EstructurasControl, regresar]
        return info
    
    elif message == 'masmembrana':
        texto = "La membrana celular es una estructura esencial para la supervivencia de la célula, ya que regula el intercambio de materiales y protege la célula del entorno externo. Regula el movimiento de sustancias dentro y fuera de la célula, esta compuesta principalmente de fosfolípidos, proteínas y carbohidratos unidos a los fosfolípidos y las proteínas que ayudan a la célula a reconocer y comunicarse con otras células."
        info = [f"<p class='comentario burbuja'>{texto}</p>", EstructurasControl, regresar]
        return info
    
    elif message == 'maspared':
        texto = "La pared celular es una estructura rígida presente en algunas células, como las células vegetales, las células fúngicas y las células bacterianas, su función principal es proporcionar soporte y protección a la célula, manteniendo su forma y evitando que se dañe bajo presión osmótica. En las células vegetales, la pared celular está compuesta principalmente de celulosa, mientras que en las células fúngicas está compuesta de quitina. En las células bacterianas, la pared celular está compuesta de peptidoglicano."
        info = [f"<p class='comentario burbuja'>{texto}</p>", EstructurasControl, regresar]
        return info
    
    elif message == 'presion':
        texto = "La presión osmótica se refiere a la tendencia de las células a absorber agua, lo que puede hacer que se hinchen y exploten si no tienen una pared celular resistente para mantener su forma. "
        info = [f"<p class='comentario burbuja'>{texto}</p>", EstructurasControl, regresar]
        return info
    
    
    elif message == 'mascitoplasma':
        texto = "El citoplasma es una estructura celular que se encuentra entre la membrana celular y el núcleo. Está compuesto por un líquido llamado citosol y por diversas estructuras celulares, como orgánulos y citoesqueleto."
        texto1 = "La función del citoplasma es proporcionar soporte y estructura a la célula, permitir la realización de procesos metabólicos, transportar sustancias y moléculas dentro de la célula y permitir la movilidad y la posición de los órganos celulares."
        info = [
        f"<p class='comentario burbuja'>{texto}</p>",
        f"<p class='comentario burbuja'>{texto1}</p>",
        EstructurasControl,
        regresar
    ]
        return info
    
    elif message == 'citoesqueleto':
        texto = "El citoesqueleto, que forma parte del citoplasma, es una red de filamentos proteicos que proporciona soporte y ayuda a mantener la forma de la célula. También ayuda a la célula a moverse ya mantener la posición de los órganos celulares."
        info = [f"<p class='comentario burbuja'>{texto}</p>", EstructurasControl, regresar]
        return info
    


    elif message == 'tiposcontrol':
        texto1 = "Es el líquido viscoso que llena la célula. Contiene los organulos celulares y es el lugar donde ocurren muchas de las funciones celulares."
        info = [f"<p class='comentario burbuja'>{texto1}</p>", EstructurasControl, regresar]
        return info


    elif message == 'Masnucleo':
        texto = "Mas acerca del nucleo"
        info = [f"<p class='comentarior burbujar'>{texto}</p>", Masnucleo, regresar]
        return info
    
    elif message == 'funcionesnucleo':
        texto = "Funciones del Núcleo "
        texto1 = "Almacenamiento del ADN: El ADN es esencial para la supervivencia y el funcionamiento de la célula, ya que contiene la información necesaria para la síntesis de proteínas y otras moléculas."
        texto2 = "Regulación de la expresión génica: El núcleo regula la expresión génica, es decir, qué genes se transcriben y traducen en proteínas y en qué momento. "
        texto3 = "Síntesis de ARN: El ARN se transcribe a partir del ADN y luego se transporta al citoplasma, donde se traduce en proteínas."
        texto4 = "Control del ciclo celular: Controla el ciclo celular el proceso de división y crecimiento de la célula. "
        info = [
        f"<p class='comentario burbuja'>{texto}</p>", 
        f"<p class='comentario burbuja'>{texto1}</p>", 
        f"<p class='comentario burbuja'>{texto2}</p>", 
        f"<p class='comentario burbuja'>{texto3}</p>", 
        f"<p class='comentario burbuja'>{texto4}</p>", 
        Masnucleo, regresar]
        return info
    
    elif message == 'adn':
        texto1 = "El ADN (ácido desoxirribonucleico) es una molécula compleja que contiene la información genética de los organismos vivos. Su estructura única y secuencia de nucleótidos es importante para su función, incluyendo la síntesis de proteínas y la replicación celular."
        info = [f"<p class='comentario burbuja'>{texto1}</p>", Masnucleo, regresar]
        return info
    
    elif message == 'arn':
        texto1 = "El ARN (ácido ribonucleico) es una molécula de cadena única que se encuentra en todas las células vivas. "
        texto2 = "El ARN desempeña varios roles importantes en la célula, incluyendo la síntesis de proteínas, la regulación génica y el procesamiento de otros tipos de ARN."
        info = [
        f"<p class='comentario burbuja'>{texto1}</p>",
        f"<p class='comentario burbuja'>{texto2}</p>",
        Masnucleo, regresar]
        return info
    
    elif message == 'celulaeu':
        texto1 = "La célula eucariota es un tipo de célula que se encuentra en organismos multicelulares y unicelulares más complejos, como plantas, animales, hongos y protistas. "
        texto2 = "La característica principal que distingue a las células eucariotas de las células procariotas (como las bacterias) es la presencia de un núcleo definido y separado del resto de la célula por una membrana nuclear."
        info = [
        f"<p class='comentario burbuja'>{texto1}</p>",
        f"<p class='comentario burbuja'>{texto2}</p>",
        Masnucleo, regresar]
        return info
    
    elif message == 'celulapro':
        texto1 = "La célula procariota es un tipo de célula que se encuentra en organismos unicelulares, como bacterias y arqueas. A diferencia de las células eucariotas, las células procariotas no tienen un núcleo definido y separado del resto de la célula por una membrana nuclear."
        texto2 = "El material genético en las células procariotas se encuentra en una región llamada nucleoide. Las células procariotas son generalmente más pequeñas que las células eucariotas y tienen una forma más simple. "
        info = [
        f"<p class='comentario burbuja'>{texto1}</p>",
        f"<p class='comentario burbuja'>{texto2}</p>",
        EstructurasControl, regresar]
        return info
    
    elif message == 'nucleoide':
        texto1 = "El nucleoide es la región en una célula procariota donde se encuentra el material genético de la célula. Aunque el nucleoide no está rodeado por una membrana nuclear, está organizado y estructurado por proteínas y enzimas especiales que ayudan a empacar y organizar el ADN"
        texto2 = "El ADN en el nucleoide es esencial para la supervivencia de la célula, ya que contiene la información genética necesaria para la síntesis de proteínas y la replicación celular."
        info = [
        f"<p class='comentario burbuja'>{texto1}</p>",
        f"<p class='comentario burbuja'>{texto2}</p>",
        Masnucleo, regresar]
        return info
    
    











    elif message == 'Metodologia':
        texto = "Tema de funcionamiento de las celulas"
        info = [f"<p class='comentarior burbujar'>{texto}</p>", Metodologia, regresar]
        return info

    elif message == 'obtencion':
        texto = "Las células obtienen nutrientes a través de dos vías principales:"
        texto1 = "Transporte pasivo: Este proceso implica el movimiento de moléculas y iones a través de la membrana celular sin gasto de energía, puede ocurrir por difusión simple, o por ósmosis."
        texto2 = "Transporte activo: Este proceso requiere el gasto de energía celular para mover moléculas y iones en contra de su gradiente de concentración. Una vez dentro de la célula, los nutrientes pueden ser utilizados para diferentes procesos metabólicos, como la producción de energía a través de la respiración celular, la síntesis de proteínas y la formación de nuevas células durante la división celular."

        info = [
        f"<p class='comentario burbuja'>{texto}</p>",
        f"<p class='comentario burbuja'>{texto1}</p>",
        f"<p class='comentario burbuja'>{texto2}</p>",
        Metodologia,
        regresar
    ]
    
        return info

    elif message == 'metabolismo':
        texto = "El metabolismo de una célula es el conjunto de reacciones químicas que ocurren en su interior para mantener su funcionamiento, crecimiento y reproducción. "
        texto2 = "La mayoría de las células utilizan el proceso de respiración celular para obtener energía. Además de la respiración celular, las células también pueden obtener energía a través de la fermentación y la fotosíntesis en el caso de las células fotosintéticas."
        info = [
        f"<p class='comentario burbuja'>{texto}</p>", 
        f"<p class='comentario burbuja'>{texto2}</p>", 
        Metodologia, regresar]
        return info
    elif message == 'reproduccion':
        texto = "La reproducción de una célula se lleva a cabo a través del proceso de división celular, que se divide en dos tipos principales: la mitosis y la meiosis."
        texto1 = "Mitosis La mitosis es el proceso de división celular que ocurre en las células somáticas o células no reproductoras. En este proceso, una célula madre se divide en dos células hijas genéticamente idénticas, que contienen la misma cantidad de cromosomas y material genético. La mitosis se lleva a cabo en cuatro etapas principales: la profase, la metafase, la anafase y la telofase."
        texto2 = "Meiosis La meiosis es el proceso de división celular que ocurre en las células reproductoras. En este proceso, una célula madre se divide en cuatro células hijas, cada una con la mitad del número de cromosomas y la mitad del material genético de la célula madre. La meiosis se lleva a cabo en dos etapas principales: la meiosis I y la meiosis II, cada una de las cuales consta de profase, metafase, anafase y telofase."
        info = [
        f"<p class='comentario burbuja'>{texto}</p>", 
        f"<p class='comentario burbuja'>{texto1}</p>",
        f"<p class='comentario burbuja'>{texto2}</p>",
        Metodologia, regresar]
        return info
    elif message == 'comunicacion':
        texto = "La comunicación celular es el proceso por el cual las células intercambian información entre sí para coordinar sus funciones y mantener la homeostasis en el organismo. "
        texto = "Mecanismos de comunicación celular "
        texto = "Comunicación directa: Ocurre entre células que están en contacto físico a través de canales de comunicación especializados llamados uniones de hendidura"
        texto = "Señalización paracrina: Ocurre cuando las células liberan moléculas señalizadoras, llamadas factores de crecimiento, en el medio extracelular cercano. Estos factores pueden actuar sobre células cercanas y estimular su crecimiento y diferenciación"
        texto = "Señalización endocrina: Ocurre cuando las células liberan moléculas señalizadoras en el torrente sanguíneo, que luego actúan sobre células distantes en diferentes partes del cuerpo."
        texto = "Señalización autocrina: Ocurre cuando las células liberan moléculas señalizadoras que actúan sobre la propia célula que las produce, estimulando su crecimiento y actividad"
        texto = "Señalización neuronal: Ocurre en el sistema nervioso, donde las células nerviosas utilizan neurotransmisores para transmitir información entre sí."
        info = [f"<p class='comentario burbuja'>{texto}</p>", Metodologia, regresar]
        return info
    elif message == 'eliminacion':
        texto = "La eliminación de desechos de la célula es un proceso importante para mantener la homeostasis y prevenir daño celular. Los desechos celulares se generan como resultado del metabolismo celular normal, así como de procesos de reparación y eliminación de células muertas o dañadas."
        texto = "Formas en que la célula elimina sus desechos"
        texto = "Exocitosis: Es un proceso en el cual los desechos se empaquetan en vesículas y se liberan fuera de la célula."
        texto = "Fagocitosis: En este proceso, las células especializadas llamadas fagocitos engullen y degradan materiales extraños o desechos celulares mediante la fusión de vesículas de digestión con los lisosomas."
        texto = "Autófagos: En este proceso, la célula digiere su propio material celular, a través de la formación de autófagosomas que se fusionan con lisosomas"
        texto = "Difusión: Algunos productos de desecho pueden difundirse directamente a través de la membrana celular y ser eliminados por difusión a través del medio extracelular."
        info = [f"<p class='comentario burbuja'>{texto}</p>", Metodologia, regresar]
        return info

    

    elif message == 'organulos':
        texto = "Los orgánulos son estructuras membranosas que se encuentran dentro de las células eucariotas y que tienen funciones específicas en la célula. Cada tipo de orgánulo tiene una estructura y función únicas que contribuyen al funcionamiento de la célula en su conjunto. "
        info = [f"<p class='comentario burbuja'>{texto}</p>", Codificacion, regresar]
        return info

    elif message == 'etapasmito':
        texto = "Son los orgánulos encargados de la producción de energía en la célula, a través de la respiración celular."
        info = [f"<p class='comentario burbuja'>{texto}</p>", Codificacion, regresar]
        return info
    
    elif message == 'endoplasmico':
        texto1 = "Es una red de membranas que se extiende por toda la célula y se divide en dos tipos: el retículo endoplásmico rugoso (RER), que tiene ribosomas adheridos a su superficie y se encarga de la síntesis de proteínas, y el retículo endoplásmico liso (REL), que no tiene ribosomas y se encarga de la síntesis de lípidos."
        info = [f"<p class='comentario burbuja'>{texto1}</p>", Codificacion, regresar]
        return info
    
    elif message == 'Golgi':
        texto1 = "Es el orgánulo encargado de modificar, clasificar y distribuir las proteínas y lípidos producidos por la célula."
        info = [f"<p class='comentario burbuja'>{texto1}</p>", Codificacion, regresar]
        return info
    
    elif message == 'Lisosomas':
        texto1 = "Son orgánulos que contienen enzimas digestivas que se encargan de la degradación de macromoléculas y de la eliminación de materiales de desecho."
        info = [f"<p class='comentario burbuja'>{texto1}</p>", Codificacion, regresar]
        return info
    
    elif message == 'Cloroplastos':
        texto1 = "Son orgánulos exclusivos de las células vegetales y se encargan de la fotosíntesis."
        info = [f"<p class='comentario burbuja'>{texto1}</p>", Codificacion, regresar]
        return info


    elif message == 'salir':
        texto = "Muchas gracias por utilizar AsAD ^w^"
        info = [f"<p id='estado' class='comentario burbuja'>{texto}</p>"]
        return info

    elif message == 'regresar':
        return buttons

    else:
        return 'Lo siento, no entendí tu mensaje.'

if __name__ == '__main__':
    app.run(debug=True)

#SET FLASK_APP=app.py
#python app.py
