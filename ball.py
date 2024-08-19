import math

def ball_collide(ball1, ball2):
    """
    Determines if two balls are colliding.
    
    Parameters:
    ball1 (tuple): A tuple representing the first ball (x1, y1, r1) where (x1, y1) is the center and r1 is the radius.
    ball2 (tuple): A tuple representing the second ball (x2, y2, r2) where (x2, y2) is the center and r2 is the radius.
    
    Returns:
    bool: True if the balls are colliding, False otherwise.
    """
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    
   
    distance_between_centers = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    
    return distance_between_centers <= (r1 + r2)


ball1 = (0, 0, 5)
ball2 = (7, 0, 3)

colliding = ball_collide(ball1, ball2)
print(f"Are the balls colliding? {colliding}")
