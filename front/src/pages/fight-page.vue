<template>
  <div>
    <h3><a href="./">Log in</a></h3>
    <div>
      <img src="./images/chelovek.png" alt="chelovek" id="chel1">
      <img src="./images/chelovek.png" alt="chelovek" id="chel2">
        <form class="form">
        <p>Выберите 3 элемента для защиты</p>
        <select id="select1" multiple size="6" name="component-select">
          <option>Голова</option>
          <option>Туловище</option>
          <option>Левая рука</option>
          <option>Правая рука</option>
          <option>Левая нога</option>
          <option>Правая нога</option>
        </select>
        <br>
      </form>
      <form class="form">
        <p>Выберите 3 элемента для атаки</p>
        <select id="select2" multiple size="6" name="component-select">
          <option value="head">Голова</option>
          <option value="body">Туловище</option>
          <option value="l_hand">Левая рука</option>
          <option value="r_hand">Правая рука</option>
          <option value="l_foot">Левая нога</option>
          <option value="r_foot">Правая нога</option>
        </select>
        <br>
      </form>
      <br>
      <input id='push' type="button" value="fight!" @click="foo">
    </div>
    <h3><a href="./statistic">Statistic</a></h3>
  </div>

</template>
<script>
import axios from 'axios'
function transform(array) {
    var answer = []
    for (var i = 0; i < 6; i++) {
        if (array[i].selected === true) {
            answer.push(i)
        }
    }
    return answer
}
function check_length(array, str) {
    var l = array.length;
    var num_selected = 0;

    for (var i = 0; i < l; i++) {
        if (array[i].selected === true) {
            num_selected++;
        }
    }
    if (num_selected > 3) {
        alert('Вы не можете выбрать более 3-х элеменов '+str);
    } else {if (num_selected < 3) {alert('Вы не можете выбрать менее 3-х элементов '+str)} else {
        return true;
    }}
}
//
function fight(defend, attack) {
    axios.post('http://127.0.0.1:8000/fight/', {
        defend: defend,
        attack: attack,
    }, {headers: {
        Authorization: `Token ${sessionStorage.getItem('token')}`
        }}).catch( function (err) {
            if (err.response.data === 'please wait') {
                alert('Please wait step second user')
            } else {
                alert('You must log in')
            }
    })
}
export default {
  methods: {
     foo() {
  var attack = document.getElementById('select2').options;
  var defend = document.getElementById('select1').options;
  var x = document.getElementById('select2');
  transform(x.options)
  var attack_val = check_length(attack, 'атаки');
  var defend_val = check_length(defend, 'защиты')
  if (attack_val === true) {
    if (defend_val === true) {
      fight(transform(defend), transform(attack));
    }
  }
}
}
}
</script>
<style>
.form {float:left; width:50%}
#push {width: 30%}
#chel2 {margin-left: 200px}
</style>