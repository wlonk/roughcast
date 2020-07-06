import Vue from 'vue';

const User = {
  state: () => ({
    current: null,
    loggingIn: false,
    errors: {},
    all: {},
  }),
  mutations: {
    logIn(state, user) {
      state.current = user;
    },
    logOut(state) {
      state.current = null;
    },
    loggingIn(state) {
      state.loggingIn = true;
    },
    doneLoggingIn(state) {
      state.loggingIn = false;
    },
    setErrors(state, errors) {
      state.errors = errors;
    },
    setUsers(state, users) {
      state.all = users;
    },
    getUserById(state, user) {
      state.all[user.id] = user;
    },
  },
  actions: {
    async logIn({ commit }, data) {
      commit('setErrors', {});
      commit('loggingIn');
      const csrftoken = Vue.$cookies.get('csrftoken');
      const response = await fetch('/api/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const user = await response.json();
        commit('logIn', user);
      } else {
        const errors = await response.json();
        console.log(errors);
        commit('setErrors', errors);
        commit('logOut');
      }
      commit('doneLoggingIn');
    },
    async logOut({ commit }) {
      // TODO: Actually clear the cookie, etc.
      const csrftoken = Vue.$cookies.get('csrftoken');
      const response = await fetch('/api/logout/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrftoken,
        },
      });
      if (response.ok) {
        commit('logOut');
      } else {
        const errors = {
          non_field_errors: [
            'There was an error logging out. Please try again in a moment.',
          ],
        };
        commit('setErrors', errors);
      }
    },
    async retrieveUsers({ commit }) {
      const resp = await fetch('/api/user/');
      if (resp.ok) {
        const users = await resp.json();
        const usersObj = users.reduce((acc, curr) => {
          acc[curr.id] = curr;
          return acc;
        }, {});
        commit('setUsers', usersObj);
      } else {
        // TODO display error
      }
    },
    async getUserById({ commit, state }, id) {
      if (state.all[id] !== undefined) {
        return;
      }
      const response = await fetch(`/api/user/${id}/`);
      if (response.ok) {
        const user = await response.json();
        commit('getUserById', user);
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default User;
