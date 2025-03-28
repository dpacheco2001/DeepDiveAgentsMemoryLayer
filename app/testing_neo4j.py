
from neo4j import GraphDatabase
from langchain_core.messages import SystemMessage
# Configura los detalles de conexión a Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "mundial2022"  # Cambia esto según tu configuración

# Crea el driver de Neo4j (esto se puede hacer al inicio de la aplicación)
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def run_cypher_query(query: str, parameters: dict = None):
    """
    Ejecuta una consulta Cypher en Neo4j y retorna los resultados.
    """
    with driver.session() as session:
        result = session.run(query, parameters or {})
        return list(result.data())
    

query = """
MATCH (n)
WHERE n:CasoEstudio OR n:AsistenteVirtual OR n:Ensayo OR n:Concepto OR n:Comportamiento OR n:Tarea OR n:Herramienta
RETURN n
"""

results = run_cypher_query(query)
memory_summary = "He recuperado las siguientes memorias importantes:\n"
for record in results:
    node = record["n"]  # Already a dictionary with node properties
    # We don't have labels from the dict, so we skip that part
    memory_summary += f"Propiedades: {node}\n"

print(memory_summary)