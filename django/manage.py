#!/usr/bin/env python
"""
Файл управления Django проектом
Этот файл является точкой входа для выполнения административных задач Django
"""
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """
    Основная функция для запуска административных команд Django
    Настраивает переменные окружения и выполняет команды управления
    """
    # Установка модуля настроек Django
    # 'greeting_project.settings' - это путь к файлу настроек проекта
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greeting_project.settings')
    try:
        # Импорт функции execute_from_command_line из Django
        # Эта функция обрабатывает все команды управления Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Обработка ошибки импорта Django
        # Если Django не установлен, выводится сообщение об ошибке
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Выполнение команды, переданной через командную строку
    # sys.argv содержит аргументы командной строки
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

