"""Importación editorial puntual; nunca se ejecuta en la aplicación ni usa una API."""
import json,re,zipfile
from pathlib import Path

root=Path(__file__).resolve().parent.parent
upstream=root/'tmp/content/quizify-main'
records=[]
excluded=[]
for path in sorted((upstream/'custom_components/quizify/questions').glob('*-es.json')):
    if path.name in ('imagenes-es.json','estimacion-es.json'): continue
    for q in json.loads(path.read_text(encoding='utf-8'))['questions']:
        question=q['question'].strip()
        answers=q.get('answers',[])
        reason=None
        if q.get('type')=='estimate' or q.get('image_url'): reason='requiere estimación o imagen'
        elif len(answers)!=3 or sum(bool(a.get('correct')) for a in answers)!=1: reason='formato incompatible'
        elif len(question)>260: reason='texto demasiado largo para una prueba de 30 segundos'
        elif re.search(r'actualmente|en la actualidad|a día de hoy|hasta ahora|el último mundial|la última edición|hoy en día',question,re.I): reason='dato temporal'
        elif re.search(r'récord|más (?:medallas|títulos|partidos|goles|seguidores)|más taquillera|más vendido|mejor pagad',question,re.I) and not re.search(r'\b(?:19|20)\d{2}\b',question): reason='récord sin referencia temporal'
        elif any(len(a['text'])>130 or re.search(r'anteriores|las dos|ambas|la primera|la segunda|A y B|A, B',a['text'],re.I) for a in answers): reason='respuesta dependiente de opciones'
        if reason:
            excluded.append({'id':q['id'],'file':path.name,'reason':reason});continue
        records.append({'id':q['id'],'file':path.name,'question':question,'answers':answers,'difficulty':q.get('difficulty','medium'),'topic':q.get('category',path.stem),'fact':q.get('fun_fact','')})
commit=zipfile.ZipFile(root/'tmp/content/quizify.zip').comment.decode('ascii')
output={'source':'https://github.com/mholzi/quizify','commit':commit,'license':'MIT','records':records,'excluded':excluded}
(root/'scripts/content/trivia-source.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(root/'public/quizify-license.txt').write_text((upstream/'LICENSE').read_text(encoding='utf-8'),encoding='utf-8')
print('Importadas:',len(records),'Excluidas:',len(excluded),'Revisión:',commit)
