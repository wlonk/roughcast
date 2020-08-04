import Vue from 'vue';

const Game = {
  state: () => ({
    all: {},
  }),
  mutations: {
    setGames(state, games) {
      state.all = games;
    },
    getGameById(state, game) {
      state.all = {
        ...state.all,
        [game.id]: game,
      }
    },
  },
  actions: {
    async retrieveGames({ commit }) {
      const resp = await fetch('/api/game/');
      if (resp.ok) {
        const games = await resp.json();
        const gamesObj = games.reduce((acc, curr) => {
          acc[curr.id] = curr;
          return acc;
        }, {});
        commit('setGames', gamesObj);
      } else {
        // TODO display error
      }
    },
    async getGameById({ commit, state }, id) {
      if (state.all[id] !== undefined) {
        return;
      }
      const response = await fetch(`/api/game/${id}/`);
      if (response.ok) {
        const game = await response.json();
        commit('getGameById', game);
      } else {
        // TODO: Display lookup error toast?
      }
    },
    async createNewGame({ commit, state }, data) {
      const csrftoken = Vue.$cookies.get('csrftoken');
      const response = await fetch('/api/game/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const newGame = await response.json();
        commit('getGameById', newGame);
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default Game;
