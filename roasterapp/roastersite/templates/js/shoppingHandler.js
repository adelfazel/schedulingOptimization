document.addEventListener('DOMContentLoaded',function(){

});

function load_page(name) {
	const request = new XMLHttpRequest();
	request.open("GET",`/menu/${name}`);
  request.onload() => () => {
			const response = request.responseText;


	}
	request.send();

}
