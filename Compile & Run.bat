
python -m py_compile "Password Generator.py"

cd __pycache__
del "Password Generator.pyw"
ren "Password Generator*.pyc" "Password Generator.pyw"

cd..
del "Password Generator.pyw"
MOVE .\__pycache__\"Password Generator.pyw" .\

@echo off
echo.
echo.
echo  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
echo    *                                                     *
echo    *  Compile successful, you can close this window now  *
echo    *                                                     *
echo  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
echo.

"Password Generator.pyw"

pause