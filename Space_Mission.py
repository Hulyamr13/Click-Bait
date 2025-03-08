def initialize_grid_and_start_position(n):
    grid = []
    start_pos = None
    for i in range(n):
        row = input().split(' ')
        if 'S' in row:
            start_pos = (i, row.index('S'))
        grid.append(row)
    return grid, start_pos



n = int(input())

grid, (x, y) = initialize_grid_and_start_position(n)
resources = 100
grid_size = len(grid)

direction_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Mark the starting position as '.' when the first move is made
grid[x][y] = '.'

while True:
    command = input()
    dx, dy = direction_moves[command]
    new_x, new_y = x + dx, y + dy

    if not (0 <= new_x < grid_size) or not (0 <= new_y < grid_size):  # If out of bounds
        print(f"Mission failed! The spaceship was lost in space.")
        break

    resources -= 5  # Decrease resources by 5 for moving

    if grid[new_x][new_y] == 'R':
        resources = min(resources + 10, 100)  # Refuel up to 100

    elif grid[new_x][new_y] == 'M':
        resources -= 5  # Additional resource loss for meteorite
        grid[new_x][new_y] = '.'  # Destroy the meteorite

    # Update the spaceship's position
    x, y = new_x, new_y

    if grid[x][y] == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        break

    # Check for mission failure only after refueling, to allow refuel at 0 resources
    if resources < 5:
        print(f"Mission failed! The spaceship was stranded in space.")
        break

# Mark the last known position with 'S' if the mission didn't succeed
if grid[x][y] != 'P':
    grid[x][y] = 'S'

# Print the final grid state
for row in grid:
    print(*row, sep=' ')
