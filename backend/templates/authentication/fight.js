function transform(array) {
    answer = []
    for (var i = 0; i < 6; i++) {
        if (array[i].selected === true) {
            answer.push(i)
        }
    }
    return answer
}

function foo() {
    var attack = document.getElementById('select2').options;
    var defend = document.getElementById('select1').options;
    var x = document.getElementById('select2');
    transform(x.options)
    attack_val = check_length(attack, 'атаки');
    defend_val = check_length(defend, 'защиты')
    if (attack_val === true) { if (defend_val === true) {
        fight(transform(defend), transform(attack));
    }}
};

function check_length(array, str) {
    var l = array.length;
    var num_selected = 0;

    for (var i = 0; i < l; i++) {
        if (array[i].selected === true) {
            num_selected++;
        };
    };
    if (num_selected > 3) {
        alert('Вы не можете выбрать более 3-х элеменов '+str);
    } else {if (num_selected < 3) {alert('Вы не можете выбрать менее 3-х элементов '+str)} else {
        return true;
    }};
}

function fight(defend, attack) {
    axios.post('http://127.0.0.1:8000/fight/', {
        defend: defend,
        attack: attack,
    }, {headers: {
        Authorization: `Token ${sessionStorage.getItem('token')}`
        }}).catch( function (err) {
            alert('You must log in');
    })
}

function test() {
    return true
}

var answer = null
function authenticate_f() {
    axios.post('http://127.0.0.1:8000/api/', {
  }, {headers: {
        Authorization: `Token ${sessionStorage.getItem('token')}`
        }})
  .then(function (response) {
       answer = true;}).catch( function() {
          console.log('error')
         answer = false;
    })
    console.log('aa', answer);
    return answer
}

// var app1 = new Vue({
//     el: '#app-1',
//     data: {
//         message: 'Hello, Vue',
//         // authenticate: authenticate_f(),
//         authenticate: true,
//     }})
// authenticate_f();