<template>
  <div>
    <h3><a href="..">Log in</a></h3>
    <img src="./images/chelovek.png" alt="chelovek" id="chel1">
    <form @submit.prevent="fight" class="form">
      <p>Выберите 3 элемента атаки</p>
      <select multiple size="6" name="component-select" v-model="attack">
        <option value="голова">Голова</option>
        <option value="туловище">Туловище</option>
        <option value="левая рука">Левая рука</option>
        <option value="правая рука">Правая рука</option>
        <option value="левая нога">Левая нога</option>
        <option value="правая нога">Правая нога</option>
      </select>
      <p>Выберите 3 элемента защиты</p>
      <select multiple size="6" name="component-select" v-model="defend">

        <option value="голова">Голова</option>
        <option value="туловище">Туловище</option>
        <option value="левая рука">Левая рука</option>
        <option value="правая рука">Правая рука</option>
        <option value="левая нога">Левая нога</option>
        <option value="правая нога">Правая нога</option>
      </select>
      <br>
      <button type="submit" id="push">Fight</button>
    </form>
    <h3><a href="./statistic">Statistic</a></h3>
  </div>
</template>

<script>
import instance from '@/pages/js/methods'

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
      if (check_length(this.attack, 'атаки') && check_length(this.defend, 'защиты')) {
        instance({requiresAuth: true}).post('fight/', {
          attack: this.attack,
          defend: this.defend
        })
            .then( function(response) {
              if (response && response.data && response.data.detail === 'fight only one user') {
                alert('Your move is recorded, wait for another player\'s move')
              } else {
                alert('the battle is done, see the statistics')
              }
            })
            .catch(function (err) {
              // console.log('error_fight', err.response.data.detail)
              if (err.response && err.response.data.detail === 'You do not have permission to perform this action.') {
                alert('Please wait for your opponent\'s turn')
              } else {
                console.log(err);
              }
            })
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