// validaciones.js
function validarFormulario() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Validación del nombre de usuario
    if (username === "") {
        alert("Por favor, ingresa tu nombre de usuario.");
        return false;
    }

    // Validación de la contraseña
    if (password === "") {
        alert("Por favor, ingresa tu contraseña.");
        return false;
    }

    // Validación adicional si es necesario

    // Envío del formulario si pasa todas las validaciones
    return true;
}
