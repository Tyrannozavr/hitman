<template>
<div id="statistic">
    <div v-if="rounds === null">
        You must <a href="./">log in</a>
    </div>
  <div>
    <h1><a href="./fight">Fight</a></h1>
  </div>
  <ol>
    <li v-for="round in rounds" v-bind:key="round.id" style="text-align: center">
        <h2>Round N {{ round.num_round }}</h2>
        <h3>Player {{ round.first_player.user }} VS Player {{ round.second_player.user }}</h3>
        <p>Player {{ round.first_player.user }} attack the: {{ round.first_player.attack }}____________________________________________________________________________________________________________
            Player {{ round.second_player.user }} attack the: {{ round.second_player.attack }}
        </p>
        <p>Player {{ round.first_player.user }} defend the: {{ round.first_player.defend }}____________________________________________________________________________________________________________
            Player {{ round.second_player.user }} defend the: {{ round.second_player.defend }}
        </p>
        <h3> {{ round.winner }} </h3>
        <p>Player {{ round.first_player.user }}: {{ round.first_player_score }} score_____________________________________________________________________________________________________________________________
            Player {{ round.second_player.user }}: {{ round.second_player_score }} score</p>
    </li>
  </ol>
</div>
</template>
<script>

import axios from 'axios'
import {BASE_URL, headers} from "@/pages/js/methods";
function part_body (data) {
      var len = data.length
      var part_body = {0: 'head', 1: 'body', 2: 'left hand', 3: 'right hand', 4: 'left foot', 5: 'right foot'};
      for (let i=0; i < len; i++) {
          for (let j=0; j<3; j++) {
           data[i].first_player.attack[j] = part_body[data[i].first_player.attack[j]];
           data[i].first_player.defend[j] = part_body[data[i].first_player.defend[j]];
           data[i].second_player.attack[j] = part_body[data[i].second_player.attack[j]];
           data[i].second_player.defend[j] = part_body[data[i].second_player.defend[j]];
          }
          data[i].first_player.attack = data[i].first_player.attack.join(', ');
          data[i].first_player.defend = data[i].first_player.defend.join(', ');
          data[i].second_player.attack = data[i].second_player.attack.join(', ');
          data[i].second_player.defend = data[i].second_player.defend.join(', ');
          if (data[i].first_player_score > data[i].second_player_score) {
              data[i]['winner'] = `${data[i].first_player.user} Win!`;
          } else {
              if (data[i].first_player_score < data[i].second_player_score)
              {data[i]['winner'] = `${data[i].second_player.user} Win!`;} else {
                  data[i]['winner'] = 'Draw'
              }
          }
      }
}
export default {
  name: 'StatisticPage',
  data () {
    return {
      message: 'Test',
      rounds: null,
    }
  },
  mounted () {
axios.get(BASE_URL + 'fight/statistic', {headers: headers})
    .then(response => (
        part_body(response.data),
        this.rounds = response.data))
    .catch(function (err) {
      console.log(err);
    })
  }
}
</script>
<style>

</style>