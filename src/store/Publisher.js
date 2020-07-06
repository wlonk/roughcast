const Publisher = {
  state: () => ({
    all: {},
  }),
  mutations: {
    setPublishers(state, publishers) {
      state.all = publishers;
    },
    getPublisherById(state, publisher) {
      state.all[publisher.id] = publisher;
    },
  },
  actions: {
    async retrievePublishers({ commit }) {
      const resp = await fetch('/api/publisher/');
      if (resp.ok) {
        const publishers = await resp.json();
        const publishersObj = publishers.reduce((acc, curr) => {
          acc[curr.id] = curr;
          return acc;
        }, {});
        commit('setPublishers', publishersObj);
      } else {
        // TODO display error
      }
    },
    async getPublisherById({ commit, state }, id) {
      if (state.all[id] !== undefined) {
        return;
      }
      const response = await fetch(`/api/publisher/${id}/`);
      if (response.ok) {
        const publisher = await response.json();
        commit('getPublisherById', publisher);
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default Publisher;
