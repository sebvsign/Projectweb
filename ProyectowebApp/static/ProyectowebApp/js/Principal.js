alert("Bienvenido");

//* GRUPO */

const grid = new Muuri('.grid', {
	layout: {
		rounding: false
	}
});

/* LO QUE MAS NOS COSTO*/
window.addEventListener('load', () => {
	grid.refreshItems().layout();
	document.getElementById('grid').classList.add('imagenes-cargadas');

	// Agregamos los listener de los enlaces para filtrar por categoria.
	const enlaces = document.querySelectorAll('#categorias a');
	enlaces.forEach((elemento) => {
		elemento.addEventListener('click', (evento) => {
			evento.preventDefault();
			enlaces.forEach((enlace) => enlace.classList.remove('activo'));
			evento.target.classList.add('activo');

			const categoria = evento.target.innerHTML.toLowerCase();
			categoria === 'todos' ? grid.filter('[data-categoria]') : grid.filter(`[data-categoria="${categoria}"]`);
		});
	});

	// Agregamos el listener para la barra de busqueda
	document.querySelector('#barra-busqueda').addEventListener('input', (evento) => {
		const busqueda = evento.target.value;
		grid.filter( (item) => item.getElement().dataset.etiquetas.includes(busqueda) );
	});

	// Agregamos listener para las imagenes
	const overlay = document.getElementById('overlay');
	document.querySelectorAll('.grid .item img').forEach((elemento) => {
		elemento.addEventListener('click', () => {
			const ruta = elemento.getAttribute('src');
			const descripcion = elemento.parentNode.parentNode.dataset.descripcion;

			overlay.classList.add('activo');
			document.querySelector('#overlay img').src = ruta;
			document.querySelector('#overlay .descripcion').innerHTML = descripcion;
		});
	});

	// Eventlistener del boton de cerrar
	document.querySelector('#btn-cerrar-popup').addEventListener('click', () => {
		overlay.classList.remove('activo');
	});

	// Eventlistener del overlay
	overlay.addEventListener('click', (evento) => {
		evento.target.id === 'overlay' ? overlay.classList.remove('activo') : '';
	});
});

//* Bastian Diaz */

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

let cerrar1 = document.querySelectorAll(".closeH")[0];
let abrir1 = document.querySelectorAll(".cta2")[0];
let modal1 = document.querySelectorAll(".modal1")[0];
let modalC1 = document.querySelectorAll(".modal-container-haven")[0];

abrir1.addEventListener("click" , function(e){
    e.preventDefault();
    modalC1.style.opacity = "1";
    modalC1.style.visibility = "visible";
    modal1.classList.toggle("modal-closeH");
});

cerrar1.addEventListener("click",function(e){
    modal1.classList.toggle("modal-closeH");
    modalC1.style.opacity = "0";
    modalC1.style.visibility = "hidden";
    setTimeout(function(){
        modalC1.style.opacity = "0";
        modalC1.style.visibility = "hidden";0
    },1000)

});

let cerrar2 = document.querySelectorAll(".closeS")[0];
let abrir2 = document.querySelectorAll(".cta3")[0];
let modal2 = document.querySelectorAll(".modal2")[0];
let modalC2 = document.querySelectorAll(".modal-container-split")[0];

abrir2.addEventListener("click" , function(e){
    e.preventDefault();
    modalC2.style.opacity = "1";
    modalC2.style.visibility = "visible";
    modal2.classList.toggle("modal-closeS");
});

cerrar2.addEventListener("click",function(e){
    modal2.classList.toggle("modal-closeS");
    modalC2.style.opacity = "0";
    modalC2.style.visibility = "hidden";
    setTimeout(function(){
        modalC2.style.opacity = "0";
        modalC2.style.visibility = "hidden";0
    },1000)

});


let cerrar3 = document.querySelectorAll(".closeA")[0];
let abrir3 = document.querySelectorAll(".cta4")[0];
let modal3 = document.querySelectorAll(".modal3")[0];
let modalC3 = document.querySelectorAll(".modal-container-ascent")[0];

abrir3.addEventListener("click" , function(e){
    e.preventDefault();
    modalC3.style.opacity = "1";
    modalC3.style.visibility = "visible";
    modal3.classList.toggle("modal-closeA");
});

cerrar3.addEventListener("click",function(e){
    modal3.classList.toggle("modal-closeA");
    modalC3.style.opacity = "0";
    modalC3.style.visibility = "hidden";
    setTimeout(function(){
        modalC3.style.opacity = "0";
        modalC3.style.visibility = "hidden";0
    },1000)

});

//* sebastian carrasco */

window.onload = function(){
	var toggleButton = document.querySelector('.toggleButton').addEventListener('click',function(){
		var border = document.querySelector('.border').classList.toggle("activeBorder");
		var button = document.querySelector('.button').classList.toggle("active");
		var day = document.querySelector('.day').classList.toggle("night");
	})
}

