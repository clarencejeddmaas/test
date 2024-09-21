import random

def lottery_style_max(boxes, num_iterations):
    max_number = float('-inf')  # Start with the lowest possible number
    
    for _ in range(num_iterations):
        selected_boxes = random.sample(boxes, 10)  # Randomly select 10 boxes
        local_max = max(selected_boxes)  # Find the maximum in selected boxes
        
        if local_max > max_number:
            max_number = local_max  # Update overall max if local max is greater
    
    return max_number

# Example usage
boxes = [random.randint(1, 1000000) for _ in range(1000000)]
largest_number = lottery_style_max(boxes, 100)  # Check 100 iterations
print(f"Largest number found: {largest_number}")
