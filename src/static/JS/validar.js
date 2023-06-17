function Login() {
    const correo = document.getElementById('documento');
    const pass = document.getElementById('Input');
    axios.post('login', {
        Ndocumento: correo.value,
        contraseña: pass.value
    })
        .then(function (response) {
            console.log(response)
                window.location.href = '/fronted/menu';
        })
        .catch(function (error) {
            console.log(error);
            Swal.fire({
                            position: 'top-center',
                            icon: 'error',
                            title: '¡Datos invalidos!',
                            showConfirmButton: false,
                            timer: 2000,          
                        })
                        document.getElementById('documento').value="";
                        document.getElementById('Input').value="";
        });
}

// Este es el ojo que sirve para visualizar la contraseña
var input = document.getElementById('Input');
        var img = document.getElementById('Clave');

        img.addEventListener("click", function () {
            if (input.type == "password") {
                input.type = "text"
            } else {
                input.type = "password"
            }
        })

        