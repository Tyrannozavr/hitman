<template>
  <div>
    <h3><a href="..">Log in</a></h3>
    <img src="./images/chelovek.png" alt="chelovek" id="chel1">
    <form @submit.prevent="fight" class="form">
      <p>Выберите 3 элемента атаки</p>
      <select multiple size="6" name="component-select" v-model="attack">
        <option value="0">Голова</option>
        <option value="1">Туловище</option>
        <option value="2">Левая рука</option>
        <option value="3">Правая рука</option>
        <option value="4">Левая нога</option>
        <option value="5">Правая нога</option>
      </select>
      <p>Выберите 3 элемента защиты</p>
      <select multiple size="6" name="component-select" v-model="defend">

        <option value="0">Голова</option>
        <option value="1">Туловище</option>
        <option value="2">Левая рука</option>
        <option value="3">Правая рука</option>
        <option value="4">Левая нога</option>
        <option value="5">Правая нога</option>
      </select>
      <br>
      <button type="submit" id="push">Fight</button>
    </form>
    <h3><a href="./statistic">Statistic</a></h3>
  </div>
</template>

<script>
import axios from "axios";

function check_length(array, str) {
  var sum_selected = array.length;
  if (sum_selected > 3) {
    alert('Вы не можете выбрать более 3-х элеменов ' + str);
  } else {
    if (sum_selected < 3) {
      alert('Вы не можете выбрать менее 3-х элементов ' + str)
    } else {
      return true;
    }
  }
}

export default {
  name: "test-page",
  data() {
    return {
      attack: [],
      defend: [],
    }
  },
  methods: {
    fight() {
      if (check_length(this.attack, 'атаки') === true) {
        if (check_length(this.defend, 'защиты') === true) {
          axios.post("http://127.0.0.1:8000/fight/", {
            attack: this.attack,
            defend: this.defend,
          }, {
            headers: {
              Authorization: `Token ${sessionStorage.getItem('token')}`
            }
          })
              .then( function(response) {
                console.log('success', response);
              })
              .catch(function (err) {
                if (err.response.data.detail === 'You do not have permission to perform this action.') {
                  alert('Please wait step second user')
                } else {
                  console.log(err.data);
                  alert('Some error has occurred')
                }
              })
        }
      }
    }
  }
}
</script>

<style scoped>
.form {
  float: left;
  width: 50%
}

#push {
  width: 30%
}
</style>