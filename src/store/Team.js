import _ from 'lodash';
import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setTeams(state, teams) {
    state.all = teams;
  },
  setTeamById(state, team) {
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
      commit('setTeamById', team);
    } else {
      // TODO: Display lookup error toast?
    }
  },
  async createNewTeam({ commit }, data) {
    try {
      const response = await api.post('teams/', data);
      const newTeam = response.data;
      commit('setTeamById', newTeam);
      return {};
    } catch (error) {
      if (error.response) {
        return error.response.data;
      } else {
        return {
          non_field_errors: ['There was error communicating with the server'],
        };
      }
    }
  },
  async editTeam({ commit }, { slug, data }) {
    try {
      const response = await api.patch(`teams/${slug}/`, data);
      const newTeam = response.data;
      commit('setTeamById', newTeam);
      return {};
    } catch (error) {
      if (error.response) {
        return error.response;
      } else {
        return {
          non_field_errors: ['There was error communicating with the server'],
        };
      }
    }
  },
};

const getters = {
  listTeams: (state, getters, rootState) => {
    return _.values(state.all).map((t) => {
      const tms = _.filter(
        rootState.TeamMembership.all,
        (tm) => tm.team_id === t.id,
      );
      const usernames = tms.map((tm) => tm.user);
      const members = _.uniq(
        _.filter(rootState.User.all, (u) => usernames.includes(u.username)),
      );
      return {
        ...t,
        members,
      };
    });
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
    const tms = _.filter(
      rootState.TeamMembership.all,
      (tm) => tm.team_id === team.id,
    );
    const usernames = tms.map((tm) => tm.user);
    const members = _.uniq(
      _.filter(rootState.User.all, (u) => usernames.includes(u.username)),
    );
    return {
      ...team,
      games,
      members,
    };
  },
  teamById: (state) => (id) => {
    return state.all[id];
  },
};

const Team = {
  state,
  mutations,
  actions,
  getters,
};

export default Team;
