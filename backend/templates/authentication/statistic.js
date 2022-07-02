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

axios.get('http://127.0.0.1:8000/fight/statistic/', {
  })
  .then(function (response) {
      var data = response.data;
      part_body(data);
      var app = new Vue({
          el: '#app',
          data: {
              rounds: data
          }
      })
  })
  .catch(function (error) {
      // alert('You must log in ');
            var app = new Vue({
          el: '#app',
          data: {
              rounds: null
          }
      })
    console.log(error);
  });