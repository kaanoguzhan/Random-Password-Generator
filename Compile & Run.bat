
python -m py_compile "Password Generator.py"

del "Password Generator.pyw"
ren "Password Generator.pyc" "Password Generator.pyw"

@echo off
echo.
echo  ******************************************************
echo  * Compile successful, you can close this window now. *
echo  ******************************************************

"Password Generator.pyw"
