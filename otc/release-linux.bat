@echo off
call gradlew.bat jar

del temp\*.* /S /Q
mkdir temp
mkdir temp\otc
mkdir temp\otc\bin
mkdir temp\otc\lib
mkdir temp\otc\examples
copy  doc\*.* temp\otc
copy  bin\*.* temp\otc\bin
copy  lib\*.* temp\otc\lib
copy  build\libs\otc-0.0.1-SNAPSHOT.jar temp\otc\lib
copy  examples\*.* temp\otc\examples
cd temp
"c:\program files\winrar\WinRAR.exe" a -afzip ..\release\setup_%Date:~0,10%.zip *.* -r


