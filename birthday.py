def trace_birthday():
    
    data = "Alice:1990-04-05, Bob:1985-12-17, Charlie:1992-08-22, Diana:1988-03-14"
    
    
    pairs = data.split(", ")
    
   
    birthday_dict = {}
    
    
    for pair in pairs:
        
        name, birthday = pair.split(":")
        
       
        birthday_dict[name] = birthday
    
    
    name_to_trace = "Charlie"
    
    
    if name_to_trace in birthday_dict:
        print(f"{name_to_trace}'s birthday is on {birthday_dict[name_to_trace]}")
    else:
        print(f"{name_to_trace} not found in the birthday dictionary.")
    
    
    rejoined_string = ", ".join([f"{name}:{birthday}" for name, birthday in birthday_dict.items()])
    
    
    print("Rejoined string:", rejoined_string)


trace_birthday()
