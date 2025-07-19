const API_URL = "/estudiantes";
const btn_guardar = document.getElementById("btn_guardar");
const formulario = document.getElementById("formulario");
const tabla = document.getElementById("tabla_estudiantes");

//COMENTARIO
async function getEstudiantesPaginado(skip = 0, limit = 10){
    console.log("Iniciando Obtener Estudiantes");
    tabla.innerHTML = ""
    const response = await fetch(`${API_URL}?skip=${skip}&limit=${limit}`);
    console.log(response)
    if (response.ok){
        console.log("OK");
        const data = await response.json();
        console.log(data)
        const estudiantes = data.details
        estudiantes.forEach(estudiante => {
            const tr = document.createElement("tr")
            tr.innerHTML = `
                <td> ${estudiante.matricula || ""} </td>
                <td> ${estudiante.nombre || ""} </td>
                <td> ${estudiante.apellidos || ""} </td>
                <td> ${estudiante.genero || ""} </td>
                <td> ${estudiante.direccion || ""} </td>
                <td> ${estudiante.telefono || ""} </td>
            `;
            tabla.appendChild(tr);
        });

        let paginacion = document.getElementById("paginacion");
        if (!paginacion){
            paginacion = document.createElement("div");
            paginacion.id = "paginacion";
            tabla.parentElement.appendChild(paginacion)
        }
        paginacion.innerHTML = `
            <button ${!data.previous ? "disabled" : ""} class="btn btn-outline-info" id="back_btn">Anterior</button>
            <span>${skip + 1} - ${Math.min(skip+limit, data.count)} de ${data.count}</span>
            <button ${!data.next ? "disabled" : ""} class="btn btn-outline-info" id="next_btn" >Siguiente</button>
        `;
        
        if(data.previous){
            document.getElementById("back_btn").onclick = () =>{
                const url = new URL(data.previous);
                getEstudiantesPaginado(
                    Number(url.searchParams.get("skip")),
                    Number(url.searchParams.get("limit"))
                )
            };
        }
        if(data.next){
            document.getElementById("next_btn").onclick = () =>{
                const url = new URL(data.next);
                getEstudiantesPaginado(
                    Number(url.searchParams.get("skip")),
                    Number(url.searchParams.get("limit"))
                )
            };
        }

    }
}
