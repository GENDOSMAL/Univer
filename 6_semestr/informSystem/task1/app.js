const express = require("express");

const app = express();
const jsonParser = express.json();

app.use(express.static(__dirname + "/public"));
const port = 3000;

// const filePath = "users.json";
// app.get("/api/users", function(req, res){

//     const content = fs.readFileSync(filePath,"utf8");
//     const users = JSON.parse(content);
//     res.send(users);
// });
// // получение одного пользователя по id
// app.get("/api/users/:id", function(req, res){

//     const id = req.params.id; // получаем id
//     const content = fs.readFileSync(filePath, "utf8");
//     const users = JSON.parse(content);
//     let user = null;
//     // находим в массиве пользователя по id
//     for(var i=0; i<users.length; i++){
//         if(users[i].id==id){
//             user = users[i];
//             break;
//         }
//     }
//     // отправляем пользователя
//     if(user){
//         res.send(user);
//     }
//     else{
//         res.status(404).send();
//     }
// });
// // получение отправленных данных
// app.post("/api/users", jsonParser, function (req, res) {

//     if(!req.body) return res.sendStatus(400);

//     const userName = req.body.name;
//     const userAge = req.body.age;
//     let user = {name: userName, age: userAge};

//     let data = fs.readFileSync(filePath, "utf8");
//     let users = JSON.parse(data);

//     // находим максимальный id
//     const id = Math.max.apply(Math,users.map(function(o){return o.id;}))
//     // увеличиваем его на единицу
//     user.id = id+1;
//     // добавляем пользователя в массив
//     users.push(user);
//     data = JSON.stringify(users);
//     // перезаписываем файл с новыми данными
//     fs.writeFileSync("users.json", data);
//     res.send(user);
// });
//  // удаление пользователя по id
// app.delete("/api/users/:id", function(req, res){

//     const id = req.params.id;
//     let data = fs.readFileSync(filePath, "utf8");
//     let users = JSON.parse(data);
//     let index = -1;
//     // находим индекс пользователя в массиве
//     for(var i=0; i < users.length; i++){
//         if(users[i].id==id){
//             index=i;
//             break;
//         }
//     }
//     if(index > -1){
//         // удаляем пользователя из массива по индексу
//         const user = users.splice(index, 1)[0];
//         data = JSON.stringify(users);
//         fs.writeFileSync("users.json", data);
//         // отправляем удаленного пользователя
//         res.send(user);
//     }
//     else{
//         res.status(404).send();
//     }
// });
// // изменение пользователя
// app.put("/api/users", jsonParser, function(req, res){

//     if(!req.body) return res.sendStatus(400);

//     const userId = req.body.id;
//     const userName = req.body.name;
//     const userAge = req.body.age;

//     let data = fs.readFileSync(filePath, "utf8");
//     const users = JSON.parse(data);
//     let user;
//     for(var i=0; i<users.length; i++){
//         if(users[i].id==userId){
//             user = users[i];
//             break;
//         }
//     }
//     // изменяем данные у пользователя
//     if(user){
//         user.age = userAge;
//         user.name = userName;
//         data = JSON.stringify(users);
//         fs.writeFileSync("users.json", data);
//         res.send(user);
//     }
//     else{
//         res.status(404).send(user);
//     }
// });
// app.use(express.static('default.html'));


app.get('/', function (req, res) {
  res.sendFile('default.html', { root: __dirname + "/" });
});

app.get('/1', function (req, res) {
  res.send('Hello world');
});

app.get('/2', function (req, res) {
  var result = 0;
  for (let index = 1; index <= req.query.n; index++) {
    result += index
  }
  res.send(result + "");
});

app.get('/3', function (req, res) {
  var result = 0;
  for (let index = 1; index <= req.query.n; index++) {
    if (index % 2 == 0 && index % 7 == 0)
      result += index
  }
  res.send(result + "");
});

app.get('/4', function (req, res) {
  var result = "";
  var currentYear = parseInt(new Date().getFullYear());
  for (let index = currentYear; index <= currentYear + 100; index++) {
    if (((index % 4 === 0) && (index % 100 !== 0)) || (index % 400 === 0))
      result += index + "<br>"
  }
  res.send(result + "");
});

app.get('/5', function (req, res) {
  var result = "";
  for (let i = 2; i <= 9; i++) {
    result += `Табл умножения на ${i}<br>`
    for (let j = 2; j <= 10; j++) {
      result += `${i}*${j}=${i * j}<br>`
    }
    result += "<br><br>"
  }
  res.send(result + "");
});

app.get('/6', function (req, res) {
  var result = "";
  var array = getRandomArray(10);
  result += "source  " + outArray(array) + "<br>"
  for (let i = 0, j = array.length - 1; i < j; i++, j--) {
    [array[i], array[j]] = [array[j], array[i]];
  }

  result += "revesed  " + outArray(array) + "<br>"
  res.send(result + "");
});

app.get('/7', function (req, res) {
  var result = "";
  var str = req.query.n;
  var str = str.trim().replace(/\s/g, "").replace(".", "").replace(",", "");
  if (str == "") {
    result = "Не полиндром ибо пусто";
    res.send(result + "");
    return;
  }
  if (str.toUpperCase() == str.split('').reverse().join('').toUpperCase()) {
    result = "Полиндром!"
  }
  else {
    result = "Не полиндром ибо не равно!"
  }
  res.send(result + "");
});

app.get('/8', function (req, res) {
  var result = "";
  var arrayLength = parseInt(req.query.n);
  var arrayFirst = getRandomArray(arrayLength);
  var arraySecond = getRandomArray(arrayLength);
  result += "source first  " + outArray(arrayFirst) + "<br>"
  result += "source second  " + outArray(arraySecond) + "<br>"
  var resArray = arrayFirst;
  for (let i = 0; i < arraySecond.length; i++) {
    resArray[arrayLength + i] = arraySecond[i];
  }
  result += "result " + outArray(resArray) + "<br>"
  res.send(result + "");
});

app.get('/9', function (req, res) {
  var result = "";
  var arrayLength = parseInt(req.query.n);
  var arrayFirst = getRandomArray(arrayLength);
  var arraySecond = getRandomArray(arrayLength);
  result += "source first  " + outArray(arrayFirst) + "<br>"
  result += "source second  " + outArray(arraySecond) + "<br>"

  var resArray = arrayFirst.sort(function (a, b) {
    return a - b;
  });
  for (let i = 0; i < arraySecond.length; i++) {
    var index = sortedIndex(resArray, arraySecond[i]);
    var temp = resArray[index];
    resArray[index] = arraySecond[i];
    for (let j = index + 1; j < resArray.length; j++) {
      var temp2 = resArray[j];
      resArray[j] = temp;
      temp = temp2;
    }
    if (i != arraySecond.length - 1)
      resArray[resArray.length] = temp;
  }

  result += "result " + outArray(resArray) + "<br>"
  res.send(result + "");
});

app.get('/10', function (req, res) {
  var result = "";
  var arrayLength = parseInt(req.query.n);
  var array = getRandomArray(arrayLength);
  result += "source first  " + outArray(array) + "<br>"
  result += "result  " + outArray(quicksort(array)) + "<br>"
  res.send(result + "");
});

function quicksort(array) {
  if (array.length <= 1) {
    return array;
  }

  var pivot = array[0];
  
  var left = []; 
  var right = [];

  for (var i = 1; i < array.length; i++) {
    array[i] < pivot ? left.push(array[i]) : right.push(array[i]);
  }

  return quicksort(left).concat(pivot, quicksort(right));
};

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

function outArray(array) {
  var res = "";
  for (let i = 0; i < array.length; i++) {
    res += `${array[i]} `
  }
  return res;
}

function getRandomArray(length) {
  var array = new Array(length);
  for (let i = 0; i < array.length; i++) {
    array[i] = getRandomInt(50)
  }
  return array;
}

function sortedIndex(array, value) {
  var low = 0,
    high = array.length;
  while (low < high) {
    var mid = low + high >>> 1;
    if (array[mid] < value) low = mid + 1;
    else high = mid;
  }
  return low;
}



app.listen(port, function () {
  console.log("Сервер ожидает подключения...");
});