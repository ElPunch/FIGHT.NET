import chromadb
import wikipediaapi
from sentence_transformers import SentenceTransformer

#primero definir que textos quieren recuperar 
#en base a consulta del usuario, recuperar esos documentos
model = SentenceTransformer('all-MiniLM-L6-v2')

wiki = wikipediaapi.Wikipedia(
    language='es',
    user_agent= 'chromadb-example/0.1.0' 
)

disciplina = ['MMA', 'Boxeo', 'Judo', 'Karate', 'Taekwondo', 'Lucha Libre', 'BJJ', 'Muay Thai', 'Kickboxing', 'Wrestling']

docs = []
for title in disciplina:
    page = wiki.page(title)
    if page.exists():
        docs.append({
            'content': page.text,
            'metadata': {'source': f"(title).pdf"}
        })

chromadb_client = chromadb.PersistentClient(path="colecciones")

collection = chromadb_client.get_or_create_collection('disciplina')


i = 0
ids = []
metadata = []
documents = []

for doc in docs:
    ids.append(str(i))
    metadata.append(doc['metadata'])
    documents.append(doc['content'])

embeddings = model.encode([doc['content'] for doc in docs])

collection.add(
    docuements=documents,
    embeddings=embeddings,
    ids=ids,
    metadata=metadata
)

