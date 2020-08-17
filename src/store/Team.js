import _ from 'lodash';
import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setTeams(state, teams) {
    state.all = teams;
  },
  getTeamById(state, team) {
    state.all = {
      ...state.all,
      [team.id]: team,
    };
  },
};

const actions = {
  async retrieveTeams({ commit }) {
    const resp = await api.get('/team/');
    if (resp.ok) {
      const teams = resp.data;
      const teamsObj = teams.reduce((acc, curr) => {
        acc[curr.id] = curr;
        return acc;
      }, {});
      commit('setTeams', teamsObj);
    } else {
      // TODO display error
    }
  },
  async getTeamById({ commit, state }, id) {
    if (state.all[id] !== undefined) {
      return;
    }
    const response = await api.get(`/team/${id}/`);
    if (response.ok) {
      const team = response.data;
      commit('getTeamById', team);
    } else {
      // TODO: Display lookup error toast?
    }
  },
  async createNewTeam({ commit }, data) {
    const response = await api.post('/team/', data);
    if (response.ok) {
      const newTeam = response.data;
      commit('getTeamById', newTeam);
      commit('retrieveTeamMemberships');
    } else {
      // TODO: Display lookup error toast?
    }
  },
};

const getters = {
  listTeams: state => {
    return _.values(state.all);
  },
  dryTeam: state => slug => {
    return _.find(state.all, p => p.slug === slug);
  },
  hydratedTeam: (state, getters, rootState) => slug => {
    const team = _.find(state.all, p => p.slug === slug);
    const games = _.filter(
      rootState.Game.all,
      g => g.team === team.slug,
    );
    return {
      ...team,
      games,
    };
  },
};

const Team = {
  state,
  mutations,
  actions,
  getters,
};

export default Team;
