import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setPublisherMemberships(state, publisherMemberships) {
    state.all = publisherMemberships;
  },
};

const actions = {
  async retrievePublisherMemberships({ commit }) {
    const resp = await api.get('/publishermembership/');
    if (resp.ok) {
      const publisherMemberships = resp.data;
      const publisherMembershipsObj = publisherMemberships.reduce(
        (acc, curr) => {
          acc[curr.id] = curr;
          return acc;
        },
        {},
      );
      commit('setPublisherMemberships', publisherMembershipsObj);
    } else {
      // TODO display error
    }
  },
};

const getters = {};

const PublisherMembership = {
  state,
  mutations,
  actions,
  getters,
};

export default PublisherMembership;
