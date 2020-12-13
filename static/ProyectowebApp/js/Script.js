const grid = new Muuri('.grid-armas',{
    layout: {
        rounding: false
    }




});
window.onload = function(){
	var toggleButton = document.querySelector('.toggleButton').addEventListener('click',function(){
		var border = document.querySelector('.border').classList.toggle("activeBorder");
		var button = document.querySelector('.button').classList.toggle("active");
		var day = document.querySelector('.day').classList.toggle("night");
	})
}

window.addEventListener('load', () => {
    grid.refreshItems().layout();
    document.getElementById('grid-armas').classList.add('imagenes-cargadas');

    const enlaces = document.querySelectorAll('#categorias a');
    enlaces.forEach ((elemento) => {
        elemento.addEventListener('click', (evento)=>{
            evento.preventDefault();
            enlaces.forEach((enlace) => enlace.classList.remove('activo'));
            evento.target.classList.add('activo');



            const categoria = evento.target.innerHTML.toLowerCase();
            categoria === 'todas' ? grid.filter('[data-categoria]') : grid.filter(`[data-categoria = "${categoria}"]`);

        });

    });

    //BARRA BUSQUEDA :)

    document.querySelector('#barra-busqueda').addEventListener(('input'), (evento)=> {
        const busqueda = evento.target.value;
        grid.filter((item)=> item.getElement().dataset.etiquetas.includes(busqueda) );
    });

    //LISTENER IMAGENES
    const overlay = document.getElementById('overlay-armas');
    document.querySelectorAll('.grid-armas .item img').forEach((elemento) => {
        
        elemento.addEventListener('click',()=>{
            const ruta = elemento.getAttribute('src');
            const descripcion = elemento.parentNode.parentNode.dataset.descripcion;
            overlay.classList.add('activo');
            document.querySelector('#overlay-armas img').src =ruta;
            document.querySelector('#overlay-armas .descripcion-arma').innerHTML =descripcion;
        });
    });
// Listener Cerrar armas

document.querySelector('#btn-cerrar-ventana').addEventListener('click', () => {
    overlay.classList.remove('activo');
});
// LISTENER OVERLAY


overlay.addEventListener('click', (evento) => {
    
    evento.target.id == 'overlay-armas' ? overlay.classList.remove('activo') : '';
}); 

});
