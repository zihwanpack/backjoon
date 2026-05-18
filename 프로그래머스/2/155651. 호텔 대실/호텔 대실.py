def time_to_minutes(time):
    hour, minutes = map(int, time.split(':'))
    result = hour * 60 + minutes
    return result

def solution(book_time):
    bookings = sorted([(time_to_minutes(start), time_to_minutes(end) + 10) for start, end in book_time])
    rooms = []
    
    for start, end in bookings:
        
        allocated = False
        
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i] = end
                allocated = True
                break
        
        if not allocated:
            rooms.append(end)
            
    return len(rooms)