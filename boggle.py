def make_grid(width, height):
    """Create the grid that will hold all titles for the boggle game"""
    return {(row, col): " " for row in range(height)
        for col in range(width)}