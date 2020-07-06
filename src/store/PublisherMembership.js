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
      const resp = await fetch('/api/publishermembership/');
      if (resp.ok) {
        const publisherMemberships = await resp.json();
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
