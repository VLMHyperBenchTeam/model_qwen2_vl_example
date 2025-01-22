from model_interface.model_factory import ModelFactory
from typing import Dict, Any


def main() -> None:
    """Основная функция для демонстрации работы фабрики моделей.

    Эта функция регистрирует модель в фабрике, создает экземпляры моделей
    и выводит информацию о них.
    """
    # Имена моделей и семейство моделей
    model_name_1 = "Qwen2-VL-2B"
    model_name_2 = "Qwen2-VL-7B"
    model_family = "Qwen2-VL"

    # Регистрация модели в фабрике
    ModelFactory.register_model(
        model_family, "model_qwen2_vl_example.models:Qwen2VL_model"
    )

    # Параметры для инициализации первой модели
    model_init_params_1: Dict[str, Any] = {
        "model_name": model_name_1,
        "system_prompt": "",
        "cache_dir": "cache",
    }

    # Параметры для инициализации второй модели
    model_init_params_2: Dict[str, Any] = {
        "model_name": model_name_2,
        "system_prompt": "",
        "cache_dir": "cache",
    }

    # Создание экземпляров моделей
    model_1 = ModelFactory.get_model(
        model_family, model_init_params=model_init_params_1
    )
    model_2 = ModelFactory.get_model(
        model_family, model_init_params=model_init_params_2
    )

    # Вывод информации о моделях
    print(f"Модель 1: {model_1}")
    model_1.print()

    print(f"Модель 2: {model_2}")
    model_2.print()


if __name__ == "__main__":
    main()
