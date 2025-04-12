#!/usr/bin/env python3
"""
Скрипт для проверки системной информации в Termux
Сохраните как check_system.py и запустите: python check_system.py
"""

import os
import time
import platform
import subprocess
import datetime

def format_size(size_bytes):
    """Форматирует размер в байтах в удобочитаемый формат"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes/1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes/(1024*1024):.1f} MB"
    else:
        return f"{size_bytes/(1024*1024*1024):.1f} GB"

def format_uptime(seconds):
    """Форматирует время работы системы"""
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if days > 0:
        return f"{days}d {hours}h {minutes}m"
    elif hours > 0:
        return f"{hours}h {minutes}m"
    else:
        return f"{minutes}m {seconds}s"

print("======= ПРОВЕРКА СИСТЕМНОЙ ИНФОРМАЦИИ =======")
print(f"Дата и время: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
print(f"Python версия: {platform.python_version()}")
print(f"Система: {platform.system()} {platform.release()}")

# Проверка Termux
is_termux = 'com.termux' in os.environ.get('PREFIX', '')
print(f"Termux: {'Да' if is_termux else 'Нет'}")

# Тест доступности файлов /proc
proc_files = ['/proc/cpuinfo', '/proc/meminfo', '/proc/uptime']
print("\n--- Доступность системных файлов ---")
for file in proc_files:
    exists = os.path.exists(file)
    readable = False
    if exists:
        try:
            with open(file, 'r') as f:
                f.read(10)
                readable = True
        except:
            pass
    print(f"{file}: {'Существует и читается' if readable else 'Недоступен'}")

# Информация о CPU
print("\n--- Информация о CPU ---")
try:
    if os.path.exists('/proc/cpuinfo'):
        cpu_info = subprocess.check_output(['cat', '/proc/cpuinfo']).decode('utf-8')
        cores = set()
        threads = 0
        for line in cpu_info.split('\n'):
            if 'processor' in line:
                threads += 1
            if 'core id' in line:
                core_id = line.split(':')[1].strip()
                cores.add(core_id)
        print(f"Физические ядра: {len(cores) if cores else 'Н/Д'}")
        print(f"Логические ядра: {threads}")
    else:
        print("Информация о CPU недоступна через /proc/cpuinfo")
        
    # Альтернативный способ
    try:
        cpu_info_alt = subprocess.check_output(['nproc', '--all']).decode('utf-8').strip()
        print(f"Число процессоров (nproc): {cpu_info_alt}")
    except:
        print("Команда nproc недоступна")
except Exception as e:
    print(f"Ошибка при получении информации о CPU: {e}")

# Информация о памяти
print("\n--- Информация о памяти ---")
try:
    if os.path.exists('/proc/meminfo'):
        mem_info = subprocess.check_output(['cat', '/proc/meminfo']).decode('utf-8')
        total = 0
        available = 0
        for line in mem_info.split('\n'):
            if 'MemTotal' in line:
                total = int(line.split()[1]) * 1024
                print(f"Всего память: {format_size(total)}")
            if 'MemAvailable' in line:
                available = int(line.split()[1]) * 1024
                print(f"Доступно памяти: {format_size(available)}")
        
        if total > 0 and available > 0:
            usage_percent = (total - available) / total * 100
            print(f"Использование памяти: {usage_percent:.1f}%")
    else:
        print("Информация о памяти недоступна через /proc/meminfo")
        
    # Альтернативный способ через free
    try:
        free_output = subprocess.check_output(['free', '-b']).decode('utf-8').strip()
        print("\nВывод команды free:")
        print(free_output)
    except:
        print("Команда free недоступна")
except Exception as e:
    print(f"Ошибка при получении информации о памяти: {e}")

# Информация о диске
print("\n--- Информация о диске ---")
try:
    df_output = subprocess.check_output(['df', '-h']).decode('utf-8')
    print("Вывод команды df -h:")
    print(df_output)
except Exception as e:
    print(f"Ошибка при получении информации о диске: {e}")

# Uptime
print("\n--- Uptime системы ---")
try:
    # Метод 1: через /proc/uptime
    if os.path.exists('/proc/uptime'):
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_content = f.read()
                uptime_seconds = float(uptime_content.split()[0])
                print(f"Uptime (из /proc/uptime): {format_uptime(int(uptime_seconds))}")
        except Exception as e:
            print(f"Ошибка при чтении /proc/uptime: {e}")
    
    # Метод 2: через команду uptime
    try:
        uptime_output = subprocess.check_output(['uptime']).decode('utf-8').strip()
        print(f"Вывод команды uptime: {uptime_output}")
    except Exception as e:
        print(f"Ошибка при выполнении команды uptime: {e}")
    
    # Метод 3: через время создания /proc/self
    try:
        boot_time = os.stat('/proc/self').st_ctime
        current_time = time.time()
        uptime_seconds = current_time - boot_time
        print(f"Uptime (через /proc/self): {format_uptime(int(uptime_seconds))}")
    except Exception as e:
        print(f"Ошибка при использовании /proc/self: {e}")
    
except Exception as e:
    print(f"Общая ошибка при получении uptime: {e}")

# Сетевая информация
print("\n--- Сетевая информация ---")
try:
    # Метод 1: через ip addr
    try:
        ip_output = subprocess.check_output(['ip', 'addr']).decode('utf-8', errors='ignore')
        print("IP адреса (ip addr):")
        for line in ip_output.split('\n'):
            if 'inet ' in line and not '127.0.0.1' in line:
                print(line.strip())
    except Exception as e:
        print(f"Ошибка при выполнении ip addr: {e}")
    
    # Метод 2: через hostname -I
    try:
        hostname_output = subprocess.check_output(['hostname', '-I']).decode('utf-8').strip()
        print(f"IP адреса (hostname -I): {hostname_output}")
    except Exception as e:
        print(f"Ошибка при выполнении hostname -I: {e}")
except Exception as e:
    print(f"Общая ошибка при получении сетевой информации: {e}")

print("\n======= ПРОВЕРКА ЗАВЕРШЕНА =======")
