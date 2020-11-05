window.onload = function(){
	var toggleButton = document.querySelector('.toggleButton').addEventListener('click',function(){
		var border = document.querySelector('.border').classList.toggle("activeBorder");
		var button = document.querySelector('.button').classList.toggle("active");
		var day = document.querySelector('.day').classList.toggle("night");
	})
}

$('.toggle').click(function(){
    $('.formulario').animate({
        height: "toggle",
        'padding-top': 'toggle',
        'padding-bottom': 'toggle',
        opacity: 'toggle'
    }, "slow");
});

