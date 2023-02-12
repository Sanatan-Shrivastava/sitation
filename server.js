var loc;

function setLocation() {
    loc = document.getElementById('location').value;
}

var sec;

function setSector() {
    sec = document.getElementById('sector').value;
}

var bud;

function setBudget() {
    bud = document.getElementById('budget').value;
    bud = bud/2;
}

function estimate() {
    const data1 = {
        city: loc,
        sector: sec,
        budget: bud
    }

    console.log(data1)
    fetch('http://localhost:5000/landData', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data1)
    })
    .then(response => response.json())
    .then(data => console.log("Response from server:", data))
    
    .catch(error => console.error("Error:", error));
}

var accordian = document.getElementById('accordionExample')
var site = document.getElementById('site')
var loc_site = document.getElementById('loc_site')
var roi = document.getElementById('roi')
var addr = document.getElementById('address')
var landarea = document.getElementById('land_area')
var landval = document.getElementById('land_val')
var qoz = document.getElementById('qoz')
var sec = document.getElementById('sec')
var invest = document.getElementById('invest')

