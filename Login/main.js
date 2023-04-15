
/*funcion para login*/

function validateEmail()
{
                
	// Get our input reference.
	var emailField = document.getElementById('correo');
    var password = document.getElementById("password").value;

    
	
	// Define our regular expression.
	var validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

	// Using test we can check if the text match the pattern
	if( validEmail.test(emailField.value) ){
		//alert('Email is valid, continue with form submission');
		//return true;
	}else{
		alert('Email es invalido, intente nuevamente.');
		return false;
	}

    if( emailField=="" || password == "")
    {
        alert("Datos Incorrectos")
        return;
    }
    else
    {
    
        alert("Datos correctos")
        window.location.href="../index.html"
    }
};


/*funcion para registro*/

function registro(){
    var email = document.getElementById("recorreo").value
    var nombre = document.getElementById("renombre").value
    var telefono = document.getElementById("telefono").value
    var contrasena1 = document.getElementById("recontraseña").value
    var contrasena2 = document.getElementById("recontraseña2").value
    var expr = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/

    if (contrasena1 != contrasena2){
      alert("LAS CONTRASEÑAS NO COINCIDEN!")
    }
      
    else if (email == "" || !expr.test(email) || nombre == "" || contrasena1 == "" || contrasena2 == "" ||  telefono == ""){
      alert("Por favor, rellena todos los campos o verifique su correo")

    }else{
      alert("TE HAZ REGISTRADO CON EXITO!")
      window.location.href = "index.html";
    }
  }

