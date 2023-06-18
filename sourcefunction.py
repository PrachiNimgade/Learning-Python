def my_logic(source, destination, discount_rate, fare):
    return  f"Fare from{ source } to { destination } is { fare- (fare*discount_rate/100)} INR with has a applied discount of { discount_rate}%"
    
source = input("Pleased enter the source ")
destination = input("Pleased enter the destination ")
fare = float(input("Pleased enter the fare "))
discount_rate = float(input("Pleased enter the discount_rate in percentage "))


print (my_logic(source, destination, discount_rate, fare))
   