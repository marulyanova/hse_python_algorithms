⚠️ Начиная с Python 3.3, значение хэша для строк, bytes и datetime по умолчанию непредсказуемо (рандомизировано) между запусками для повышения безопасности. Для чисел хэш обычно стабилен. В hash_table_tests.py используется в качестве тестовых ключей строки.

Запуск hash_table_tests.py
```python
PYTHONHASHSEED=0 pytest hash_table_tests.py
```