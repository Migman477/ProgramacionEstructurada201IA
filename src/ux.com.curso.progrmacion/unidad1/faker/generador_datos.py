#importar la libreria de Faker
from faker import Faker

faker = Faker("es_MX")

print("Generando datos Dummy")

print(f"Nombre : {faker.name()}")
print(f"Direccion : {faker.address()}")
print(f"Telefono : {faker.phone_number()}")
print(f"Correo : {faker.email()}")