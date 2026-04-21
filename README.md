# 🎮 Custom DirectX

<img width="1920" height="1048" alt="image" src="https://github.com/user-attachments/assets/d9621718-3a6d-453f-9f04-3bf6492857c8" />

---

## 📋 Описание

**Custom DirectX** — это графическое приложение на Python с использованием `customtkinter`, которое позволяет:
- 🔧 Устанавливать 4 различных версии DirectX
- ⚡ Применять более **50 оптимизаций** реестра для повышения производительности в играх
- 🎮 Улучшать совместимость со старыми и новыми играми
- 🖥️ Настраивать параметры DirectX 11/12, DirectDraw, MMX, AGP, Vulkan и OpenGL
- 🔄 Возвращать все настройки к стандартным (DirectX Default)
- 💻 Поддержка **CLI аргументов** для автоматизации

---

## 🚀 Установка

1. [ Скачайте последний релиз](https://github.com/anton18-png/Custom-DirectX/releases/download/v3.1/DirectX_Optimizer.exe)
2. Запустите `Custom_DirectX_V3.exe` **от имени Администратора**

## 🎯 Использование

### Установка DirectX

Приложение поддерживает установку 4 версий DirectX:

| Версия | Команда | Описание |
|--------|---------|----------|
| **Standard DirectX** | `StandardDirectX.exe /q` | Официальная версия от Microsoft (90% пользователей) |
| **DirectX For ProOS** | `cd DirectXForProOS && DXSETUP.exe /silent` | Альтернативная версия для профессиональных сборок |
| **DirectX Game Edition** | `DirectXGameEdition.exe /q` | Версия из папки Redist игровых установщиков |
| **DirectX MartyFiles Edition** | `DirectXMartyFilesEdition.exe` | Специальная редакция от WinClick (не отображается в списке программ) |

## 💻 CLI Аргументы

Программа поддерживает запуск из командной строки без графического интерфейса:

### Синтаксис

```batch
main.pyw [--StandardDirectX] [--DirectXGameEdition] [--DirectXMartyFilesEdition] [--DirectXForProOS] [-at] [-ut]
```

### Аргументы

| Аргумент | Сокращение | Описание |
|----------|------------|----------|
| `--StandardDirectX` | — | Установить Standard DirectX |
| `--DirectXGameEdition` | — | Установить DirectX Game Edition |
| `--DirectXMartyFilesEdition` | — | Установить DirectX MartyFiles Edition |
| `--DirectXForProOS` | — | Установить DirectX For ProOS |
| `--alltweaks` | `-at` | Применить все твики |
| `--untweaks` | `-ut` | Удалить все твики (DirectX Default) |

### Примеры использования

```batch
# Запуск GUI (без аргументов)
DirectX_Optimizer.exe

# Установка только Standard DirectX
DirectX_Optimizer.exe --StandardDirectX

# Установка Game Edition и применение всех твиков
DirectX_Optimizer.exe --DirectXGameEdition -at

# Только применить все твики
DirectX_Optimizer.exe -at

# Только удалить все твики
DirectX_Optimizer.exe -ut

# Установить Standard DirectX и удалить твики
DirectX_Optimizer.exe --StandardDirectX -ut

# Комбинация: установка + твики
DirectX_Optimizer.exe --DirectXGameEdition --StandardDirectX -at
```

---

## 📋 Список твиков

### DirectX твики

| № | Твик | Описание |
|---|------|----------|
| 1 | Game+Performance Mode | Включение игрового режима и режима производительности |
| 2 | DDSCAPS Acceleration | Аппаратное ускорение обработки поверхностей |
| 3 | DirectDraw Hardware | Аппаратное ускорение DirectDraw |
| 4 | MIDI Hardware | Аппаратное ускорение для MIDI |
| 5 | Hardware Point Sprites | Аппаратное ускорение точечных объектов |
| 6 | Hardware Rasterizer | Аппаратные средства растеризации |
| 7 | Hardware State Blocks | Обработка stateblocks видеодрайвером |
| 8 | Reference Driver | Образцовый драйвер программной прорисовки |
| 9 | RAMP Driver | Драйвер программной RAMP-прорисовки |
| 10 | NULL Device | Драйвер "NULL Device" |
| 11 | DirectX Libraries | Дополнительные библиотеки DirectX |
| 12 | AGP Texturing | Поддержка AGP текстурирования |
| 13 | Non-Local Video Memory | Использование нелокальной видеопамяти |
| 14 | MMX Instructions | Поддержка процессорных команд MMX |
| 15 | MMX Fast Path | Быстрый MMX путь |
| 16 | MMX for RGB | Использование MMX для режима эмуляции RGB |
| 17 | EnumSeparateMMX | Драйвер прорисовки с MMX |
| 18 | Few Vertices | Оптимизация для малого количества вершин |
| 19 | Disable VSync | Отключение вертикальной синхронизации |
| 20-24 | Debug Disable | Отключение всех видов отладки (5 твиков) |
| 25 | Disable NoSysLock | Отключение принудительного NoSysLock |
| 26 | Disable ModeX | Отключение режима совместимости EGA |
| 27 | Enable PrintScreen | Реакция на клавишу PrintScreen |
| 28 | VRAM Buffer | Увеличение быстродействия VRAM |
| 29 | Reduce Latency | Уменьшение задержек DirectX |
| 30-45 | D3D11/D3D12 Optimizations | 16 оптимизаций для современных версий DirectX |

### Vulkan твики

| № | Твик | Описание |
|---|------|----------|
| 1 | Vulkan Shader Cache | Включение кэша шейдеров Vulkan |
| 2 | Vulkan Topology Support | Включение виртуальной топологии |

### OpenGL твики

| № | Твик | Описание |
|---|------|----------|
| 1 | OpenGL Optimizations | Базовые оптимизации OpenGL (DisableAsync, MultisampleBuffers и др.) |
| 2 | OpenGL Buffer Size | Увеличение буферов OpenGL до 4MB/2MB/1MB для AMD/Intel/NVIDIA/ATI |
| 3 | OpenGL Driver Settings | Переменные окружения GPU_MAX_HEAP_SIZE и др. |

---

## 📜 Лицензия

MIT License — свободное использование, модификация и распространение.
