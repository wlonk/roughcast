import _ from 'lodash';
import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setGames(state, games) {
    state.all = games;
  },
  getGameById(state, game) {
    state.all = {
      ...state.all,
      [game.id]: game,
    };
  },
};

const actions = {
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
};

const getters = {
  listGames: state => {
    return _.values(state.all);
  },
  gamesForTeam: state => team => {
    return _.filter(state.all, g => g.team === team);
  },
  dryGame: state => slug => {
    return _.find(state.all, g => g.slug === slug);
  },
  hydratedGame: (state, getters, rootState) => slug => {
    const game = _.find(state.all, g => g.slug === slug);
    const team = _.find(rootState.Team.all, p => p.slug === game.team);
    const versions = _.filter(rootState.Version.all, v => v.game === game.slug);
    return {
      ...game,
      team,
      versions,
    };
  },
};

const Game = {
  state,
  mutations,
  actions,
  getters,
};

export default Game;
