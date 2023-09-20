const app = require('express')();

const http = require('http').Server(app);

const io = require('socket.io')(http);

var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

var username = ''

app.get('/', (req, res) => {
	res.sendfile(__dirname + '/index.html')
})
app.get('/index.js', (req, res) => {
	res.sendfile(__dirname + '/index.js')
})
app.get('/socket.io/socket.io.js', (req, res) => {
	res.sendfile(__dirname + '/node_modules/socket.io/client-dist/socket.io.js')
})
/*app.get('/client.js', (req, res) => {
	res.sendfile('client.js')
})*/
/*app.get('/user' ,(req, res) => {
	res.sendfile(__dirname + '/client.html')
})*/
app.get('/client.css', (req, res) => {
	res.sendfile(__dirname + '/client.css')
})
app.get('/username', (req, res) => {
	res.sendfile(__dirname + '/username.html')
})
app.post('/user', (req,res) => {
	if (req.body.username){
		res.sendfile(__dirname + '/client.html')
		username = req.body.username
	}
	else{
		res.sendfile(__dirname+'/username.html')
	}
})
io.on('connection', (socket) => {
	socket.id = username
	console.log(`a client with id ${socket.id} connected`)
	socket.on('disconnect', () => {
		console.log('user disconnect')
	})
	socket.emit('user', socket.id);
	socket.on('to-server', (data) => {
		console.log(`${socket.id} tell me : ${data}`)
	})
	socket.on('chat message', (data) => {
		console.log(`${socket.id} tell me : ${data}`)
		socket.broadcast.emit('chat message', {'user':socket.id,'data':data});
		console.log({'user':socket.id,'data':data})
	})
});

http.listen(3000, () => console.log('listening on : 3000 port'));

