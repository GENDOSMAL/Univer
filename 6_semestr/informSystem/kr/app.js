const express = require("express");
const fs = require('fs')
const os = require("os");

const app = express();
app.use(express.static(__dirname + "/public"));
const port = 3000;

app.get('/', function (req, res) {
	res.sendFile('default.html', { root: __dirname + "/" });
});

app.get('/osinfo', function (req, res) {
	var resut = "";
	resut += "Путь до темповой директории: " + os.tmpdir() + "<br>"
	resut += "Имя хоста: " + os.hostname() + "<br>"
	resut += "Тип ОС: " + os.type() + "<br>"
	resut += "Время работы ОС: " + toDDHHMMSS(os.uptime()) + "<br>"
	resut += "Доступная оперативная память: " + Math.round(os.freemem() / (1024 * 1024)) + "<br>"
	resut += "Информация о ЦП: " + getCpu() + "<br>"
	resut += "Информация о сетевых интерфейсах: " + getNetwork() + "<br>"
	res.send(resut + "");
});

app.listen(port, function () {
	console.log("Сервер ожидает подключения...");
});

function getCpu() {
	var res = "";
	var count = 0;
	os.cpus().forEach(element => {
		res = `[${element.model.trim()}]:${element.speed}`
		count += 1;
	});
	res += ":" + count + " threads"
	return res;
}

function getNetwork() {
	var res = "";
	var interfaces = os.networkInterfaces();
	for (let iface in interfaces) {
		res += "[" + iface + ""
		for (let i in interfaces[iface]) {
			var f = interfaces[iface][i];
			res += " ip:" + f.address + " mac:" + f.mac + " netMask:" + f.netmask;
		}
		res += "]"
	}
	return res;
}

var toDDHHMMSS = (secs) => {
	var secNum = parseInt(secs, 10)
	var days = Math.floor(secNum / 3600 / 24)
	var hours = Math.floor(secNum / 3600)% 24
	var minutes = Math.floor(secNum / 60) % 60
	var seconds = secNum % 60

	return [days, hours, minutes, seconds]
		.map(v => v < 10 ? "0" + v : v)
		.filter((v, i) => v !== "00" || i > 0)
		.join(":")
}
