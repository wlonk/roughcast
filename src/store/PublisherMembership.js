import api from '../api';

const PublisherMembership = {
  state: () => ({
    all: {},
  }),
  mutations: {
    setPublisherMemberships(state, publisherMemberships) {
      state.all = publisherMemberships;
    },
  },
  actions: {
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
  },
};

export default PublisherMembership;
