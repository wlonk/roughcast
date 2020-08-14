import api from '../api';

const Publisher = {
  state: () => ({
    all: {},
  }),
  mutations: {
    setPublishers(state, publishers) {
      state.all = publishers;
    },
    getPublisherById(state, publisher) {
      state.all = {
        ...state.all,
        [publisher.id]: publisher,
      };
    },
  },
  actions: {
    async retrievePublishers({ commit }) {
      const resp = await api.get('/publisher/');
      if (resp.ok) {
        const publishers = resp.data;
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
      const response = await api.get(`/publisher/${id}/`);
      if (response.ok) {
        const publisher = response.data;
        commit('getPublisherById', publisher);
      } else {
        // TODO: Display lookup error toast?
      }
    },
    async createNewPublisher({ commit }, data) {
      const response = await api.post('/publisher/', data);
      if (response.ok) {
        const newPublisher = response.data;
        commit('getPublisherById', newPublisher);
        commit('retrievePublisherMemberships');
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default Publisher;
