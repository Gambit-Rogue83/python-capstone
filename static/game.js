
var buttons = document.querySelectorAll('button');
var move = document.querySelector('.move')
var form = document.querySelector('form')
var hunter_a = document.querySelector('#J17')
var hunter_b = document.querySelector('#K17')

hunter_a.classList.add('huntee')
hunter_b.classList.add('hunter')

let agentSpace = ''

buttons.forEach(button =>{
    button.addEventListener('click', () =>{
        if(agentSpace){
            var prevSpace = document.getElementById(agentSpace)
            prevSpace.classList.remove('selected')
        }

        agentSpace = button.id;
        button.classList.add('selected');
        document.getElementById('selected-button').value = agentSpace;
        move.innerHTML = agentSpace
    })
})

form.addEventListener('submit', (e) =>{
    e.preventDefault();

    var formData = {
        agentField: agentSpace,
        agentDetected: document.querySelector('#spotted').checked,
        usedItem: document.querySelector('#equipment').checked,
        taskCompleted: document.querySelector('#objective').checked
    }

    fetch('/game-update', {
        method: 'POST',
        body: JSON.stringify(formData),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then((response) => response.json())
    .then((movement) =>{
        console.log(movement)
    var prevHunterA = hunter_a
    var prevHunterB = hunter_b

    if (prevHunterA) {;
        prevHunterA.classList.remove('huntee');
    }

    if (prevHunterB) {
        prevHunterB.classList.remove('hunter');
    }


    // Update the positions of the hunters
    hunter_a = document.getElementById(movement[0])
    hunter_b = document.getElementById(movement[1])

    hunter_a.classList.add('huntee');
    hunter_b.classList.add('hunter');
});
    })
