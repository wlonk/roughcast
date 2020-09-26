import _ from 'lodash';
import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setInvites(state, invites) {
    state.all = invites;
  },
  setInviteById(state, invite) {
    state.all = {
      ...state.all,
      [invite.id]: invite,
    };
  },
  deleteInviteById(state, inviteId) {
    state.all = _.omit(state.all, inviteId);
  },
};

const actions = {
  async retrieveInvites({ commit }) {
    const resp = await api.get('invites/');
    const invites = resp.data.reduce((acc, curr) => {
      acc[curr.id] = curr;
      return acc;
    }, {});
    commit('setInvites', invites);
  },
  async acceptInvite({ commit }, id) {
    try {
      await api.post(`invites/${id}/accept/`);
      commit('retrieveTeams');
      commit('deleteInviteById', id);
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
  async createNewInvite({ commit }, data) {
    try {
      const response = await api.post('invites/', data);
      const newInvite = response.data;
      commit('setInviteById', newInvite);
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
  async deleteInvite({ commit }, id) {
    try {
      await api.delete(`invites/${id}/`);
      commit('deleteInviteById', id);
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
  listInvites: (state) => {
    return _.values(state.all);
  },
  myPendingInvites: (state, getters) => {
    const myTeamIds = _.map(getters.myTeams, (t) => t.id);
    return _.map(
      _.filter(state.all, (i) => !myTeamIds.includes(i.team)),
      (i) => ({ ...i, team: getters.teamById(i.team) }),
    );
  },
  myOfferedInvites: (state, getters) => {
    const myTeamIds = _.map(getters.myTeams, (t) => t.id);
    return _.filter(state.all, (i) => myTeamIds.includes(i.team));
  },
};

const Invite = {
  state,
  mutations,
  actions,
  getters,
};

export default Invite;
