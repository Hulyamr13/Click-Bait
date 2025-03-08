from collections import deque

def process_engagement(suggested_links, featured_articles, target_value):
    suggested_queue = deque(suggested_links)  # FIFO
    featured_stack = list(featured_articles)  # LIFO
    final_feed = []
    
    while suggested_queue and featured_stack:
        suggested = suggested_queue.popleft()
        featured = featured_stack.pop()
        
        if suggested > featured:
            remainder = suggested % featured
            final_feed.append(-remainder)
            if remainder > 0:
                suggested_queue.append(remainder * 2)  # Return to FIFO
        elif featured > suggested:
            remainder = featured % suggested
            final_feed.append(remainder)
            if remainder > 0:
                featured_stack.append(remainder * 2)  # Return to LIFO
        else:
            final_feed.append(0)  # Equal values, add 0, no remainder added back
    
    total_engagement = sum(final_feed)
    print(f"Final Feed: {', '.join(map(str, final_feed))}")
    
    if total_engagement >= target_value:
        print(f"Goal achieved! Engagement Value: {total_engagement}")
    else:
        shortfall = target_value - total_engagement
        print(f"Goal not achieved! Short by: {shortfall}")

# Handling single test case as expected
if __name__ == "__main__":
    suggested_links = list(map(int, input().split()))
    featured_articles = list(map(int, input().split()))
    target_value = int(input())
    process_engagement(suggested_links, featured_articles, target_value)
