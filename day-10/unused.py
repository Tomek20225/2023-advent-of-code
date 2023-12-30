from typing import TypeAlias

Location: TypeAlias = tuple[int, int] # (y, x)

# TODO: Make S not be treated as a vertex in every scenario
def get_polygon_vertices(points: list[Location]) -> list[Location]:
    vertices: list[Location] = [points[0]]
    last_y, last_x = points[0]
    movement_history = [0, 0, 0, 0] # N, E, S, W

    for i in range(1, len(points) + 1):
        # Compare last point with S
        point_y, point_x = points[i % len(points)]

        if last_y == point_y:
            # Moving from west to east
            if point_x > last_x:
                if movement_history[0] + movement_history[2] + movement_history[3] > 0:
                    vertices.append(points[i - 1])

                movement_history[0] = 0
                movement_history[1] += 1
                movement_history[2] = 0
                movement_history[3] = 0
            # Moving from east to west
            else:
                if movement_history[0] + movement_history[1] + movement_history[2] > 0:
                    vertices.append(points[i - 1])

                movement_history[0] = 0
                movement_history[1] = 0
                movement_history[2] = 0
                movement_history[3] += 1
        elif last_x == point_x:
            # Moving from north to south
            if point_y > last_y:
                if movement_history[0] + movement_history[1] + movement_history[3] > 0:
                    vertices.append(points[i - 1])

                movement_history[0] = 0
                movement_history[1] = 0
                movement_history[2] += 1
                movement_history[3] = 0
            # Moving from south to north
            else:
                if movement_history[1] + movement_history[2] + movement_history[3] > 0:
                    vertices.append(points[i - 1])

                movement_history[0] += 1
                movement_history[1] = 0
                movement_history[2] = 0
                movement_history[3] = 0

        last_y = point_y
        last_x = point_x
    
    return vertices