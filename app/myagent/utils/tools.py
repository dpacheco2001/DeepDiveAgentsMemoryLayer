#Tools for the graph
from typing import Annotated, Literal, TypedDict
import uuid
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from langgraph.store.base import BaseStore
from langgraph.prebuilt import InjectedStore
from neo4j import GraphDatabase
from .models import Models
from . import prompts
from langchain_core.messages import SystemMessage, HumanMessage,ToolMessage
# Configuración de conexión a Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "mundial2022"  # Cambia esto por tu contraseña

# Crear el driver de Neo4j (se puede inicializar una sola vez al inicio de la aplicación)
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

model_with_tools = Models.get_model("gemini-2.0-flash")

@tool
def execute_query(query: str) -> list:
    """
    Herramienta: Ejecuta un query Cypher en la base de datos Neo4j.
    
    Args:
        query (str): El query Cypher a ejecutar.
    Returns:
        list: Lista de registros devueltos, donde cada registro es un diccionario.
              Si hay un error, devuelve una lista con un único diccionario que contiene el mensaje de error.
    """
    prompt = prompts.POST_PROCESS_QUERY
    response= model_with_tools.invoke([SystemMessage(content=prompt),HumanMessage(content=str(query))])
    response =response.content
    try:
        with driver.session() as session:
            result = session.run(response)
            return [record.data() for record in result]
    except Exception as e:
        # Return the error message in a format the agent can understand
        return [{"error": f"Error en la consulta: {str(e)}"}]