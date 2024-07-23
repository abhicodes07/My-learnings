class Address:
    def __init__(self, street, block):
        self.street = street
        self.block = block
        self.address = f"{street}, {block}, Jaipur, Rajasthan"



emp1 = Address("West side street", "block-2")
print(f"Employee1 street name: {emp1.street}")
print(f"Employee1 block name: {emp1.block}")
print(f"Employee1 full address: {emp1.address}")


emp1.street = "East side street"
emp1.block = "Block 4"
print(f"Street: {emp1.street}")
print(f"Block: {emp1.block}")
print(f"Address: {emp1.address}")
