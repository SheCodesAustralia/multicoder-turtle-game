from World import World

WORLDS = [
    World(
        obstacle_positions=[
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)
        ],
        portal_position=(0, 5)
    ),
    World(
        obstacle_positions=[
            (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5)
        ],
        portal_position=(6, 10)
    ),
    World(
        obstacle_positions=[
            (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5)
        ],
        portal_position=(4, 3)
    )
]
