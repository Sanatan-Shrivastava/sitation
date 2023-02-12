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
    const data = {
        city: loc,
        sector: sec,
        budget: bud
    }

    console.log(data)
    fetch('http://localhost:5000/landData', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => console.log("Response from server:", data))
    
    .catch(error => console.error("Error:", error));

    
}
 
