from smartphone import Smartphone, GamingPhone

def run_smartphone_demo():
    print("📱 Smartphone Demo")
    phone1 = Smartphone("Samsung", "Galaxy S22", 128)
    phone2 = GamingPhone("Asus", "ROG Phone 6", 256, "Ultra")

    phone1.specs()
    phone1.use()

    phone2.specs()
    phone2.use()

if __name__ == "__main__":
    run_smartphone_demo()
