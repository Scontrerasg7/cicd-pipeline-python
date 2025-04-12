## 1. ¿Qué ventajas le proporciona a un proyecto el uso de un pipeline de CI? Menciona al menos tres ventajas específicas y explica por qué son importantes.

    * Garantizar que el código que se integra a un repositorio funciona: esto asegura que no se están agregando bugs y que no se están "rompiendo" features.
    * Darle un formato estándar: crea un repositorio organizado y minimiza los cambios sugeridos en los commits.
    * Generar un report de coverage: le da una idea al equipo de qué tanto código está testeado en el repositorio, con miras a mejorarlo.

## 2. ¿Cuál es la diferencia principal entre una prueba unitaria y una prueba de aceptación? Da un ejemplo de algo que probarías con una prueba unitaria y algo que probarías con una prueba de aceptación (en el contexto de cualquier aplicación que conozcas (describela primero)).

    Una prueba unitaria, como su nombre lo menciona, testea unidades funcionales de código, fragmentos que tienen un comportamiento directo y sencillo (funciones, clases, métodos). Una prueba de aceptación simula el comportamiento de un usuario dentro de la interfaz gráfica y evalúa el resultado.
    * Usaríamos una prueba unitaria para mockear una base de datos y evaluar una petición. Una para el caso exitoso donde un registro exista y otra para un caso erróneo en el que el registro no exista.
    * Usaríamos una prueba de aceptación para simular que se elimina un registro de una tabla, se activa un loader spinner y finalmente aparece un modal de cierto color que confirma la eliminación.

### 3. Describe brevemente qué hace cada uno de los steps principales de tu workflow de GitHub Actions (desde el checkout hasta el push de Docker). Explica el propósito de cada uno (qué hace y para qué se hace).

- Clona el repo y setea python con sus dependencias.

```
   actions/checkout@v3
   actions/setup-python@v3
   python -m pip install --upgrade pip
   pip install -r requirements.txt
```

- Corre el black sin editar, corre pylint y flake8 y guarda el reporte en un archivo para que lo use sonar

```
    black app --check
    pylint app --output-format=text --fail-under=9 > pylint-report.txt || true
    flake8 app --output-file=flake8-report.txt || true
```

- Corre las pruebas unitarias (guarda la cobertura para sonar) y las de aceptación

```
pytest --ignore=tests/test_acceptance_app.py  # Genera un informe XML para SonarCloud
gunicorn --workers=2 --bind=0.0.0.0:8000 app.app:app &
          sleep 10
          pytest tests/test_acceptance_app.py --cov-report=xml:acceptance_coverage.xml --html=acceptance_report.html # Genera un informe XML con otro nombre, para no sobre-escribir el anterior de  las pruebas unitarias
```

- Luego corre la acción oficial de sonar para usar los archivos generados antes

- Finalmente setea docker, inicia sesión en dockerhub y hace push de la imagen

## 4. ¿Qué problemas o dificultades encontraste al implementar este taller? ¿Cómo los solucionaste? (Si no encontraste ningún problema, describe algo nuevo que hayas aprendido).

Al no tener instalado docker desktop, tuvimos que instalar colima para poder correr docker. Por otro lado, las pruebas tuvimos que arreglar según lo que veíamos en SonarCloud, se sumó un poco que ninguno del equipo usa python para su trabajo por lo que tuvimos que ayudarnos de la IA para solucionar los issues.
Aprendimos a implementar herramientas de formateo de código como black, y como los linters como pylint generan reportes que son usados por sonar. También fue interesante indagar en el codigo que se corre para las pruebas de aceptación y ver como itera en varios casos.

## 5. ¿Qué ventajas ofrece empaquetar la aplicación en una imagen Docker al final del pipeline en lugar de simplemente validar el código?

Con el artefacto generado de la imagen de docker, se puede desplegar en los diferentes ambientes (test, staging, producción), a diferencia de solo la validación que no genera el artefacto a desplegar. Por otra parte, la imagen de Docker incluye todo lo necesario para que la app funcione (código, dependencias, configuraciones).
