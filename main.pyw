import subprocess
import os
import sys
import tkinter.messagebox as messagebox
import customtkinter as ctk
from pathlib import Path

# Настройка темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class DirectXInstallerApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("DirectX Installer & Optimized Tweaker")
        self.root.geometry("900x1000")
        self.root.minsize(800, 900)
        
        # Установка иконки
        icon_path = Path("icon.ico")
        if icon_path.exists():
            try:
                self.root.iconbitmap(icon_path)
            except:
                pass
        
        # Кастомные цвета
        self.primary_color = "#2e7d32"
        self.hover_color = "#1b5e20"
        self.bg_color = "#0d1f0d"
        self.text_color = "#d4e6d4"
        self.danger_color = "#c62828"
        
        self.root.configure(fg_color=self.bg_color)
        
        # Главный фрейм
        self.main_frame = ctk.CTkScrollableFrame(
            self.root, 
            fg_color=self.bg_color,
            border_width=0
        )
        self.main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Заголовок
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="🎮 DirectX Installer & Optimized Tweaks",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.primary_color
        )
        self.title_label.pack(pady=(0, 20))
        
        # === Секция 1: Установка DirectX ===
        self.create_section_header("📦 УСТАНОВКА DIRECTX")
        
        self.create_install_button(
            name="Standard DirectX",
            cmd="StandardDirectX.exe /q",
            description="Стандартный установщик DirectX — используют 90% пользователей.\nОфициальная версия от Microsoft с полной поддержкой всех компонентов."
        )
        
        self.create_install_button(
            name="DirectX For ProOS",
            cmd="cd DirectXForProOS && DXSETUP.exe /silent",
            description="Альтернативная версия DirectX, если стандартный установщик не работает.\nОптимизирована для профессиональных сборок Windows."
        )
        
        self.create_install_button(
            name="DirectX Game Edition",
            cmd="DirectXGameEdition.exe /q",
            description="Версия DirectX, обычно находящаяся в папке Redist в игровых установщиках.\nСодержит дополнительные игровые компоненты и библиотеки."
        )
        
        self.create_install_button(
            name="DirectX MartyFiles Edition",
            cmd="DirectXMartyFilesEdition.exe",
            description="Специальная редакция от WinClick — не отображается в списке установленных приложений.\nПолезна для совместимости со старыми играми."
        )
        
        # === Секция 2: Основные твики ===
        self.create_section_header("⚙️ ОСНОВНЫЕ ТВИКИ")
        
        btn_frame1 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame1.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame1, "🎮 Game+Performance Mode", self.tweak_game_performance)
        self.create_tweak_button(btn_frame1, "💾 Кэш шейдеров DX-Vulkan", self.tweak_shader_cache)
        self.create_tweak_button(btn_frame1, "⚡ Отключить VSync", self.tweak_disable_vsync)
        
        btn_frame2 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame2.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame2, "🔧 Few Vertices оптимизация", self.tweak_few_vertices)
        self.create_tweak_button(btn_frame2, "🖨️ Включить PrintScreen", self.tweak_enable_printscreen)
        self.create_tweak_button(btn_frame2, "🚀 Улучшить DX-Vulkan", self.tweak_improve_dx_vulkan)
        
        btn_frame3 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame3.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame3, "⏱️ Уменьшить задержки", self.tweak_reduce_latency)
        self.create_tweak_button(btn_frame3, "🔄 Отключить NoSysLock", self.tweak_disable_nosyslock)
        self.create_tweak_button(btn_frame3, "📺 Отключить ModeX", self.tweak_disable_modex)

        # Новая секция для D3D11/D3D12 оптимизаций
        self.create_section_header("🎮 D3D11/D3D12 ОПТИМИЗАЦИИ")

        btn_frame_d3d = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame_d3d.pack(fill="x", pady=5)

        self.create_tweak_button(btn_frame_d3d, "🖥️ Graphics Settings", self.tweak_graphics_settings)
        self.create_tweak_button(btn_frame_d3d, "⚠️ Unsafe Command Buffer", self.tweak_d3d12_unsafe_buffer)
        self.create_tweak_button(btn_frame_d3d, "⚡ Runtime Optimizations", self.tweak_d3d12_runtime_optimizations)

        btn_frame_d3d2 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame_d3d2.pack(fill="x", pady=5)

        self.create_tweak_button(btn_frame_d3d2, "📐 Resource Alignment", self.tweak_d3d12_resource_alignment)
        self.create_tweak_button(btn_frame_d3d2, "🧵 D3D11 Multithreaded", self.tweak_d3d11_multithreaded)
        self.create_tweak_button(btn_frame_d3d2, "🧵 D3D12 Multithreaded", self.tweak_d3d12_multithreaded)

        btn_frame_d3d3 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame_d3d3.pack(fill="x", pady=5)

        self.create_tweak_button(btn_frame_d3d3, "📋 D3D11 Deferred Contexts", self.tweak_d3d11_deferred_contexts)
        self.create_tweak_button(btn_frame_d3d3, "📋 D3D12 Deferred Contexts", self.tweak_d3d12_deferred_contexts)
        self.create_tweak_button(btn_frame_d3d3, "🧩 D3D11 Allow Tiling", self.tweak_d3d11_allow_tiling)

        btn_frame_d3d4 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame_d3d4.pack(fill="x", pady=5)

        self.create_tweak_button(btn_frame_d3d4, "⚙️ D3D11 Dynamic Codegen", self.tweak_d3d11_dynamic_codegen)
        self.create_tweak_button(btn_frame_d3d4, "🧩 D3D12 Allow Tiling", self.tweak_d3d12_allow_tiling)
        self.create_tweak_button(btn_frame_d3d4, "📄 CPU Page Table", self.tweak_d3d12_cpu_page_table)

        btn_frame_d3d5 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame_d3d5.pack(fill="x", pady=5)

        self.create_tweak_button(btn_frame_d3d5, "💾 Heap Serialization", self.tweak_d3d12_heap_serialization)
        self.create_tweak_button(btn_frame_d3d5, "🗺️ Map Heap Allocations", self.tweak_d3d12_map_heap_allocations)
        self.create_tweak_button(btn_frame_d3d5, "🏠 Residency Management", self.tweak_d3d12_residency_management)
        
        # === Секция 3: MMX оптимизации ===
        self.create_section_header("🧠 MMX ОПТИМИЗАЦИИ")
        
        btn_frame4 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame4.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame4, "🔧 Включить MMX инструкции", self.tweak_enable_mmx)
        self.create_tweak_button(btn_frame4, "⚡ MMX Fast Path", self.tweak_mmx_fastpath)
        self.create_tweak_button(btn_frame4, "🎨 MMX для RGB", self.tweak_mmx_for_rgb)
        
        btn_frame5 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame5.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame5, "🔄 EnumSeparateMMX", self.tweak_enum_separate_mmx)
        
        # === Секция 4: AGP и память ===
        self.create_section_header("🖥️ AGP И ВИДЕОПАМЯТЬ")
        
        btn_frame6 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame6.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame6, "🎮 AGP Texturing", self.tweak_agp_texturing)
        self.create_tweak_button(btn_frame6, "💾 Нелокальная видеопамять", self.tweak_nonlocal_vidmem)
        self.create_tweak_button(btn_frame6, "📀 Увеличить VRAM буфер", self.tweak_vga_buffer)
        
        # === Секция 5: Драйверы программной прорисовки ===
        self.create_section_header("🎨 ДРАЙВЕРЫ ПРОГРАММНОЙ ПРОРИСОВКИ")
        
        btn_frame7 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame7.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame7, "🔍 Reference Driver", self.tweak_enum_reference)
        self.create_tweak_button(btn_frame7, "🎯 RAMP Driver", self.tweak_enum_ramp)
        self.create_tweak_button(btn_frame7, "🕳️ NULL Device", self.tweak_enum_null)
        
        # === Секция 6: Аппаратное ускорение ===
        self.create_section_header("⚡ АППАРАТНОЕ УСКОРЕНИЕ")
        
        btn_frame8 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame8.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame8, "🎯 Hardware Point Sprites", self.tweak_point_sprites)
        self.create_tweak_button(btn_frame8, "🎚️ Hardware State Blocks", self.tweak_state_blocks)
        self.create_tweak_button(btn_frame8, "🎨 Hardware Rasterizer", self.tweak_hardware_rasterizer)
        
        btn_frame9 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame9.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame9, "🖼️ DDSCAPS Acceleration", self.tweak_ddscaps)
        self.create_tweak_button(btn_frame9, "🎮 DirectDraw Hardware", self.tweak_directdraw_hardware)
        self.create_tweak_button(btn_frame9, "🎵 MIDI Hardware", self.tweak_midi_hardware)
        
        # === Секция 7: Отключение отладки ===
        self.create_section_header("🐛 ОТКЛЮЧЕНИЕ ОТЛАДКИ")
        
        btn_frame10 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame10.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame10, "🔇 Disable Debugging", self.tweak_disable_debugging)
        self.create_tweak_button(btn_frame10, "🔇 Disable FullDebug", self.tweak_disable_full_debug)
        self.create_tweak_button(btn_frame10, "🔇 Disable Debug Monitor", self.tweak_disable_dm)
        
        btn_frame11 = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        btn_frame11.pack(fill="x", pady=5)
        
        self.create_tweak_button(btn_frame11, "🔇 Disable Multimon Debug", self.tweak_disable_multimon_debug)
        self.create_tweak_button(btn_frame11, "🔇 Disable Debug Runtime", self.tweak_disable_debug_runtime)
        
        # === Секция 8: Управление твиками ===
        self.create_section_header("🔄 УПРАВЛЕНИЕ ТВИКАМИ")
        
        self.apply_all_btn = ctk.CTkButton(
            self.main_frame,
            text="✅ ПРИМЕНИТЬ ВСЕ ТВИКИ",
            command=self.apply_all_tweaks,
            height=50,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.primary_color,
            hover_color=self.hover_color
        )
        self.apply_all_btn.pack(fill="x", pady=(10, 10))
        
        self.reset_all_btn = ctk.CTkButton(
            self.main_frame,
            text="🔄 DIRECTX DEFAULT — ВЕРНУТЬ ВСЁ КАК БЫЛО",
            command=self.reset_all_tweaks,
            height=50,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.danger_color,
            hover_color="#8e0000"
        )
        self.reset_all_btn.pack(fill="x", pady=(10, 20))
        
        # Информация
        self.info_frame = ctk.CTkFrame(self.main_frame, fg_color="#1a2a1a", corner_radius=10)
        self.info_frame.pack(fill="x", pady=(10, 0))
        
        self.info_label = ctk.CTkLabel(
            self.info_frame,
            text="💡 ИНФОРМАЦИЯ:\n"
                 "• Запустите скрипт от имени Администратора\n"
                 "• После применения твиков перезагрузите компьютер",
            font=ctk.CTkFont(size=12),
            text_color=self.text_color,
            justify="left"
        )
        self.info_label.pack(padx=10, pady=10)
        
        # Статус
        self.status_var = ctk.StringVar(value="Готов к работе")
        self.status_bar = ctk.CTkLabel(
            self.root,
            textvariable=self.status_var,
            font=ctk.CTkFont(size=11),
            fg_color=self.primary_color,
            text_color="white",
            corner_radius=0,
            height=28
        )
        self.status_bar.pack(side="bottom", fill="x")
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_section_header(self, text):
        header = ctk.CTkLabel(
            self.main_frame,
            text=text,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.primary_color
        )
        header.pack(anchor="w", pady=(15, 5))
    
    def create_tweak_button(self, parent, text, command):
        btn = ctk.CTkButton(
            parent,
            text=text,
            command=command,
            height=35,
            font=ctk.CTkFont(size=12),
            fg_color=self.primary_color,
            hover_color=self.hover_color
        )
        btn.pack(side="left", padx=5, pady=5, expand=True, fill="x")
    
    def create_install_button(self, name, cmd, description):
        frame = ctk.CTkFrame(self.main_frame, fg_color="#1a2a1a", corner_radius=10)
        frame.pack(fill="x", pady=5)
        
        btn = ctk.CTkButton(
            frame,
            text=f"📀 Установить {name}",
            command=lambda: self.install_directx(cmd, name),
            height=40,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=self.primary_color,
            hover_color=self.hover_color
        )
        btn.pack(side="left", padx=(10, 15), pady=10)
        
        text_frame = ctk.CTkFrame(frame, fg_color="transparent")
        text_frame.pack(side="left", fill="both", expand=True, pady=8)
        
        desc_label = ctk.CTkLabel(
            text_frame,
            text=description,
            font=ctk.CTkFont(size=11),
            text_color=self.text_color,
            wraplength=500,
            justify="left"
        )
        desc_label.pack(anchor="w")
    
    def run_reg(self, command, description):
        try:
            subprocess.run(command, shell=True, capture_output=True)
            self.status_var.set(f"✅ {description}")
            return True
        except:
            self.status_var.set(f"❌ {description}")
            return False
    
    def install_directx(self, command, name):
        self.status_var.set(f"⏳ Установка {name}...")
        self.root.update()
        try:
            full_command = f'cmd /c "{command}"'
            process = subprocess.Popen(full_command, shell=True, cwd=os.path.dirname(os.path.abspath(__file__)))
            process.wait(timeout=300)
            self.status_var.set(f"✅ {name} установлен")
            messagebox.showinfo("Успех", f"{name} успешно установлен!")
        except Exception as e:
            self.status_var.set(f"❌ Ошибка {name}")
            messagebox.showerror("Ошибка", str(e))
    
    # === ВСЕ ТВИКИ ===
    
    def tweak_game_performance(self):
        self.run_reg('reg add "HKCU\\Software\\DirectX" /v "PerformanceMode" /t REG_DWORD /d 1 /f', "Game Mode")
        self.run_reg('reg add "HKCU\\Software\\DirectX" /v "GameMode" /t REG_DWORD /d 1 /f', "Performance Mode")
    
    def tweak_shader_cache(self):
        self.run_reg('Reg.exe add "HKLM\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "EnableShaderCache" /t REG_DWORD /d "1" /f', "Shader Cache")
    
    def tweak_disable_vsync(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "FlipNoVsync" /t REG_DWORD /d "1" /f', "VSync OFF")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /v "FlipNoVsync" /t REG_DWORD /d "1" /f', "VSync OFF 32bit")
    
    def tweak_few_vertices(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "FewVertices" /t REG_DWORD /d "1" /f', "Few Vertices")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /v "FewVertices" /t REG_DWORD /d "1" /f', "Few Vertices 32bit")
    
    def tweak_enable_printscreen(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "EnablePrintScreen" /t REG_DWORD /d "1" /f', "PrintScreen")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "EnablePrintScreen" /t REG_DWORD /d "1" /f', "PrintScreen 32bit")
    
    def tweak_improve_dx_vulkan(self):
        self.run_reg('Reg.exe add "HKLM\\SYSTEM\\ControlSet001\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "EnableVirtualTopologySupport" /t REG_DWORD /d "1" /f', "DX-Vulkan Improve")
    
    def tweak_reduce_latency(self):
        self.run_reg('Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "PreferSystemMemoryContiguous" /t REG_DWORD /d "0" /f', "Latency 0000")
        self.run_reg('Reg.exe add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0001" /v "PreferSystemMemoryContiguous" /t REG_DWORD /d "0" /f', "Latency 0001")
    
    def tweak_disable_nosyslock(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "ForceNoSysLock" /t REG_DWORD /d "0" /f', "NoSysLock OFF")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "ForceNoSysLock" /t REG_DWORD /d "0" /f', "NoSysLock OFF 32bit")
    
    def tweak_disable_modex(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "ModeXOnly" /t REG_DWORD /d "0" /f', "ModeX OFF")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "ModeXOnly" /t REG_DWORD /d "0" /f', "ModeX OFF 32bit")
    
    def tweak_enable_mmx(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "DisableMMX" /t REG_DWORD /d "0" /f', "MMX DD")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "DisableMMX" /t REG_DWORD /d "0" /f', "MMX DD 32bit")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "DisableMMX" /t REG_DWORD /d "0" /f', "MMX D3D")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /v "DisableMMX" /t REG_DWORD /d "0" /f', "MMX D3D 32bit")
    
    def tweak_mmx_fastpath(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "MMX Fast Path" /t REG_DWORD /d "1" /f', "MMX Fast Path")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /v "MMX Fast Path" /t REG_DWORD /d "1" /f', "MMX Fast Path 32bit")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "MMXFastPath" /t REG_DWORD /d "1" /f', "MMXFastPath")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /v "MMXFastPath" /t REG_DWORD /d "1" /f', "MMXFastPath 32bit")
    
    def tweak_mmx_for_rgb(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "UseMMXForRGB" /t REG_DWORD /d "1" /f', "MMX for RGB")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /v "UseMMXForRGB" /t REG_DWORD /d "1" /f', "MMX for RGB 32bit")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "UseMMXForRGB" /t REG_DWORD /d "1" /f', "MMX for RGB Drivers")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers" /v "UseMMXForRGB" /t REG_DWORD /d "1" /f', "MMX for RGB Drivers 32bit")
    
    def tweak_enum_separate_mmx(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "EnumSeparateMMX" /t REG_DWORD /d "1" /f', "EnumSeparateMMX")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers" /v "EnumSeparateMMX" /t REG_DWORD /d "1" /f', "EnumSeparateMMX 32bit")
    
    def tweak_agp_texturing(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "DisableAGPSupport" /t REG_DWORD /d "0" /f', "AGP Texturing")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "DisableAGPSupport" /t REG_DWORD /d "0" /f', "AGP Texturing 32bit")
    
    def tweak_nonlocal_vidmem(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "UseNonLocalVidMem" /t REG_DWORD /d "1" /f', "NonLocal DD")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "UseNonLocalVidMem" /t REG_DWORD /d "1" /f', "NonLocal DD 32bit")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "UseNonLocalVidMem" /t REG_DWORD /d "1" /f', "NonLocal D3D")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /v "UseNonLocalVidMem" /t REG_DWORD /d "1" /f', "NonLocal D3D 32bit")
    
    def tweak_vga_buffer(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "VGABuffer" /t REG_DWORD /d "21181233" /f', "VGABuffer DD")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "VGABuffer" /t REG_DWORD /d "21181233" /f', "VGABuffer DD 32bit")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "VGABuffer" /t REG_DWORD /d "21181233" /f', "VGABuffer D3D")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /v "VGABuffer" /t REG_DWORD /d "21181233" /f', "VGABuffer D3D 32bit")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectMusic" /v "VGABuffer" /t REG_DWORD /d "21181233" /f', "VGABuffer Music")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectMusic" /v "VGABuffer" /t REG_DWORD /d "21181233" /f', "VGABuffer Music 32bit")
    
    def tweak_enum_reference(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "EnumReference" /t REG_DWORD /d "1" /f', "Reference Driver")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers" /v "EnumReference" /t REG_DWORD /d "1" /f', "Reference Driver 32bit")
    
    def tweak_enum_ramp(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "EnumRamp" /t REG_DWORD /d "1" /f', "RAMP Driver")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers" /v "EnumRamp" /t REG_DWORD /d "1" /f', "RAMP Driver 32bit")
    
    def tweak_enum_null(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "EnumNullDevice" /t REG_DWORD /d "1" /f', "NULL Device")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers" /v "EnumNullDevice" /t REG_DWORD /d "1" /f', "NULL Device 32bit")
    
    def tweak_point_sprites(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "EmulatePointSprites" /t REG_DWORD /d "0" /f', "Point Sprites HW")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "EmulatePointSprites" /t REG_DWORD /d "0" /f', "Point Sprites HW 32bit")
    
    def tweak_state_blocks(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "EmulateStateBlocks" /t REG_DWORD /d "0" /f', "State Blocks HW")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "EmulateStateBlocks" /t REG_DWORD /d "0" /f', "State Blocks HW 32bit")
    
    def tweak_hardware_rasterizer(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "ForceRgbRasterizer" /t REG_DWORD /d "0" /f', "Hardware Rasterizer")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers" /v "ForceRgbRasterizer" /t REG_DWORD /d "0" /f', "Hardware Rasterizer 32bit")
    
    def tweak_ddscaps(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "DisableDDSCAPSInDDSD" /t REG_DWORD /d "0" /f', "DDSCAPS HW")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "DisableDDSCAPSInDDSD" /t REG_DWORD /d "0" /f', "DDSCAPS HW 32bit")
    
    def tweak_directdraw_hardware(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "EmulationOnly" /t REG_DWORD /d "0" /f', "DirectDraw HW")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /v "EmulationOnly" /t REG_DWORD /d "0" /f', "DirectDraw HW 32bit")
    
    def tweak_midi_hardware(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\DirectMusic" /v "DisableHWAcceleration" /t REG_DWORD /d "0" /f', "MIDI HW")
        self.run_reg('reg add "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectMusic" /v "DisableHWAcceleration" /t REG_DWORD /d "0" /f', "MIDI HW 32bit")
    
    def tweak_disable_debugging(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "EnableDebugging" /t REG_DWORD /d "0" /f', "Debugging OFF")
    
    def tweak_disable_full_debug(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "FullDebug" /t REG_DWORD /d "0" /f', "FullDebug OFF")
    
    def tweak_disable_dm(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "DisableDM" /t REG_DWORD /d "1" /f', "Debug Monitor OFF")
    
    def tweak_disable_multimon_debug(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "EnableMultimonDebugging" /t REG_DWORD /d "0" /f', "Multimon Debug OFF")
    
    def tweak_disable_debug_runtime(self):
        self.run_reg('reg add "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "LoadDebugRuntime" /t REG_DWORD /d "0" /f', "Debug Runtime OFF")

    def tweak_graphics_settings(self):
        self.run_reg('Reg.exe add "HKCU\\Software\\Microsoft\\DirectX\\GraphicsSettings" /v "SwapEffectUpgradeCache" /t REG_DWORD /d "1" /f', "SwapEffectUpgradeCache")
        self.run_reg('Reg.exe add "HKCU\\Software\\Microsoft\\DirectX\\GraphicsSettings" /v "SpecificGPUOptionApplicable" /t REG_DWORD /d "1" /f', "SpecificGPUOptionApplicable")

    def tweak_d3d12_unsafe_buffer(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_ENABLE_UNSAFE_COMMAND_BUFFER_REUSE" /t REG_DWORD /d "1" /f', "D3D12 Unsafe Command Buffer")

    def tweak_d3d12_runtime_optimizations(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_ENABLE_RUNTIME_DRIVER_OPTIMIZATIONS" /t REG_DWORD /d "1" /f', "D3D12 Runtime Optimizations")

    def tweak_d3d12_resource_alignment(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_RESOURCE_ALIGNMENT" /t REG_DWORD /d "1" /f', "D3D12 Resource Alignment")

    def tweak_d3d11_multithreaded(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D11_MULTITHREADED" /t REG_DWORD /d "1" /f', "D3D11 Multithreaded")

    def tweak_d3d12_multithreaded(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_MULTITHREADED" /t REG_DWORD /d "1" /f', "D3D12 Multithreaded")

    def tweak_d3d11_deferred_contexts(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D11_DEFERRED_CONTEXTS" /t REG_DWORD /d "1" /f', "D3D11 Deferred Contexts")

    def tweak_d3d12_deferred_contexts(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_DEFERRED_CONTEXTS" /t REG_DWORD /d "1" /f', "D3D12 Deferred Contexts")

    def tweak_d3d11_allow_tiling(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D11_ALLOW_TILING" /t REG_DWORD /d "1" /f', "D3D11 Allow Tiling")

    def tweak_d3d11_dynamic_codegen(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D11_ENABLE_DYNAMIC_CODEGEN" /t REG_DWORD /d "1" /f', "D3D11 Dynamic Codegen")

    def tweak_d3d12_allow_tiling(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_ALLOW_TILING" /t REG_DWORD /d "1" /f', "D3D12 Allow Tiling")

    def tweak_d3d12_cpu_page_table(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_CPU_PAGE_TABLE_ENABLED" /t REG_DWORD /d "1" /f', "D3D12 CPU Page Table")

    def tweak_d3d12_heap_serialization(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_HEAP_SERIALIZATION_ENABLED" /t REG_DWORD /d "1" /f', "D3D12 Heap Serialization")

    def tweak_d3d12_map_heap_allocations(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_MAP_HEAP_ALLOCATIONS" /t REG_DWORD /d "1" /f', "D3D12 Map Heap Allocations")

    def tweak_d3d12_residency_management(self):
        self.run_reg('Reg.exe add "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_RESIDENCY_MANAGEMENT_ENABLED" /t REG_DWORD /d "1" /f', "D3D12 Residency Management")
    
    # === ПРИМЕНЕНИЕ ВСЕХ ТВИКОВ ===
    
    def apply_all_tweaks(self):
        if not self.is_admin():
            messagebox.showwarning("Внимание", "Запустите от имени Администратора!")
            return
        
        self.status_var.set("⏳ Применение всех твиков...")
        self.root.update()
        
        tweaks = [
            self.tweak_game_performance, self.tweak_shader_cache, self.tweak_disable_vsync,
            self.tweak_few_vertices, self.tweak_enable_printscreen, self.tweak_improve_dx_vulkan,
            self.tweak_reduce_latency, self.tweak_disable_nosyslock, self.tweak_disable_modex,
            self.tweak_enable_mmx, self.tweak_mmx_fastpath, self.tweak_mmx_for_rgb,
            self.tweak_enum_separate_mmx, self.tweak_agp_texturing, self.tweak_nonlocal_vidmem,
            self.tweak_vga_buffer, self.tweak_enum_reference, self.tweak_enum_ramp,
            self.tweak_enum_null, self.tweak_point_sprites, self.tweak_state_blocks,
            self.tweak_hardware_rasterizer, self.tweak_ddscaps, self.tweak_directdraw_hardware,
            self.tweak_midi_hardware, self.tweak_disable_debugging, self.tweak_disable_full_debug,
            self.tweak_disable_dm, self.tweak_disable_multimon_debug, self.tweak_disable_debug_runtime,
            self.tweak_graphics_settings,
            self.tweak_d3d12_unsafe_buffer,
            self.tweak_d3d12_runtime_optimizations,
            self.tweak_d3d12_resource_alignment,
            self.tweak_d3d11_multithreaded,
            self.tweak_d3d12_multithreaded,
            self.tweak_d3d11_deferred_contexts,
            self.tweak_d3d12_deferred_contexts,
            self.tweak_d3d11_allow_tiling,
            self.tweak_d3d11_dynamic_codegen,
            self.tweak_d3d12_allow_tiling,
            self.tweak_d3d12_cpu_page_table,
            self.tweak_d3d12_heap_serialization,
            self.tweak_d3d12_map_heap_allocations,
            self.tweak_d3d12_residency_management,
        ]
        
        for tweak in tweaks:
            tweak()
            self.root.update()
        
        self.status_var.set("✅ Все твики применены!")
        messagebox.showinfo("Готово", "Все твики успешно применены!\nПерезагрузите компьютер.")
    
    # === СБРОС ВСЕХ ТВИКОВ (DIRECTX DEFAULT) ===
    
    def reset_all_tweaks(self):
        if not self.is_admin():
            messagebox.showwarning("Внимание", "Запустите от имени Администратора!")
            return
        
        if not messagebox.askyesno("Подтверждение", "Удалить ВСЕ твики DirectX? Настройки вернутся к стандартным."):
            return
        
        self.status_var.set("⏳ Сброс настроек...")
        self.root.update()
        
        delete_commands = [
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "DisableDM" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "DisableMMX" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "EnableDebugging" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "EnableMultimonDebugging" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "FewVertices" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "FlipNoVsync" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "FullDebug" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "LoadDebugRuntime" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "MMX Fast Path" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "MMXFastPath" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "UseMMXForRGB" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "UseNonLocalVidMem" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D" /v "VGABuffer" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "EnumNullDevice" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "EnumRamp" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "EnumReference" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "EnumSeparateMMX" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "ForceRgbRasterizer" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Direct3D\\Drivers" /v "UseMMXForRGB" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "DisableAGPSupport" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "DisableDDSCAPSInDDSD" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "DisableMMX" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "EmulatePointSprites" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "EmulateStateBlocks" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "EmulationOnly" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "EnablePrintScreen" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "ForceNoSysLock" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "ModeXOnly" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "UseNonLocalVidMem" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectDraw" /v "VGABuffer" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectMusic" /v "DisableHWAcceleration" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectMusic" /v "VGABuffer" /f 2>nul',
            'reg delete "HKCU\\Software\\Microsoft\\DirectX\\GraphicsSettings" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_ENABLE_UNSAFE_COMMAND_BUFFER_REUSE" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_ENABLE_RUNTIME_DRIVER_OPTIMIZATIONS" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_RESOURCE_ALIGNMENT" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D11_MULTITHREADED" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_MULTITHREADED" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D11_DEFERRED_CONTEXTS" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_DEFERRED_CONTEXTS" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D11_ALLOW_TILING" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D11_ENABLE_DYNAMIC_CODEGEN" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_ALLOW_TILING" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_CPU_PAGE_TABLE_ENABLED" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_HEAP_SERIALIZATION_ENABLED" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_MAP_HEAP_ALLOCATIONS" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\DirectX" /v "D3D12_RESIDENCY_MANAGEMENT_ENABLED" /f 2>nul',
            'reg delete "HKCU\\Software\\DirectX" /f 2>nul',
        ]
        
        for cmd in delete_commands:
            subprocess.run(cmd, shell=True, capture_output=True)
            self.root.update()
        
        # Wow6432Node
        wow_commands = [
            'reg delete "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Direct3D\\Drivers" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectDraw" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\DirectMusic" /f 2>nul',
        ]
        
        for cmd in wow_commands:
            subprocess.run(cmd, shell=True, capture_output=True)
            self.root.update()
        
        self.status_var.set("✅ DirectX Default — все сброшено!")
        messagebox.showinfo("Готово", "Все твики удалены!\nНастройки возвращены к стандартным.\nПерезагрузите компьютер.")
    
    def is_admin(self):
        try:
            return os.getuid() == 0
        except:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    def on_closing(self):
        self.root.destroy()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DirectXInstallerApp()
    app.run()