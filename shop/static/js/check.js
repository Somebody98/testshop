let modal_content = document.querySelector('.modal-content')
let modal_content2 = document.querySelector('.modal-content2')


// Функция для получения значения cookie по ключу:
function getCookie(name) {
	var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
	return matches ? decodeURIComponent(matches[1]) : undefined;
}


function check(){
	console.log(getCookie('authorization'))
	sv = (getCookie('authorization'))
	if (sv == "\"successful authorization\"")
		{}
	else {console.log('yes');modal_content.style.display=('none');modal_content2.style.display=null;   const header = document.createElement("h1");const  headerText = document.createTextNode("Hello World");   }

}

check()