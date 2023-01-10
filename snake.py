
class SnakePathFinder:

    def __init__(self, board:list[int], snake:list[list[int]]) -> None:
        self.board = board # [x, y]
        self.snake = snake

    def _print_paths(self, paths: list[tuple[list(),int]]) -> None:
        """ Guarda la lista de caminos en un archivo para poder visualizar los caminos generados."""

        with open('paths.txt', 'w') as file:
            file.write(f"Total Pahts: {len(paths)} \n")
            for path in paths:
                file.write(f"Snake: {path[0]}, movments: {path[1]} \n")


    def get_all_paths(self, depth:int, print_paths = False) -> int:
        """ Obtiene todos los caminos posible con la profundidad establecida dados un board y una snake."""

        possible_paths = [(self.snake, depth, '')]

        finished_paths = list()
        direction = ['R', 'L', 'D', 'U']

        while possible_paths:
            snake, remain_depth, path  = possible_paths.pop(0)

            if remain_depth == 0:
                finished_paths.append((snake, path))
            else:
                head = snake[0]
                next_movements = [[head[0]+1, head[1]],
                                  [head[0]-1, head[1]],
                                  [head[0], head[1]+1],
                                  [head[0], head[1]-1]]

                for idx, movement in enumerate(next_movements):
                    if 0 <= movement[0] < self.board[0] and 0 <= movement[1] < self.board[1] and movement not in snake[:-1]:
                        new_snake = snake[:-1]
                        new_snake.insert(0, movement)
                        possible_paths.append((new_snake,remain_depth - 1, path + direction[idx]))

        
        if print_paths: self._print_paths(finished_paths)

        return len(finished_paths)

                
