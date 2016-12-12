map = [[0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
       [0, 1, 0, 1, 0, 0, 0, 1, 0, 0], 
       [0, 0, 0, 1, 0, 0, 1, 0, 1, 0], 
       [1, 1, 1, 1, 0, 1, 1, 1, 1, 0], 
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
       [0, 1, 0, 0, 0, 0, 1, 0, 1, 1], 
       [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
       [0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
       [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]]

def escape_maze(map, dist_x, dist_y):
    # if we fail at first step... lol
    if len(map)== 0 or len(map[0]) == 0 or map[0][0] == 1:
        return 0

    # since map[0][0] is access able at this point
    queue = []
    step_count = 0
    # node define (value, y_axis, x_axis)
    visited = set()  
    queue.append((0,0))
    
    while len(queue) > 0:

        # get next status
        cur = queue[0]
        queue.pop(0)

        # check visited
        if cur in visited:
            continue
        visited.add(cur)
        
        # check if success
        # print cur
        if cur[0] == dist_x and cur[1] == dist_y:
            # return at first reach point,
            # because data in queue managed level - by level, the first result will be the shortest
            return step_count

        if cur[0] >= len(map) or cur[1] >= len(map[0]):
            continue

        # up
        if cur[0] - 1 >= 0 and map[cur[0] - 1][cur[1]] == 0:
            queue.append((cur[0] - 1, cur[1]) )
        # left
        if cur[1] - 1 >= 0 and map[cur[0]][cur[1] - 1] == 0:
            queue.append((cur[0], cur[1] + 1))
        # down
        if cur[0] + 1 < len(map) and map[cur[0] + 1][cur[1]] == 0:
            queue.append((cur[0] + 1, cur[1]))
        # right
        if cur[1] + 1 < len(map[0]) and map[cur[0]][cur[1] + 1] == 0:
            queue.append((cur[0], cur[1] + 1 ))

        step_count += 1
    # can not reach
    return -1

print escape_maze(map, 0,0)