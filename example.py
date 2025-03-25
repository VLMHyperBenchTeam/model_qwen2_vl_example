from typing import Any, Dict

from model_interface.model_factory import ModelFactory


def main() -> None:
    """Основная функция для демонстрации работы фабрики моделей.

    Эта функция регистрирует модель в фабрике, создает экземпляры моделей
    и выводит информацию о них.
    """
    # Имена моделей и семейство моделей
    model_name_1 = "Qwen2-VL-2B-Instruct"
    model_name_2 = "Qwen2-VL-7B-Instruct"
    model_family = "Qwen2-VL"

    # Регистрация модели в фабрике
    ModelFactory.register_model(
        model_family, "model_qwen2_vl_example.models:Qwen2VLModel"
    )

    # Параметры для инициализации первой модели
    model_init_params_1: Dict[str, Any] = {
        "model_name": model_name_1,
        "system_prompt": "path_to_system_prompt_1.txt",
        "cache_dir": "cache",
    }

    # Параметры для инициализации второй модели
    model_init_params_2: Dict[str, Any] = {
        "model_name": model_name_2,
        "system_prompt": "path_to_system_prompt_2.txt",
        "cache_dir": "cache",
    }

    # Создание объектов моделей
    model_1 = ModelFactory.get_model(
        model_family, model_init_params=model_init_params_1
    )
    model_2 = ModelFactory.get_model(
        model_family, model_init_params=model_init_params_2
    )

    # Вывод информации о моделях
    print(f"Создана Модель 1: {model_1}")
    model_1.print()
    dummy_result_1 = model_1.predict_on_image(
        image="path_to_image_1.jpg", question="Что изображено на картинке?"
    )
    print(f"Псевдо ответ от модели 1: {dummy_result_1}")

    print()
    print(f"Создана Модель 2: {model_2}")
    model_2.print()
    dummy_result_2 = model_2.predict_on_image(
        image="path-to_image_2.jpg", question="Что изображено на картинке?"
    )
    print(f"Псевдо ответ от модели 2: {dummy_result_2}")


if __name__ == "__main__":
    main()
