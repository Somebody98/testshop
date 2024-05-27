
function set(){
//    if (window.localStorage['candyname'] != undefined){
//        ob = window.localStorage['candyname']

const user = "Tom";

const xhr = new XMLHttpRequest();

// обработчик получения ответа сервера
xhr.onload = () => {
    if (xhr.status == 200) {
        console.log(xhr.responseText);
    } else {
        console.log("Server response: ", xhr.statusText);
    }
};

// POST-запрос к ресурсу /user
xhr.open("POST", "/user");
xhr.send(user);     // отправляем значение user в методе send
//    .(response => response.json()) // Преобразуем полученный ответ в JSON
//        .then(data => console.log(data)) // Обрабатываем данные, полученные в ответе
//        .catch(error => console.error('Ошибка:', error)); // Если возникли ошибки, выводим их в консоль
//        }
}

set()