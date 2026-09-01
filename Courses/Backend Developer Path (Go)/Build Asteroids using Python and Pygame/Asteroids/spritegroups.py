from typedgroup import TypedGroup
from traittypes import Drawable, Updatable

from asteroidfield import AsteroidField
from asteroid import Asteroid

from player import Player
from shot import Shot

# Each pygame sprite group container specializes in a different trait task:
updatables: TypedGroup[Updatable] = TypedGroup()
drawables: TypedGroup[Drawable] = TypedGroup()
asteroids: TypedGroup[Asteroid] = TypedGroup()
shots: TypedGroup[Shot] = TypedGroup()

# Containers specify which sprite group(s) instances automatically join:
AsteroidField.container = updatables
Asteroid.containers = updatables, drawables, asteroids
Shot.containers = updatables, drawables, shots
Player.containers = updatables, drawables
