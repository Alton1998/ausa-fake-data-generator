from faker import Faker
import secrets
import random


def gen_user_data(num=10):
    faker = Faker()
    for _ in range(num):
        user_data = dict()
        user_data['name'] = faker.name()
        user_data['id'] = secrets.token_hex(16)
        user_data['pwd'] = faker.password()
        user_data['address'] = faker.address()
        user_data['phone'] = faker.basic_phone_number()
        user_data['age'] = random.randrange(0,100)
        yield user_data

medicine_choice_list = ["Disaline Pricartax","Oluocine","Difil","Sodone Mal Heparideraletolex","Eque","Rotinavirosin","Pratec","Visalcin","Roxia-Duranupra-1a","Lope","Flol","Hydro","Kalorate","Diane","Estralinid","Zaglitone Benofuviriumaccar","Methalfateride","Ferix"]
def gen_prescription():
    prescription = ""
    for _ in range(random.randrange(1,4)):
        prescription = prescription + random.choice(medicine_choice_list) + "\n"
    return prescription

def gen_encounter(user_data):
    faker = Faker()
    for user in user_data:
        encounter = dict()
        vitals = dict()
        encounter["encounter_id"] = secrets.token_hex(16)
        encounter["user_id"] = user["id"]
        encounter["vitals"] = vitals
        encounter["date(UTC)"] = faker.date_time().strftime("%m/%d/%Y, %H:%M:%S")
        vitals["systolic_bp"] = random.randrange(80,200)
        vitals["diastolic_bp"] = random.randrange(50,90)
        vitals["temperature(Celsius)"] = random.randrange(80,120)
        encounter["comments"] = faker.text()
        encounter["prescription"] = gen_prescription()
        yield encounter


print("User Data")
user_list = list(gen_user_data(12))
for user in user_list:
    print(user)
print("Encounter Data")
for encounter in gen_encounter(user_list):
    print(encounter)