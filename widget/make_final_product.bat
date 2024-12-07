:: Install the library pyinstaller  
pip install pyinstaller   

:: Verify the installer 
pyinstaller --version

:: Create the Executable
pyinstaller --onefile C:\BHCC\python\CSC-287-01\widget\widgetButtons.py

:: Create a windowed application without the command prompt window appearing
pyinstaller --onefile --windowed C:\BHCC\python\CSC-287-01\widget\widgetButtons.py

:: Verify if the executable was created and announce success
if exist C:\BHCC\python\CSC-287-01\widget\dist\widgetButtons.exe (
    echo Executable created successfully Anatolie Jentimir Maladetz !!
) else (
    echo Failed to create the executable.
)

:: Pause to keep the window open
pause



 