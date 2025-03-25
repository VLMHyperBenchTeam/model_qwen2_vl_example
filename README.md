# 🦾 Qwen2-VL Example — Демо-реализация интерфейса для VLM-моделей для VLMHyperBench

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/dependencies-poetry-green)](https://python-poetry.org/)

Это демонстрационный пакет для разработки VLM-моделей (Vision-Language Models).

Имитирует работу с семейством моделей **Qwen2-VL**, реализуя единый интерфейс из пакета [model-interface](https://github.com/VLMHyperBenchTeam/model_interface) для добавления их в `VLMHyperBench`([ссылка](https://github.com/VLMHyperBenchTeam/VLMHyperBench)).

**Содержит:**
- Учебный пример по разработке своего python-пакета(`model_qwen2_vl_example`) с абстрактным классом `ModelInterface` ([ссылка](https://github.com/VLMHyperBenchTeam/model_interface))
- Учебный пример создания объектов-имитаторов VLM-моделей (`example.py`)

## 🎯 Зачем это нужно?

Этот проект поможет:
1. Быстро освоить паттерн "Фабрика" с динамической регистрацией VLM моделей на производство в `ModelFactory`([ссылка](https://github.com/VLMHyperBenchTeam/model_interface))
2. Познакомится с разработкой python-пакетов для VLM для добавления их в `VLMHyperBench`([ссылка](https://github.com/VLMHyperBenchTeam/VLMHyperBench)).
3. Создать объекты-имитаторы VLM-моделей (`example.py`) и посмотреть их свойства.

## 🚀 Запуск проекта с Poetry

```bash
git clone https://github.com/VLMHyperBenchTeam/model_qwen2_vl_example.git
cd model_qwen2_vl_example
poetry install
```

## 📂 Структура проекта
```
model_qwen2_vl_example/
├── model_qwen2_vl_example/ - Пример python-пакета для VLM 
│   ├── __init__.py
│   └── models.py      — Реализация "шуточного" класса для VLM
├── example.py         — Демо-скрипт создающий имитаторы VLM
├── pyproject.toml     — Конфигурация проекта для Poetry
└── README.md          — Это описание
```

### 2. Пример python-пакета для VLM

Смотрите реализацию "учебного" класса `Qwen2VLModel` для VLM:

```
model_qwen2_vl_example/models.py
```

### 3. Пример работы

Файл `example.py` демонстрирует работу с моделью через абстрактный интерфейс.

Демонстрирует:
* Регистрацию модели в Фабрике `ModelFactory`
* Инициализацию параметров для VLM
* Создание объектов класса `Qwen2VLModel`
* Вывод информации о моделях

Пример вывода `example.py`

```
Создана Модель 1: <model_qwen2_vl_example.models.Qwen2VLModel object at 0x7fbcb362ffa0>
self.model_name: Qwen2-VL-2B-Instruct
self.system_prompt: path_to_system_prompt_1.txt
self.cache_dir: cache
self.framework: Hugging Face
Псевдо ответ от модели 1: Qwen2-VL-2B-Instruct predict_on_image

Создана Модель 2: <model_qwen2_vl_example.models.Qwen2VLModel object at 0x7fbcb362ff70>
self.model_name: Qwen2-VL-7B-Instruct
self.system_prompt: path_to_system_prompt_2.txt
self.cache_dir: cache
self.framework: Hugging Face
Псевдо ответ от модели 2: Qwen2-VL-7B-Instruct predict_on_image
```

## 🔗 Связанные проекты

### Использует:
* [model_interface](https://github.com/VLMHyperBenchTeam/model_interface) —  это гибкий python-пакет для унификации работы с VLM-моделями для `VLMHyperBench`([ссылка](https://github.com/VLMHyperBenchTeam/VLMHyperBench)).

### Примеры уже реализованных python-пакетов для VLM

1. **[model_qwen2-vl](https://github.com/VLMHyperBenchTeam/model_qwen2-vl)**

   Реальная реализация для семейства моделей Qwen2-VL:
   - Поддержка 2B/7B версий
   - Фреймворк Hugging Face
   - Обработка изображений с регулируемым разрешением
   - Примеры работы с документами (счета, накладные)

2. **[model_qwen2_5_vl](https://github.com/VLMHyperBenchTeam/model_qwen2.5-vl)**  
   Реальная реализация для семейства моделей Qwen2.5-VL:
   - Поддержка 3B/7B версий
   - Фреймворк Hugging Face
   - Обработка изображений с регулируемым разрешением
   - Примеры работы с документами (счета, накладные)
