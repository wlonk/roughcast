import _ from 'lodash';
import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setPublishers(state, publishers) {
    state.all = publishers;
  },
  getPublisherById(state, publisher) {
    state.all = {
      ...state.all,
      [publisher.id]: publisher,
    };
  },
};

const actions = {
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
};

const getters = {
  hydratedPublisher: (state, getters, rootState) => (slug) => {
    const publisher = _.find(
      state.all,
      (p) => p.slug === slug,
    );
    const games = _.filter(
      rootState.Game.all,
      (g) => g.publisher === publisher.slug,
    );
    return {
      ...publisher,
      games,
    };
  },
};

const Publisher = {
  state,
  mutations,
  actions,
  getters,
};

export default Publisher;
