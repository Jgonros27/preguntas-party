"""Genera los JSON estáticos a partir de bancos editoriales locales y versionados.

No requiere red. Mantiene las 50 tarjetas iniciales y utiliza IDs derivados del
texto para que una regeneración no cambie la identidad de las tarjetas.
"""
import collections,hashlib,json,random,re,sys,unicodedata
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'scripts/content'))
from vocabulary import vocabulary
from culture import culture
from actions import ACTIONS,HARD,JOBS,ANIMAL_ACTIONS
from telepathy import telepathy
from situations import situations

TARGET=1500
RNG=random.Random(20261011)
def normalized(text):
    return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',text.casefold()).encode('ascii','ignore').decode()).strip()
def unique(cards):
    seen=set();result=[]
    for c in cards:
        key=normalized(c['prompt'])
        if key not in seen:
            seen.add(key);result.append(c)
    return result
def select(category,pool,initial,quotas=None):
    originals=initial[category]
    original_prompts={normalized(c['prompt']) for c in originals}
    pool=[c for c in unique(pool) if normalized(c['prompt']) not in original_prompts]
    buckets=collections.defaultdict(list)
    for card in pool: buckets[card['topic']].append(card)
    for bucket in buckets.values(): RNG.shuffle(bucket)
    priority={'El rey león','Tiburón','Harry Potter','Harry Potter y la piedra filosofal','Spider-Man','Atracar un banco','Hacer una tortilla de patatas','Mascar un chicle','Cirujano','Albañil','Electricista','Canguro','Pájaro carpintero','Cangrejo','Gorila','Se me han olvidado las gafas','Subirse a una montaña rusa','Tener un déjà vu'}
    for bucket in buckets.values():bucket.sort(key=lambda c:c['prompt'] not in priority)
    chosen=[]
    if quotas:
        for topic,count in quotas.items():
            chosen.extend(buckets[topic][:count]);buckets[topic]=buckets[topic][count:]
    # Round-robin de ámbitos: el excedente de una familia no eclipsa a las demás.
    while len(chosen)<TARGET-len(originals):
        progress=False
        for topic in sorted(buckets):
            if buckets[topic] and len(chosen)<TARGET-len(originals):
                chosen.append(buckets[topic].pop());progress=True
        if not progress: raise ValueError(f'{category}: contenido insuficiente ({len(chosen)+len(originals)})')
    if len(chosen)>TARGET-len(originals):
        RNG.shuffle(chosen);chosen=chosen[:TARGET-len(originals)]
    for c in chosen:
        c['id']=f'{category}-{hashlib.sha256(normalized(c["prompt"]).encode()).hexdigest()[:12]}'
    # IDs históricos conservados; la ampliación no reinicia las barajas usadas.
    for c in originals:
        c.setdefault('difficulty','medium');c.setdefault('topic','selección original')
    result=originals+chosen
    RNG.shuffle(result)
    assert len(result)==TARGET
    assert len({c['id'] for c in result})==TARGET
    assert len({normalized(c['prompt']) for c in result})==TARGET
    (ROOT/f'src/data/{category}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'cards':len(result),'topics':dict(collections.Counter(c['topic'] for c in result)),'difficulty':dict(collections.Counter(c['difficulty'] for c in result)), 'formats':dict(collections.Counter(c.get('type','challenge') for c in result))}

def card(prompt,topic,difficulty='medium'):
    return {'prompt':prompt,'topic':topic,'difficulty':difficulty}

def bool_statement(question,answer):
    """Solo conversiones de sujeto/atributo sin ambigüedades de opciones."""
    if re.search(r'de estos|de estas|siguiente|aproximad|se dice|considera|atribuye|primero|inventó|descubrió',question,re.I): return None
    q=question.strip('¿? ')
    m=re.fullmatch(r'Cuál es (el|la) (.+)',q,re.I)
    if m and '?' not in m[2] and not answer.startswith(('El ','La ','Los ','Las ')):
        return m[1].capitalize()+' '+m[2]+' es '+answer+'.'
    # Solo verbos que convierten el elemento preguntado en SUJETO, no objeto.
    m=re.fullmatch(r'Qué (?:animal|planeta|país|ciudad|continente|océano|río|metal|elemento|instrumento|película|serie|deporte|fruta|órgano|idioma|pintor|cantante|director|actor|actriz|escritor|compositor|marca|empresa) ((?:es |tiene |se |mide |vive |puede |dirigió |escribió |compuso |protagonizó |aparece |acogió |organizó |lanzó |alberga |almacena |cambia |pone |popularizó ).+)',q,re.I)
    if m and not re.search(r'más|menor|mayor|más de|del cuerpo|conocido por',m[1],re.I):
        subject='El '+answer.lower() if answer in ('Ciclismo','Tenis','Pádel','Bádminton','Fútbol','Baloncesto') else answer
        return subject+' '+m[1]+'.'
    m=re.fullmatch(r'Quién ((?:dirigió|escribió|compuso|pintó|fue|presentaba|ganó|regaló) .+)',q,re.I)
    if m: return (answer+' '+m[1]).rstrip('.')+'.'
    return None

def trivia():
    source=json.loads((ROOT/'scripts/content/trivia-source.json').read_text(encoding='utf-8'))
    result=[]
    for i,record in enumerate(source['records']):
        answers=record['answers'];correct=next(a['text'] for a in answers if a['correct'])
        wrong=[a['text'] for a in answers if not a['correct']]
        q=record['question'];c=card(q,record['topic'],record['difficulty'])
        if re.search(r'solo se puede llegar|17.000 islas|menor densidad de población|practicaba Rafael Nadal',q,re.I): continue
        c['answer']=correct;c['type']='choice';c['options']=[a['text'] for a in answers]
        c['source']={'project':'quizify','file':record['file'],'id':record['id']}
        # No duplicamos una misma pregunta para aumentar artificialmente el mazo.
        # Cada registro se publica una sola vez, en uno de los tres formatos.
        proposed=correct if i%2==0 else wrong[i%len(wrong)]
        statement=bool_statement(q,proposed)
        if i%5==0 and statement:
            c['prompt']='Verdadero o falso: '+statement
            c['type']='boolean';c['answer']='Verdadero.' if proposed==correct else 'Falso. La respuesta correcta es '+correct+'.';c.pop('options')
        elif i%3==0 and not re.search(r'estos|estas|siguiente|cuál de|qué de|opci[oó]n',q,re.I):
            c['type']='open';c.pop('options')
        result.append(c)
    return result

def main():
    original_path=ROOT/'scripts/content/original.json'
    if not original_path.exists():
        initial={category:json.loads((ROOT/f'src/data/{category}.json').read_text(encoding='utf-8')) for category in ('telepatia','mimica','preguntas','dibujos','prohibido')}
        assert all(len(cards)==10 for cards in initial.values()),'Falta el snapshot inicial de las 50 tarjetas.'
        original_path.write_text(json.dumps(initial,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    initial=json.loads(original_path.read_text(encoding='utf-8'))
    lex=vocabulary();names=culture();scene=situations()
    # Dificultad editorial por concepto, nunca aleatoria.
    difficult_animals={'Mantis religiosa','Termita','Renacuajo','Alpaca','Pez globo','Manta raya','Suricata','Tejón','Orangután','Anaconda','Codorniz'}
    familiar_people={'Michael Jackson','Elvis Presley','Rafael Nadal','Lionel Messi','Cristiano Ronaldo','Charlie Chaplin','Bruce Lee','Shakira'}
    simple_characters={'Harry Potter','Spider-Man','Batman','Superman','Hulk','Darth Vader','Yoda','Shrek','Pikachu','Mickey Mouse','Homer Simpson','Bob Esponja','Mario','Elsa','Olaf','Simba','Pinocho','Caperucita Roja'}
    for c in lex:
        if c['topic']=='animales':c['difficulty']='medium' if c['prompt'] in difficult_animals else 'easy'
        if c['topic']=='emociones y conceptos':c['difficulty']='hard'
        if c['prompt'] in ('Prismáticos','Telescopio','Microscopio','Lupa','Cámara de fotos'):
            c['forbidden'][2:]=['Óptica','Observar']
        # Asociaciones comunes del ámbito, ajustadas a objetos, plantas y herramientas.
        if c['topic']=='herramientas y plantas':
            idx=[x['prompt'] for x in lex if x['topic']==c['topic']].index(c['prompt'])
            c['forbidden'][2:]=['Herramienta','Reparar'] if idx<27 else ['Planta','Naturaleza']
        if c['topic']=='hogar':
            c['forbidden'][2:]=['Ropa','Vestir'] if c['prompt'] in 'Sombrero|Gorra|Bufanda|Guante|Calcetín|Zapato|Bota|Sandalia|Zapatilla|Chancla|Camiseta|Camisa|Pantalón|Vaqueros|Falda|Vestido|Abrigo|Chaqueta|Jersey|Sudadera|Pijama|Bañador|Bikini|Corbata|Pajarita|Cinturón|Tirantes'.split('|') else c['forbidden'][2:]
    for c in names:
        c['difficulty']='easy' if c['prompt'] in familiar_people|simple_characters else 'hard' if c['topic']=='famosos' else 'medium'
    # Las pistas finales siempre son cuatro términos distintos y relevantes.
    for c in lex:
        seen=set();words=[]
        for word in c['forbidden']:
            if normalized(word) not in seen:words.append(word);seen.add(normalized(word))
        if len(words)<4 and c['topic']=='herramientas y plantas':
            for word in ['Jardín','Tierra','Cultivar']:
                if normalized(word) not in seen and len(words)<4:words.append(word);seen.add(normalized(word))
        assert len(words)==4,(c['prompt'],words)
        c['forbidden']=words
    reports={}
    reports['prohibido']=select('prohibido',lex+names+scene,initial,{'acciones y situaciones':180,'animales':100,'personajes':150,'cine y series':120,'famosos':100,'emociones y conceptos':70})
    drawing=[]
    for c in lex+names+scene:
        drawing.append({k:v for k,v in c.items() if k!='forbidden'})
    # Escenas reconocibles para dibujar, no emparejamientos aleatorios.
    for job,actions in JOBS.items():
        for action in actions:drawing.append(card(job+' '+action,'escenas de profesiones'))
    for animal,actions in ANIMAL_ACTIONS.items():
        for action in actions:drawing.append(card(animal+' '+action,'escenas de animales'))
    reports['dibujos']=select('dibujos',drawing,initial,{'acciones y situaciones':150,'escenas de profesiones':100,'escenas de animales':100,'animales':100,'personajes':130,'cine y series':100,'famosos':60,'emociones y conceptos':50})
    mime=[]
    for prompt in ACTIONS.strip().split('|'):mime.append(card(prompt,'acciones cotidianas','easy'))
    for prompt in HARD.strip().split('|'):mime.append(card(prompt,'desafíos y situaciones','hard'))
    for c in lex:
        if c['topic'] in ('animales','profesiones','fantasía','música y espectáculo','emociones y conceptos'):
            mime.append({k:v for k,v in c.items() if k!='forbidden'})
    for c in names:mime.append({k:v for k,v in c.items() if k!='forbidden'})
    for job,actions in JOBS.items():
        for action in actions:mime.append(card(job+' '+action,'escenas de profesiones'))
    for animal,actions in ANIMAL_ACTIONS.items():
        for action in actions:mime.append(card(animal+' '+action,'escenas de animales'))
    reports['mimica']=select('mimica',mime,initial,{'acciones cotidianas':470,'animales':120,'profesiones':75,'cine y series':120,'personajes':120,'famosos':60,'escenas de profesiones':170,'escenas de animales':170,'fantasía':35,'música y espectáculo':30,'desafíos y situaciones':100,'emociones y conceptos':20})
    tele=telepathy()
    animals='viva en una granja|viva en el mar|viva en un río|viva en un bosque|viva en una selva|viva en el desierto|viva en la sabana|viva en zonas frías|pueda volar|pueda nadar|pueda trepar|pueda saltar|tenga cuernos|tenga una cola larga|tenga manchas|tenga rayas|tenga plumas|tenga escamas|tenga caparazón|tenga patas largas|sea nocturno|sea una mascota|sea herbívoro|sea carnívoro|sea un ave|sea un reptil|sea un anfibio|sea un pez|sea un mamífero|sea un insecto|sea un arácnido|sea un molusco|sea un crustáceo|sea un marsupial|sea un primate|sea un roedor|sea un felino|aparezca en un cuento|aparezca en una película|asociéis con buena suerte'.split('|')
    for condition in animals:
        for prefix in ['Un animal que {condition}','Un animal que {condition} y os gustaría ver de cerca']:
            tele.append(card(prefix.format(condition=condition),'animales','hard' if condition in ('sea un molusco','sea un crustáceo','sea un arácnido','sea un marsupial') else 'easy'))
    contexts='un día de lluvia|una tarde de verano|un viaje largo|un cumpleaños|una fiesta de Navidad|un fin de semana|una excursión al campo|un rato en la playa|una tarde con amigos|una noche en casa|unas vacaciones de invierno|un día de mucho calor|una reunión familiar|una fiesta sorpresa|una mañana libre|una acampada|una fiesta de disfraces|una visita a una ciudad|un día sin Internet|una cita|una tarde con niños|una escapada romántica|un día sin dinero|una tarde en un parque|un viaje en tren|una espera en el aeropuerto|una sobremesa|una fiesta en la piscina|un descanso de trabajo|un día con nieve|una tarde de otoño|una clase de deporte|una tarde de juegos|un viaje en barco|un día de mucho viento|una visita al pueblo|un festival|un campamento|una fiesta de fin de curso|una cena entre amigos'.split('|')
    for context in contexts:
        tele.append(card('Una actividad que haríais durante '+context,'acciones y planes','easy'))
        tele.append(card('Una actividad que evitaríais durante '+context,'acciones y planes','medium'))
    # Temas algo menos cotidianos sin forzar respuestas únicas.
    for prompt in ['Un personaje de la mitología griega','Un personaje de la mitología nórdica','Un personaje de una novela de misterio','Un personaje de una novela de aventuras','Un personaje histórico del Renacimiento','Un personaje histórico de la antigua Roma','Un personaje histórico de la antigua Grecia','Un personaje histórico de Egipto','Un pintor impresionista','Un compositor del siglo XIX','Una científica de la historia','Un explorador del pasado','Un autor de ciencia ficción','Una especia usada en la India','Un plato de Oriente Medio','Un plato de la gastronomía coreana','Un plato de la gastronomía tailandesa','Un personaje de un western','Un personaje de una obra de Shakespeare','Un instrumento usado por un músico famoso']:
        tele.append(card(prompt,'temas difíciles','hard'))
    reports['telepatia']=select('telepatia',tele,initial,{'animales':80,'acciones y planes':80,'temas difíciles':20,'temas clásicos':100,'personajes de ficción':350,'personajes reales':260,'marcas':300,'gastronomía':300})
    reports['preguntas']=select('preguntas',trivia(),initial)
    report_path=ROOT/'scripts/content/report.json'
    report_path.write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(reports,ensure_ascii=True,indent=2))

if __name__=='__main__':main()
