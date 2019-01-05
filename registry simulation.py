import sys  
import os

registers = list()

class Register:
  def __init__(self, reg_number, reg_type, customers):
    self.reg_number = reg_number
    self.reg_type = reg_type
    self.customers = []

  def set_reg_number(reg_number):
    self.reg_number = reg_number

  def get_reg_number():
    return reg_number
  
  def set_reg_type(reg_type):
    self.reg_type = reg_type

  def get_reg_type():
    return self.reg_type

  def set_customers(customers):
    self.customers = customers

  def get_customers():
    return customers

class Customer:
  def __init__(self, cust_type, cust_time, cust_items):
    self.cust_type = cust_type
    self.cust_time = cust_time
    self.cust_items = cust_items
    
  def set_cust_type(cust_type):
    self.cust_type = cust_type

  def get_cust_type():
    return cust_type
  
  def set_cust_items(cust_items):
    self.cust_items = cust_items

  def get_cust_items():
    return self.cust_items

  def set_cust_time(cust_time):
    self.cust_time = cust_time

  def get_cust_time():
    return cust_time

def create_registers(num_of_registers):
  for number in xrange(1,num_of_registers):
    register = Register(number, "regular", 0)
    registers.append(register)
  training_register = Register(num_of_registers, "training", 0)
  registers.append(training_register)

def add_customer_b_to_first_register(customer, target_registers):
  lowest_number = 0
  target = None
  count = 0
  for register in target_registers:
    if count == 0:
      count+=1
      lowest_number = register.reg_number
      target = register
      
    if register.reg_number < lowest_number:
      lowest_number = register.reg_number
      target = register

  target.customers.append(customer)

def add_customer_a(customer):
  count = 0;
  first_minimum = 0;
  target_registers = [None]
  for register in registers:
    if count == 0:
      count+=1
      first_minimum = len(register.customers)
      target_registers[0] = register
    else:
      if len(register.customers) == first_minimum:
        first_minimum = len(register.customers)
        target_registers.append(register)
      if len(register.customers) < first_minimum:
        first_minimum = len(register.customers)
        target_registers = [register]

  if len(target_registers) == 1:
    target = target_registers[0]
  else:
    # do for unordered register
    add_customer_b_to_first_register(customer, target_registers) 

def add_customer_b(customer):
  count = 0;
  target = None
  first_min = 0
  for register in registers:
    if count == 0:
      first_min = register.customers[len(customers-1)].cust_items

    if register.customers[len(customers-1)].cust_items == 0:
      target = register  
      return
    else:
      if first_min > register.customers[len(customers-1)].cust_items:
        first_min = register.customers[len(customers-1)].cust_items 
        target = register
    target.customers.append(customer)

def add_customer_to_register(customer):

  if customer.cust_type == "A":
    # add_customer_a
    add_customer_a(customer)
  else:
    # add_customer_b
    add_customer_b(customer)

def register_timer(registers): #this isnt right still working on it
  our_t = 0
  register_time=0
  for register in registers:
    if register.reg_type == 'regular':
      for register.customers in register:
        if register.customers.cust_time > register_time:
          customer_time_at_register = register.customers.cust_time + (1* register.customers.cust_items)
          register_time =register_time + customer_time_at_register 

        elif register.customers.cust_time == register_time:
          customer_time_at_register = 1* register.customers.cust_items
          register_time =register_time + customer_time_at_register 
        else:
          customer_time_at_register =(register_time - register.customers.cust_time) + (1* register.customers.cust_items)
          register_time =register_time + customer_time_at_register 

    else:
      for register.customers in register:
        if register.customers.cust_time > register_time:
          customer_time_at_register = register.customers.cust_time + (2* register.customers.cust_items)
          register_time =register_time + customer_time_at_register 

        elif register.customers.cust_time == register_time:
          customer_time_at_register = 2* register.customers.cust_items
          register_time =register_time + customer_time_at_register 
        else:
          customer_time_at_register =(register_time - register.customers.cust_time) + (2* register.customers.cust_items)
          register_time =register_time + customer_time_at_register 

        
      
      

def main():  
   filepath = "demofile.txt"

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   with open(filepath) as fp:
       count = 1
       for line in fp:
           if count == 1:
            num_of_registers = int(line)
            create_registers(num_of_registers)
           else:
            # create a customer
            customer_info = line.split()
            customer = Customer(customer_info[0], customer_info[1], customer_info[2])

            # Add customer to queue          
            add_customer_to_register(customer)

            print("Customer info is {}".format(customer_info))
           count += 1

       print("We have {} registers".format(num_of_registers))

       for register in registers:
         print("-------------------------")
         print(register.reg_number)
         print(register.reg_type)
         print(len(register.customers))
         print(register.customers)
         print("------------------------")

if __name__ == '__main__':  
  main()
