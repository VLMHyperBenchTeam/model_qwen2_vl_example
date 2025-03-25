from typing import Any, List

from model_interface.model_interface import ModelInterface


class Qwen2VLModel(ModelInterface):
    """Реализация модели Qwen2VL, наследующая абстрактный класс ModelInterface.

    Этот класс предоставляет пример конкретной реализации класса для семейства моделей "Qwen2-VL".

    Attributes:
        model_name (str): Название модели как у разработчика (например, "Qwen2-VL-2B").
        system_prompt (str): Системный промпт, используемый моделью.
        cache_dir (str): Директория для кэширования данных модели.
        framework (str): Используемый фреймворк для инференса модели
                (например, "Hugging Face", "vLLM", "SGLang").
                Каждый унаследованный класс реализует объект модели
                привязанный к одному фреймворку инференса.
                Этот атрибут класса всегда задан разработчиком класса для модели.
                Атрибут не должен изменяться в процессе работы модели.
    """

    def __init__(self, model_name: str, system_prompt: str, cache_dir: str) -> None:
        """Инициализирует экземпляр Фабрики моделей.

        Args:
            model_name (str): Название модели как у разработчика (например, "Qwen2-VL-2B").
            system_prompt (str): Системный промпт, используемый моделью.
            cache_dir (str): Директория для кэширования данных модели.
        """
        super().__init__(model_name, system_prompt, cache_dir)
        self.framework = "Hugging Face"

    def predict_on_image(self, image: Any, question: str) -> str:
        """Реализация метода для предсказания на основе одного изображения.

        Args:
            image (Any): Изображение, на основе которого делается предсказание.
                        Тип может быть специфичным для реализации (например, PIL.Image, np.array и т.д.).
            question (str): Промпт-вопрос по изображению.

        Returns:
            str: Строка с ответом от модели.
        """
        return f"{self.model_name} predict_on_image"

    def predict_on_images(self, images: List[Any], question: str) -> str:
        """Реализация метода для предсказания на основе нескольких изображений.

        Args:
            images (List[Any]): Список изображений, на основе которых делается предсказание.
                               Тип элементов списка может быть специфичным для реализации.
            question (str): Промпт-вопрос по изображениям.

        Returns:
            str: Строка с ответом от модели.
        """
        return f"{self.model_name} predict_on_images"

    def print(self) -> None:
        """Выводит название модели.

        Этот метод используется для отладки или вывода информации о модели.
        """
        print(f"self.model_name: {self.model_name}")
        print(f"self.system_prompt: {self.system_prompt}")
        print(f"self.cache_dir: {self.cache_dir}")
        print(f"self.framework: {self.framework}")
