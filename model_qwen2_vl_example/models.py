from model_interface.model_interface import ModelInterface

class Qwen2VL_model(ModelInterface):
    def predict_on_image(self, image, question):
        """Метод для предсказания по одному изображению."""
        print(f"{self.model_name} predict_on_image")

    def predict_on_images(self, images, question):
        """Метод для предсказания по нескольким изображениям."""
        print(f"{self.model_name} predict_on_images")

    def print(self):
        print(self.model_name)
        