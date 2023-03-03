@echo off
cd C:\Users\Public\Desktop\venv
call Scripts\activate


for /f "delims=" %%f in ('dir /b /a-d "C:\Users\donat\OneDrive\Desktop\convert_file_names\vhf-archive-export-2022-09-21-134051.708850 (1)\2022\09\1"') do (
    copy "C:\Users\donat\OneDrive\Desktop\convert_file_names\vhf-archive-export-2022-09-21-134051.708850 (1)\2022\09\1\%%f" "C:\Users\Public\Desktop\venv\%%f"
    echo whisper "C:\Users\Public\Desktop\venv%%f" --model small --task translate
    whisper "C:\Users\Public\Desktop\venv\%%f" --model small --task translate
    move "C:\Users\Public\Desktop\venv\%%f.txt" "C:\Users\donat\OneDrive\Desktop\copied_over"

    echo %%f.txt >> "C:\Users\donat\OneDrive\Desktop\copied_over\information.txt"
    type "C:\Users\donat\OneDrive\Desktop\copied_over\%%f.txt" >> "C:\Users\donat\OneDrive\Desktop\copied_over\information.txt"
    echo. >> "C:\Users\donat\OneDrive\Desktop\copied_over\information.txt"


    taskkill /F /IM python.exe
    start /B python "C:\Users\donat\OneDrive\Desktop\gui.py"
    

    del "C:\Users\Public\Desktop\venv\%%f"
    del "C:\Users\Public\Desktop\venv\%%f.srt"
    del "C:\Users\Public\Desktop\venv\%%f.txt"
    del "C:\Users\Public\Desktop\venv\%%f.vtt"
)

