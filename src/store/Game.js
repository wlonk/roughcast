import api from '../api';

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
      };
    },
  },
  actions: {
    async retrieveGames({ commit }) {
      const resp = await api.get('/game/');
      if (resp.ok) {
        const games = resp.data;
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
      const response = await api.get(`/game/${id}/`);
      if (response.ok) {
        const game = response.data;
        commit('getGameById', game);
      } else {
        // TODO: Display lookup error toast?
      }
    },
    async createNewGame({ commit }, data) {
      const response = await api.post('/game/', data);
      if (response.ok) {
        const newGame = response.data;
        commit('getGameById', newGame);
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default Game;
