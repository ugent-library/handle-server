@echo off

SET PRG=%~dp0%

SET CP=.

REM Get the full name of the directory where the Handle code is installed
SET HDLHOME=%PRG%..

REM add all the jar files in the lib directory to the classpath
FOR %%i IN ("%HDLHOME%\lib\*.*") DO CALL "%HDLHOME%\bin\cpappend.bat" %%i

java -cp "%CP%" net.handle.apps.tools.KeyGenerator %*