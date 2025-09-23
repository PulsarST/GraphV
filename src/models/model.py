from typing import List
from pydantic import BaseModel

from models.enums import GraphType


class Graph(BaseModel):
    id: int
    graph_type: GraphType
    relatives: List[int]


class GraphList:
    graphs: List[Graph]
