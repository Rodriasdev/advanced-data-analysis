# Analizador de Desempeño de Empleados

`EmployeePerformanceAnalyzer` es un script en Python que se conecta a una base de datos MySQL para obtener datos de desempeño de empleados, calcular estadísticas básicas y correlaciones, y visualizar los datos utilizando histogramas y gráficos de dispersión. Este proyecto utiliza `pandas` para la manipulación de datos, `matplotlib` para la visualización, y `MySQLdb` para la interacción con la base de datos.

## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tuusuario/employee-performance-analyzer.git
    cd employee-performance-analyzer
    ```

2. **Instalar los paquetes de Python requeridos**:
    Puedes instalar los paquetes necesarios utilizando pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configurar la base de datos MySQL**:
    Asegúrate de tener configurada y en funcionamiento una base de datos MySQL. Necesitas tener una tabla llamada `employeeperformance` con las siguientes columnas:

    - `id`: Identificador único para cada registro
    - `employee_id`: Identificador único para cada empleado
    - `departament`: Departamento donde trabaja el empleado
    - `performance_score`: Puntaje de desempeño del empleado
    - `years_with_company`: Número de años que el empleado ha estado en la empresa
    - `salary`: Salario del empleado

4. **Configuración de la base de datos**:
    Modifica la función `connectdb()` en el módulo `db.py` para incluir los detalles de conexión a tu base de datos MySQL (host, usuario, contraseña, nombre de la base de datos).

## Uso

Ejecuta el script utilizando el siguiente comando:

```bash
python employee_performance_analyzer.py
