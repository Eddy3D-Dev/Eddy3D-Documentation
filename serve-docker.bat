REM Stop all running Docker containers
FOR /f "tokens=*" %%i IN ('docker ps -q') DO docker stop %%i
docker run --rm -it -p 8080:8000 -v %cd%:/docs eddy3d-mkdocs-material