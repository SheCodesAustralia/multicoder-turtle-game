from World import World

WORLDS = [
    ##
    World(
        obstacle_positions=[
            (0, 7), (1, 7), (2, 1), (2, 2), (3, 2), (3, 6), (4, 6),
            (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 9),
            (5, 10), (6, 9), (7, 3), (7, 4), (7, 5), (7, 6), (7, 9),
            (8, 6), (9, 0), (9, 1), (9, 4), (9, 6), (10, 6)
        ],
        portal_position=(10, 0),
        bird_start_position=(10, 10),
        food_position=(1, 10)
    )
    ##
]
