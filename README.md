<div align="center">
    <h1>⏱️ tictac</h1>
    <img height="20" alt="Python 3.8+" src="https://img.shields.io/badge/python-3.8+-blue">
    <img height="20" alt="License MIT" src="https://img.shields.io/badge/license-AGPL--v3-orange">
    <img height="20" alt="Status" src="https://img.shields.io/badge/status-stable-brightgreen">
    <p>
        <img height="20" alt="PyPI Downloads" src="https://static.pepy.tech/personalized-badge/tictac-timer?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=RED&left_text=downloads">
    </p>
    <p><strong>tictac</strong> - a simple timer for your code</p>
    <blockquote>(─‿‿─)</blockquote>
</div>

---

```
   __  _      __            
  / /_(_)____/ /_____ ______
 / __/ / ___/ __/ __ `/ ___/
/ /_/ / /__/ /_/ /_/ / /__  
\__/_/\___/\__/\__,_/\___/  
                            
```


## установка

```
pip install tictac-timer
```

## быстрый старт

```python
from tictac import timer
import time

# context manager
with timer("Загрузка данных"):
    time.sleep(1.2)
    # [tictac] Загрузка данных: 1.20 sec

# decorator
@timer
def heavy_process():
    time.sleep(0.5)
    # [tictac] heavy_process: 0.50 sec

# decorator с параметрами
@timer("Обработка", unit="ms")
def fast_process():
    time.sleep(0.01)
    # [tictac] Обработка: 10.00 ms
```

## параметры

```python
timer(name=None, unit="s", output=None)
```

- **name** — label для таймера (по умолчанию имя функции)
- **unit** — единица измерения: `"s"`, `"ms"`, `"min"`
- **output** — callback `(msg: str) -> None` (по умолчанию `print`)

## примеры

### кастомный вывод

```python
import logging

log = logging.getLogger(__name__)

with timer("query", output=log.info):
    db.execute("SELECT ...")
```

### несколько таймеров

```python
with timer("preparation"):
    time.sleep(0.3)

with timer("processing", unit="ms"):
    time.sleep(15)

# [tictac] preparation: 0.30 sec
# [tictac] processing: 15.00 ms
```

## лицензия

[AGPL-3.0](LICENSE)
