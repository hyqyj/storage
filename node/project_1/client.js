const io = require('socket.io-client');
const socket = io('http://127.0.0.1:3000');

socket.on('connect', (socket) => {
	console.log('connected to server!');
})

socket.on('disconnect', () =>{
	console.log('dis connect')
})
socket.emit('to-server', 'hello my server')
socket.on('to-client', (data) => {
	console.log('server tell me :' + data)
	
})


/*	var socket = io('http://127.0.0.1:3000');
	socket.on('connect', () => {
		console.log('connect to server')
	})

	socket.on('disconnect', () => {
		console.log('dis connect ')
	})

	socket.on('to-client', (data) => {
		console.log('server tell me :' + data)
	})

	btn.onclick = function () {
		var val = message.value
		socket.emit('to-server',val)
*/