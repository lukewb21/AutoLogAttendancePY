@ECHO OFF

if "%1" == "-nowin" (
  python program/main.py
) else (
  start pwsh -NoExit -Command "python program/main.py"
)
