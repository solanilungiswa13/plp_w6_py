class Smartphone:
    def __init__(self, brand, model, os, storage_gb):
        self.brand = brand
        self.model = model
        self.os = os
        self.storage_gb = storage_gb
        self.apps = []

    def install_app(self, app_name):
        self.apps.append(app_name)

    def show_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, OS: {self.os}, Storage: {self.storage_gb}GB")
        print("Installed Apps:", self.apps)


class SmartPhoneWithCamera(Smartphone):  # Inheritance example
    def __init__(self, brand, model, os, storage_gb, camera_mp):
        super().__init__(brand, model, os, storage_gb)
        self.camera_mp = camera_mp

    def take_picture(self):
        print(f"Taking a picture with {self.camera_mp}MP camera.")


# Example usage
my_phone = Smartphone("Apple", "iPhone 14", "iOS", 256)
my_phone.install_app("Instagram")
my_phone.install_app("TikTok")
my_phone.show_specs()

my_camera_phone = SmartPhoneWithCamera("Google", "Pixel 7", "Android", 128, 50)
my_camera_phone.take_picture()
my_camera_phone.show_specs()