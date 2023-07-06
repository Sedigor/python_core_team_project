from faker import Faker
import random


fake = Faker()

def generate_phone_number():
    prefix = "+380"
    body = ""
    for _ in range(7):
        num = random.randint(0, 9)
        body += str(num)
    phone_number = prefix + body
    return phone_number
    

def create_fake_users(fake, n=20):
    users = []
    for _ in range(n):
        user = {}
        user["name"] = fake.name()
        user["phone"] = generate_phone_number()
        user["birthday"] = fake.date()
        user["email"] = fake.ascii_free_email()
        user["address"] = fake.street_address()
        users.append(user)
    return users


def random_user(users):
    user = random.choice(users)
    return user


if __name__ == '__main__':
    users = create_fake_users(fake)
    for user in users:
        print("| {:<25}|{:^16}|{:^16}|{:<16}|{:<16}".format(user["name"], 
                                                            user["phone"], 
                                                            user["birthday"], 
                                                            user["email"], 
                                                            user["address"]))
    user_1 = random_user(users)
    user_2 = random_user(users)