from typing import List
from pydantic import BaseModel

from models.enums import GraphType


class GraphModel(BaseModel):
    id: int
    graph_type: GraphType
    relatives: List[int]


class GraphListModel(BaseModel):
    models: List[GraphModel]
