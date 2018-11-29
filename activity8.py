import csv



class Customer:
    def __init__(self,id, firstName, lastName, company, address, city, state, zip):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def getname(self):
        name = str(self.firstName + " " + self.lastName)
        return name

    def getadd(self):
        return self.address

    def getcompany(self):
        return self.company

    def getlocation(self):
        location = str(self.city + "," + self.state + " " + self.zip)
        return location


def display_title():
    print("Customer Viewer");



customerlist=[]

def csv_reader():
 data = open('customers.csv')
 customers = csv.reader(data)
 for customer in customers:
    if customers.line_num == 1:
        continue;
    else:
        id = customer[0]
        firstname = customer[1]
        lastname = customer[2]
        company = customer[3]
        address = customer[4]
        city = customer[5]
        state = customer[6]
        zip = customer[7]
        customerlist.append(Customer(id, firstname, lastname, company, address, city, state, zip))
 data.close()

def find_customer(cust_id):
 if cust_id=="":
     return ('No Customer with that specified ID.')
 if 100 < int(cust_id) < 601:
   csv_reader()
   for n in customerlist :
     if n.id == cust_id:
      return n;
      print(Customer.getname(n))
      if n.company != "":
       print(Customer.getcompany(n))
      print(Customer.getadd(n))
      print(Customer.getlocation(n))
     if 0 > int(cust_id) > len(customerlist):
      print('No Customer with that specified ID.')
 else:
    return ('No Customer with that specified ID.')



def find_customers(ID):
 if 100 < int(ID) < 601:
    for n in customerlist :
     if n.id == ID:
       print(Customer.getname(n))
       if n.company != "":
           print(Customer.getcompany(n))
       print(Customer.getadd(n))
       print(Customer.getlocation(n))
       choice = input("\n continue? (y/n): ")
       if choice != "y":
           print("Bye")
           break;
       else:
           Id = input("Enter Customer ID: ")
           find_customers(Id)
 else:
     print('No Customer with that specified ID.')
     choice = input("\n Continue? (y/n): ")
     if choice != "y":
         print("Bye")
     else:
         Id = input("Enter Customer ID: ")
         find_customers(Id)


def main():
    display_title()
    cust_id = input("Enter Customer ID:")
    csv_reader()
    find_customers(cust_id)





if __name__ == '__main__':
    main()




