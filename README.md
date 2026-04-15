# 🎮 DirectX Installer & Optimized Tweaker

<img width="1912" height="1042" alt="image" src="https://github.com/user-attachments/assets/595a22d4-572e-4d3b-9c86-e994ff4065d4" />

## 📋 Описание

**DirectX Installer & Optimized Tweaker** — это графическое приложение на Python с использованием `customtkinter`, которое позволяет:

- 🔧 Устанавливать 4 различных версии DirectX
- ⚡ Применять более 40 оптимизаций реестра для повышения производительности в играх
- 🎮 Улучшать совместимость со старыми и новыми играми
- 🖥️ Настраивать параметры DirectX 11/12, DirectDraw, MMX, AGP и многое другое
- 🔄 Возвращать все настройки к стандартным (DirectX Default)

---

## 🚀 Установка

1. [ Скачайте последний релиз](https://github.com/anton18-png/Custom-DirectX/releases/download/v3/Custom_DirectX_V3.exe)
2. Запустите `Custom_DirectX_V3.exe` **от имени Администратора**

## 🎯 Использование

### 1. Установка DirectX

Приложение поддерживает установку 4 версий DirectX:

| Версия | Команда | Описание |
|--------|---------|----------|
| **Standard DirectX** | `StandardDirectX.exe /q` | Официальная версия от Microsoft (90% пользователей) |
| **DirectX For ProOS** | `cd DirectXForProOS && DXSETUP.exe /silent` | Альтернативная версия для профессиональных сборок |
| **DirectX Game Edition** | `DirectXGameEdition.exe /q` | Версия из папки Redist игровых установщиков |
| **DirectX MartyFiles Edition** | `DirectXMartyFilesEdition.exe` | Специальная редакция от WinClick (не отображается в списке программ) |

### 2. Применение твиков

Все твики разделены на категории:

#### 🎮 Основные твики
- Game+Performance Mode
- Кэш шейдеров DX-Vulkan
- Отключение VSync
- Few Vertices оптимизация
- Включение PrintScreen
- Улучшение DX-Vulkan
- Уменьшение задержек
- Отключение NoSysLock
- Отключение ModeX

#### 🧠 MMX оптимизации
- Включение MMX инструкций
- MMX Fast Path
- MMX для RGB
- EnumSeparateMMX

#### 🖥️ AGP и видеопамять
- AGP Texturing
- Нелокальная видеопамять (AGP Aperture/PCIe BAR)
- Увеличение VRAM буфера

#### 🎨 Драйверы программной прорисовки
- Reference Driver
- RAMP Driver
- NULL Device

#### ⚡ Аппаратное ускорение
- Hardware Point Sprites
- Hardware State Blocks
- Hardware Rasterizer
- DDSCAPS Acceleration
- DirectDraw Hardware
- MIDI Hardware

#### 🐛 Отключение отладки
- Disable Debugging
- Disable FullDebug
- Disable Debug Monitor
- Disable Multimon Debug
- Disable Debug Runtime

#### 🎮 D3D11/D3D12 оптимизации
- Graphics Settings (SwapEffectUpgradeCache, SpecificGPUOptionApplicable)
- D3D12 Unsafe Command Buffer
- D3D12 Runtime Optimizations
- D3D12 Resource Alignment
- D3D11/D3D12 Multithreaded
- D3D11/D3D12 Deferred Contexts
- D3D11/D3D12 Allow Tiling
- D3D11 Dynamic Codegen
- D3D12 CPU Page Table
- D3D12 Heap Serialization
- D3D12 Map Heap Allocations
- D3D12 Residency Management

### 3. Управление твиками

- **✅ ПРИМЕНИТЬ ВСЕ ТВИКИ** — применяет все доступные оптимизации одной кнопкой
- **🔄 DIRECTX DEFAULT** — удаляет ВСЕ твики и возвращает стандартные настройки Windows

---

## 📜 Лицензия

MIT License — свободное использование, модификация и распространение.
