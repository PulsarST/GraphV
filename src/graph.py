from typing import List, Tuple
from pygame import Surface, Vector2
import pygame
import random

from models.model import GraphListModel, GraphModel


class Graph:
    def __init__(self, graph_model: GraphModel, radius: float = 10) -> None:
        self.id = graph_model.id
        self.pos: Vector2 = Vector2(0, 0)
        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.color = graph_model.graph_type
        pygame.draw.circle(
            self.image,
            graph_model.graph_type.lower(),
            (radius, radius),
            radius,
        )

        window_size: Tuple[int, int] = pygame.display.get_window_size()
        self.pos: Vector2 = Vector2(
            random.randint(0, window_size[0]),
            random.randint(0, window_size[1]),
        )

        self.relatives: List[int] = graph_model.relatives.copy()

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.pos.x - self.radius, self.pos.y - self.radius))

    def update(self) -> None: ...

    def to_model(self) -> GraphModel:
        return GraphModel(id=self.id, graph_type=self.color, relatives=self.relatives)


class GraphList:
    def __init__(self, graph_list: GraphListModel) -> None:
        self.graphs: List[Graph] = [
            Graph(graph_model) for graph_model in graph_list.models
        ]
        self.graph_by_id = {g.id: g for g in self.graphs}

    def update(self) -> None: ...

    def to_model(self) -> GraphListModel:
        return GraphListModel(models=[graph.to_model() for graph in self.graphs])

    def draw_edge(self, surface: Surface) -> None:
        for graph in self.graphs:
            for id in graph.relatives:
                if id in graph.relatives:
                    relative_graph = self.graph_by_id[id]
                    pygame.draw.line(surface, "black", graph.pos, relative_graph.pos, 2)

    def draw(self, surface: Surface) -> None:
        for graph in self.graphs:
            graph.draw(surface)

    def serialize(self, path: str) -> None:
        with open(file=path, mode="w", encoding="utf-8") as file:
            file.write(self.to_model().model_dump_json(indent=4))
