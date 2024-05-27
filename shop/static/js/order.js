let knopka = document.querySelector(".button_166");
let modalknopka = document.querySelector(".btn btn-primary");
let id_tovar = document.querySelector(".nazvanie-soder");


/* Функция для получения значения cookie по ключу:*/

/*
function getCookie(name) {
	var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
	return matches ? decodeURIComponent(matches[1]) : undefined;
}


function prizrak(){
	console.log(getCookie('authorization'))
	sv = (getCookie('authorization'))
	if (sv == "\"successful authorization\"")
		{console.log('yes'), knopka.setAttribute("href", "/send-message/");}
	else {console.log('no'), knopka.setAttribute("data-bs-toggle", "modal"), knopka.setAttribute("data-bs-target", "#exampleModal");}

}

prizrak()
