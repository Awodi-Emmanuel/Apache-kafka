from faker import Faker

fake = Faker()

def get_registered_user():
    return  {
        "Firstname": fake.name(),
        "Address": fake.address(),
        "Date": fake.year()
        
    }
    
    
    
if __name__ == "__main__":
    print(get_registered_user())