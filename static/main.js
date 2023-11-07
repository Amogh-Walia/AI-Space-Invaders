let canvas, 
		c, 
		invaders, 
		w, 
		h, 
		dt, 
		player, 
		lives,
		lastUpdate,
		div,
		kill,
		generation,
		Board;

canvas = document.createElement('canvas');
canvas.width = w = 240;
canvas.height = h = 480;
Board = []
var socket = io();
const loc = [[],[],[],[],[],[],[]];


c = canvas.getContext('2d',{alpha: false});
if (window.devicePixelRatio > 1) {
	c.canvas.width = c.canvas.width * window.devicePixelRatio;
	c.canvas.height = c.canvas.height * window.devicePixelRatio;
	c.canvas.style.width = w+'px';
	c.canvas.style.height = h+'px';
	c.scale(window.devicePixelRatio, window.devicePixelRatio);
}

div = document.createElement('div');

function init(){
	lives = 0;
	generation = 1;
	dt = 210;
	kill =0;
	lastUpdate = Date.now();
	canvas.style.border = "solid";
	document.body.appendChild( canvas );
	document.body.appendChild( div );
	invaders = new Genetics();
	invaders.createPopulation();
	player = new Player( w/4/2, h/4-4 );
	
	update();
}

Pulse = 0;

function waitForValue() {
	return new Promise((resolve) => {
	  socket.on('Pulse', (data) => {
		resolve(data)
	  });
	});
  }

function UpdateTable() {
	return new Promise((resolve) => {
	  socket.on('TABLE', (data) => {
		resolve(data)
	  });
	});
  }

async function Table(){
	data = await UpdateTable();
	Board = data;

}


async function deltaTime(){

	console.log(dt)
	if (dt != 0) {
		player.isMovingLeft = false;
		player.isMovingRight= false;
		
	}
	
	data = await waitForValue();
	dt = data[0];
	player.isMovingLeft = data[1]==1 ? true:false;
	player.isMovingRight = data[2]==1 ? true:false;
	data[3]==1 ? player.shoot():null;

}

function getBestOfGeneration(){
	let index = 0, best = 0;
	for(let i = 0; i < invaders.population.length; i++){
		if( invaders.population[i].fit > best ){
			best = invaders.population[i].fit;
			index = i;
		}
	}
	if( !invaders.bestOfGeneration || invaders.population[index].fit > invaders.bestOfGeneration.fit ){
		invaders.bestOfGeneration = invaders.population[index];
	}
}



function update(){
	c.fillStyle = "white";
	c.fillRect(0,0,w,h);
	c.fillStyle = "black";
	c.font = "10px Arial";
	c.fillText("Generation: "+generation, 5, 10);
	c.fillText("Invaders Missed: "+lives, 5, 20);
	c.fillText("Invaders Killed: "+kill, 5, 30);
	for(let i = 0; i < invaders.population.length; i++){
		invaders.population[i].show();
	}
	player.show();
	let allDead = true;
	for(let i = 0; i < invaders.population.length; i++){
		if( invaders.population[i].isAlive ){
			allDead = false;
			break;
		}
	}
	if(allDead){
		getBestOfGeneration();
		if(generation%7){
			invaders.evolve();
		}else{
			invaders.elitism();
		}
		generation++;
	}



	deltaTime();
	requestAnimationFrame(update);

	
}



socket.emit("Init");

socket.on('RESET', function(){
	console.log('RESET');
	init();
 });



socket.on('FETCH', function(){
	console.log('FETCHING');
	const variablesToSend = {
		Arr: loc,
		gen: generation,
		kills: kill
	};
	console.log(variablesToSend);
	fetch('data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(variablesToSend)
	})
	.then(response => {
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		return response.json();
	})
 });