<template>
  <div id="statistic">
    <div>
      <h1>
        <router-link :to="{name: 'fight'}">Fight</router-link>
      </h1>
    </div>
    <ol>
      <li v-for="round in rounds" v-bind:key="round.id" style="text-align: center">
        <h2>Round N {{ round.num_round }}</h2>
        <h3>Player {{ round.first_player.user }} VS Player {{ round.second_player.user }}</h3>
        <p>Player {{ round.first_player.user }} attack the: {{
            round.first_player.attack.join(', ')
          }}_______________________________________________________________________________________________________
          Player {{ round.second_player.user }} attack the: {{ round.second_player.attack.join(', ') }}
        </p>
        <p>Player {{ round.first_player.user }} defend the: {{
            round.first_player.defend.join(', ')
          }}_______________________________________________________________________________________________________
          Player {{ round.second_player.user }} defend the: {{ round.second_player.defend.join(', ') }}
        </p>
        <h3> {{ round.winner }} </h3>
        <p>Player {{ round.first_player.user }}: {{ round.first_player_score }}
          score________________________________________________________________________________________________________________________
          Player {{ round.second_player.user }}: {{ round.second_player_score }} score</p>
      </li>
    </ol>
  </div>
</template>
<script>

import axiosInstance from "@/utils/AxiosSetting";

export default {
  name: 'StatisticPage',
  data() {
    return {
      message: 'Test',
      rounds: null,
    }
  },
  async mounted() {
    const response = await axiosInstance().get('fight/statistic')
    try {
      this.rounds = response.data;
    } catch (error) {
      console.log(error);
    }
  }
}
</script>
<style>

</style>