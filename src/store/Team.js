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
    const resp = await api.get('teams/');
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
    const response = await api.get(`teams/${id}/`);
    if (response.ok) {
      const team = response.data;
      commit('getTeamById', team);
    } else {
      // TODO: Display lookup error toast?
    }
  },
  async createNewTeam({ commit }, data) {
    const response = await api.post('teams/', data);
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
  listTeams: (state) => {
    return _.values(state.all);
  },
  myTeams: (state) => {
    return _.filter(state.all, (t) => t.user_is_member);
  },
  dryTeam: (state) => (slug) => {
    return _.find(state.all, (p) => p.slug === slug);
  },
  hydratedTeam: (state, getters, rootState) => (slug) => {
    const team = _.find(state.all, (p) => p.slug === slug);
    const games = _.filter(rootState.Game.all, (t) => t.team === team.slug);
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
