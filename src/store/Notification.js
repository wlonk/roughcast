import api from '../api';

const state = () => ({
  all: {},
});

const mutations = {
  setNotifications(state, notifications) {
    state.all = notifications;
  },
  setNotificationById(state, notification) {
    state.all = {
      ...state.all,
      [notification.id]: notification,
    };
  },
};

const actions = {
  async retrieveNotifications({ commit }) {
    try {
      const resp = await api.get('notifications/');
      const notificationsObj = resp.data.reduce((acc, curr) => {
        acc[curr.id] = curr;
        return acc;
      }, {});
      commit('setNotifications', notificationsObj);
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
  async markRead({ commit }, notificationId) {
    try {
      const resp = await api.patch(`notifications/${notificationId}/`, {
        seen_at: new Date(),
      });
      commit('setNotificationById', resp.data);
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
  allNotifications: state => {
    return state.all;
  },
};

const Notification = {
  state,
  mutations,
  actions,
  getters,
};

export default Notification;
