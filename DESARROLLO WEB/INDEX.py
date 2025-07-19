<!DOCTYPE html>
<html>
    <head>
        <title>Gestor de estudiantes</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <!--<link rel="stylesheet" href="style.css"> -->
    </head>
    <body class="container mt-5" data-bs-theme="dark">
        <div class="d-flex justify-content-end mb-3">
            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="toggleTheme" checked>
                <label class="form-check-label small" for="toggleTheme" id="toggleLabel">Modo Oscuro</label>
            </div>
        </div>
        <h1 class="mb-4">Lista de Alumnos</h1>
        <form id="formulario" class="row g-3 mb-4">
            <div class="col-md-2">
                <input type="text" class="form-control" id="matricula" name="matricula" placeholder="Matricula">
            </div>
            <div class="col-md-2">
                <input type="text" class="form-control" id="nombre" name="name" placeholder="Nombre">
            </div>
            <div class="col-md-2">
                <input type="text" class="form-control" id="apellidos" name="apellidos" placeholder="Apellidos">
            </div>
            <div class="col-md-2">
                <select class="form-select" id="genero" name="genero">
                    <option value="Masculino">Masculino</option>
                    <option value="Femenino">Femenino</option>
                </select>
            </div>
            <div class="col-md-2">
                <input type="text" class="form-control" id="direccion" name="direccion" placeholder="Direccion">
            </div>
            <div class="col-md-2">
                <input type="text" class="form-control" id="telefono" name="telefono" placeholder="Telefono">
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-primary" id="btn_guardar">Guardar</button>
                <button type="button" class="btn btn-secondary" id="btn_cancelar">Cancelar</button>
            </div>
        </form>

        <table class="table table-striped table-hover">
            <thead>
                <tr>
                    <th>Matricula</th>
                    <th>Nombre</th>
                    <th>Apellidos</th>
                    <th>Genero</th>
                    <th>Direccion</th>
                    <th>Telefono</th>
                </tr>
            </thead>
            <tbody id="tabla_estudiantes">
                <!-- Aquí se agregan los estudiantes -->
            </tbody>
        </table>
        
    </body>
    
    <script src="app.js"></script>
    <script>
        const toggle = document.getElementById('toggleTheme');
        const label = document.getElementById('toggleLabel');
        const body = document.body;

        toggle.addEventListener('change', () => {
            if (toggle.checked) {
                body.setAttribute('data-bs-theme', 'dark');
                label.textContent = 'Modo Oscuro';
            } else {
                body.setAttribute('data-bs-theme', 'light');
                label.textContent = 'Modo Claro';
            }
        });
    </script>
</html>
