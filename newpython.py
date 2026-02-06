class CheckLogin:
    def __init__(self, func):
        # Jab hum @CheckLogin likhte hain, asli function yahan store ho jata hai
        self.func = func

    def __call__(self, *args, **kwargs):
        # Ye method tab chalta hai jab hum place_order() ko call karte hain
        logged_in = True
        
        if logged_in:
            print("Class Decorator: Login Checked. Access Granted!")
            return self.func(*args, **kwargs)
        else:
            print("Class Decorator: Access Denied!")

# Ab hum class ko decorator ki tarah use karenge
@CheckLogin
def place_order(item):
    print(f"Order placed for: {item}")

# Execution
place_order("Laptop")