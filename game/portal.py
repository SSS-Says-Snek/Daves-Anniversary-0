"""
This file is a part of the 'Unnamed' source code.
The source code is distributed under the MIT license.
"""

import itertools
from typing import List

import pygame

from game.common import TILE_HEIGHT, TILE_WIDTH
from game.states.enums import Dimensions


class Portal:
    def __init__(self, obj, dimensions: List[Dimensions]):
        self.image = pygame.Surface((obj.width, obj.height))
        self.rect = self.image.get_rect(topleft=(obj.x, obj.y))

        self.dimension_cycle = itertools.cycle(dimensions)
        self.current_dimension = next(self.dimension_cycle)
        self.dimension_change = False

    def update(self, player, events):
        self.dimension_change = False

        # if the player is standing next to the portal
        if self.rect.colliderect(player.rect):
            for event in events["events"]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        # switch to the next dimension
                        self.dimension_change = True
                        self.current_dimension = next(self.dimension_cycle)

    def draw(self, screen: pygame.Surface, camera):
        screen.blit(self.image, camera.apply(self.rect.topleft))
