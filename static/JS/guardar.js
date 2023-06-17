function guardar() {
    const nombres = document.getElementById('nombre');
    const Apellidos = document.getElementById('Apellido')
    const cursos = document.getElementById('curso');
    const Nfichas = document.getElementById('Nficha');
    const documento = document.getElementById('documento');
 
    


    axios
      .post(
        'guardar',
        {
          nombre: nombres.value,
          apellido: Apellidos.value,
          curso: cursos.value,
          Nficha: Nfichas.value,
          documento: documento.value,
          
      
         
        },
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
      .then((res) => {
        Swal.fire({
          position: 'top-center',
          icon: 'success',
          title: '¡Datos registrados exitosamente!',
          showConfirmButton: false,
          timer: 2000,
      })
        console.log(res.data)
      })
      .catch((error) => {
        console.error(error)
      })
  }



  