import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setTeamMemberships(state, teamMemberships) {
    state.all = teamMemberships;
  },
};

const actions = {
  async retrieveTeamMemberships({ commit }) {
    const resp = await api.get('teammemberships/');
    if (resp.ok) {
      const teamMemberships = resp.data;
      const teamMembershipsObj = teamMemberships.reduce((acc, curr) => {
        acc[curr.id] = curr;
        return acc;
      }, {});
      commit('setTeamMemberships', teamMembershipsObj);
    } else {
      // TODO display error
    }
  },
};

const getters = {};

const TeamMembership = {
  state,
  mutations,
  actions,
  getters,
};

export default TeamMembership;
