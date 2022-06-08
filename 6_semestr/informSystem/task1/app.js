const express = require("express");

const app = express();
const jsonParser = express.json();

app.use(express.static(__dirname + "/public"));
const port = 3000;

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