//* Sebastian Painen */

function validarFormulario(){
    // elimnamos unos alert duplicados -.-*
    $('alert').remove();

    //declaracion de var
    
    var nickname = $('#nickname').val(),
        email = $('#email').val(),
        asunto = $('#asunto').val(),
        comentarios = $('#comentarios').val();

    //validamos el campo nickname

    if(nickname == "" || nickname == null){
        cambiarColor("nickname");
        // mostramos el mensaje de alert
        mostrarAlerta("Campo Obligatorio");
        return false;
    }else{
        var expresion = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(nickname)){
            //muestra un msj que debe ingresar un nickname sin el arroba
            cambiarColor("nickname");
            mostrarAlerta("No se permiten caracteres que contengan : @ ");
        }
    }


    //validamos correo

    if(email == "" || email == null){
        cambiarColor("email");
        // mostramos el mensaje de alert
        mostrarAlerta("Campo Obligatorio");
        return false;
    }else{
        var expresion = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if(!expresion.test(email)){
            //muestra un msj 
            cambiarColor("email");
            mostrarAlerta("Por favor ingrese un correo valido");
        }
    }

    //validamos asunto

    if(asunto=="" || asunto==null){

        cambiarColor("asunto");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    }else{
        var expresion= /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(asunto)){
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("asunto");
            mostraAlerta("No se permiten caracteres especiales");
            return false;
        }
    }

     // validamos el mensaje
     if(comentarios=="" || comentarios==null){

        cambiarColor("comentarios");
        // mostramos el mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    }else{
        var expresion= /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(comentarios)){
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("comentarios");
            mostraAlerta("No se permiten caracteres especiales");
            return false;
        }
    }

$('input').focus(function(){
    $('.alert').remove();
    colorDefault('nickname');
    colorDefault('email');
    colorDefault('asunto');
});

$('textarea').focus(function(){
    colorDefault('comentarios');
});

     var elemento = document.forms["formulario_registro"]["micheckbox"].checked;
     if(elemento == true){
         document.getElementById("info").innerHTML = "Gracias por tu feedback, tus palabras valen mucho !!";
         document.forms["formulario_registro"].reset();
         document.forms["formulario_registro"].addEventListener(alert("Enviado"));
         return false;
     }
     else{
         document.getElementById("info").innerHTML = "Favor lea y seleccione la aceptación terminos";
         return false;
     }


}

let cerrar = document.querySelectorAll(".close")[0];
let abrir = document.querySelectorAll(".cta1")[0];
let modal = document.querySelectorAll(".modal")[0];
let modalC = document.querySelectorAll(".modal-container")[0];

abrir.addEventListener("click" , function(e){
    e.preventDefault();
    modalC.style.opacity = "1";
    modalC.style.visibility = "visible";
    modal.classList.toggle("modal-close");
});

cerrar.addEventListener("click",function(e){
    modal.classList.toggle("modal-close");
    modalC.style.opacity = "0";
    modalC.style.visibility = "hidden";
    setTimeout(function(){
        modalC.style.opacity = "0";
        modalC.style.visibility = "hidden";0
    },1000)

});

// creamos una funcion de color por defecto a los bordes de los inputs
function colorDefault(dato){
    $('#' + dato).css({
        border: "1px solid #999"
    });
}

// creamos una funcion para cambiar de color a su borde de los input

function cambiarColor(dato){
    $('#' + dato).css({
        border: "1px solid #dd5144"
    });
}

// funcion para mostrar alert

function mostrarAlerta(texto){
    $('#nickname').before('<div class="alert">Error: '+ texto + '</div>');
}


// function validarFormulario(){

//     var elemento = document.forms["formulario_registro"]["micheckbox"].checked;
//     if(elemento == true){
//         document.getElementById("info").innerHTML = "Gracias por aceptar!!";
//         document.forms["formulario_registro"].reset();
//         document.forms["formulario_registro"].addEventListener(alert("Enviado"));
//         return false;
//     }
//     else{
//         document.getElementById("info").innerHTML = "Favor lea y seleccione la aceptación terminos";
//         return false;
//     }
// }

window.onload = function(){
	var toggleButton = document.querySelector('.toggleButton').addEventListener('click',function(){
		var border = document.querySelector('.border').classList.toggle("activeBorder");
		var button = document.querySelector('.button').classList.toggle("active");
		var day = document.querySelector('.day').classList.toggle("night");
	})
}