from model_interface.model_factory import ModelFactory

if __name__ == '__main__':

    # Получение данных
    model_name_1 = 'Qwen2-VL-2B'
    model_name_2 = 'Qwen2-VL-7B'
    model_family = 'Qwen2-VL'

    ModelFactory.register_model(model_family, 'model_qwen2_vl_example.models:Qwen2VL_model')

    model_init_params_1 = {
        'model_name': model_name_1,
        'system_prompt': '',
        'cache_dir': 'cache'
    }

    model_init_params_2 = {
        'model_name': model_name_2,
        'system_prompt': '',
        'cache_dir': 'cache'
    }

    model_1 = ModelFactory.get_model(model_family, model_init_params=model_init_params_1)
    model_2 = ModelFactory.get_model(model_family, model_init_params=model_init_params_2)
    print(model_1)
    model_1.print()
    print(model_2)
    model_2.print()

# model_qwen2-vl.models.Qwen2VL_model - путь к классу модели внутри python-пакета
# qwen2-vl - название семейства моделей
    