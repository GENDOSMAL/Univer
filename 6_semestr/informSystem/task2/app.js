const express = require("express");

const app = express();
app.use(express.static(__dirname + "/public"));
const port = 3000;

app.get('/', function (req, res) {
  res.sendFile('default.html', { root: __dirname + "/" });
});

app.get('/1', function (req, res) {
  var a = req.query.a;
  var intToFound = parseInt(req.query.f);
  var resut = "";
  var sourceArray = a.split("_");
  for (let i = 0; i < sourceArray.length; i++) {
    sourceArray[i] = parseInt(sourceArray[i])
  }
  sourceArray = sourceArray.sort(function (a, b) {
    return a - b;
  });
  console.log(sourceArray);
  resut += "Исходный массив  " + outArray(sourceArray) + "<br>"
  resut += "Параметр для поиска " + intToFound + "<br>"
  var indexOfSearchItems = binarySearch(intToFound, sourceArray)
  console.log(indexOfSearchItems);
  console.log(intToFound);
  if (indexOfSearchItems == -1) {
    resut += "<h1>Элемент НЕ найден в списке</h1>"
  }
  else {
    resut += "<h1>Элемент найден в списке под индексом [" + indexOfSearchItems + "] со значением [" + sourceArray[indexOfSearchItems] + "]</h1>"
  }
  res.send(resut + "");
});

app.get('/2', function (req, res) {
  res.send(leapYear(parseFloat(req.query.d)));
});

function leapYear(year) {
  var result = "";
  var tail_1 = year - Math.floor(year);
  result += "Високосный год на вашей планете каждые " + Math.floor(1 / tail_1) + " лет(года).<br>";
  var except = Math.floor((24 * 60 / (60 - (tail_1 * 24 * 60) % 60)) * (1 / tail_1))
  if (except > 0) {
    result += "За исключением каждого " + except + " года";
    result += " (не учитывая возможности округления в сторону веков для удобства счёта)";
  }
  return result;
}

function binarySearch(value, list) {
  let first = 0;
  let last = list.length - 1;
  let position = -1;
  let found = false;
  let middle;

  while (found === false && first <= last) {
    middle = Math.floor((first + last) / 2);
    if (list[middle] == value) {
      found = true;
      position = middle;
    } else if (list[middle] > value) {
      last = middle - 1;
    } else {
      first = middle + 1;
    }
  }
  return position;
}

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