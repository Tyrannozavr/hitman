function foo() {
    var x = document.getElementById('select2').options;
    attack = check_length(x, 'атаки');
    // console.log(attack);
    if (attack == true) {
        console.log(this.attack);
        fight(this.defend, this.attack);
    }
};
function check_length(array, str) {
    var l = array.length;
    var num_selected = 0;

    for (var i = 0; i < l; i++) {
        if (array[i].selected == true) {
            num_selected++;
        };
    };
    if (num_selected > 3) {
        alert('Вы не можете выбрать более 3-х элеменов '+str);
    } else {if (num_selected < 3) {alert('Вы не можете выбрать менее 3-х элементов '+str)} else {
        return true;
    }};
}

function fight(protect, attack) {
    axios.post('http://127.0.0.1:8000/fight/', {
        defend: [1,2,3],
        attack: [1,2,3],
    })
}
