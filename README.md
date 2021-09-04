# Shutdown PC
Программа для выключения компьютера по таймеру или по дате. 
* По таймеру: устанавливаете через сколько ПК выключится в минутах. (максимум 1440)
* По дате: устанавливаете когда ПК выключится (число, месяц, год, часы, минуты).
  

  Если поставить галочку "добавить в планировщик", то программу можно закрывать. 
  Для Windows - создается задача на выключение в планировщике windows.

___

## Установка
Инструкция о том, как получить копию этой программы и запустить её на компьютере. 

**Windows**

- Скачать `shutdown_pc.exe` файл и запустить его. \[[Download](https://github.com/rybkinn/ShutdownPC/raw/master/shutdown_pc.exe "shutdown_pc.exe")\]
###### или  
- `git clone https://github.com/rybkinn/ShutdownPC.git`
  - (можно скачать архив \[[Download](https://github.com/rybkinn/ShutdownPC/archive/master.zip "ShutdownPC-master.zip")\])

- Запустить файл `shutdown_pc.exe`

**Linux**

- `git clone https://github.com/rybkinn/ShutdownPC.git`
  - (или нажать на "Code" => Download ZIP и распаковать архив)

- Установить зависимости командой `pip install -r requirements.txt`
- Запустить файл `shutdown_pc.py` (сделать исполняемым `chmod u+x shutdown_pc.py`)
___

## Программа создана с помощью

- Python 3
- PyQt5
- Qt5 Designer