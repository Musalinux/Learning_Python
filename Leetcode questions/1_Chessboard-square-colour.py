"""
Determine the Color of a Chessboard Square
Problem: Given a chessboard coordinate (e.g., "a1" or "d5"), determine whether the square is black or white.
"""
def is_black_square(coordinate):
    # Convert column letter ('a' to 'h') to a number (1 to 8)
    col = ord(coordinate[0]) - ord('a') + 1  
    row = int(coordinate[1])  # Extract row number

    # If the sum of row + column is even, it's a black square
    return (col + row) % 2 == 0  

# Example usage
coordinate = input("Enter a chessboard square (e.g., a1, d4): ").lower()
if is_black_square(coordinate):
    print(f"The square {coordinate} is Black.")
else:
    print(f"The square {coordinate} is White.")
