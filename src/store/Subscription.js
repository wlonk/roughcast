import _ from 'lodash';
import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setSubscriptions(state, subscriptions) {
    state.all = subscriptions;
  },
  setSubscriptionById(state, subscription) {
    state.all = {
      ...state.all,
      [subscription.id]: subscription,
    };
  },
  deleteSubscriptionById(state, subscriptionId) {
    state.all = _.omit(state.all, subscriptionId);
  },
};

const actions = {
  async retrieveSubscriptions({ commit }) {
    const resp = await api.get('subscriptions/');
    const subscriptions = resp.data;
    const subscriptionsObj = subscriptions.reduce((acc, curr) => {
      acc[curr.id] = curr;
      return acc;
    }, {});
    commit('setSubscriptions', subscriptionsObj);
  },
  async subscribe({ commit }, instance) {
    const resp = await api.post('subscriptions/', { instance });
    const subscription = resp.data;
    commit('setSubscriptionById', subscription);
  },
  async unsubscribe({ commit }, subscriptionId) {
    const resp = await api.delete(`subscriptions/${subscriptionId}/`);
    if (resp.ok) {
      commit('deleteSubscriptionById', subscriptionId);
    }
  },
};

const getters = {
  listSubscriptions: (state) => {
    return _.values(state.all);
  },
  getSubscriptionForInstance: (state) => (instance) => {
    return _.find(state.all, (s) => s.instance === instance);
  },
};

const Subscription = {
  state,
  mutations,
  actions,
  getters,
};

export default Subscription;
