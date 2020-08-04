import Vue from 'vue';

const AttachedFile = {
  state: () => ({
    all: {},
  }),
  mutations: {
    setAttachedFiles(state, attached_files) {
      state.all = attached_files;
    },
    getAttachedFileById(state, attached_file) {
      state.all = {
        ...state.all,
        [attached_file.id]: attached_file,
      }
    },
  },
  actions: {
    async retrieveAttachedFiles({ commit }) {
      const resp = await fetch('/api/attached_file/');
      if (resp.ok) {
        const attached_files = await resp.json();
        const attached_filesObj = attached_files.reduce((acc, curr) => {
          acc[curr.id] = curr;
          return acc;
        }, {});
        commit('setAttachedFiles', attached_filesObj);
      } else {
        // TODO display error
      }
    },
    async getAttachedFileById({ commit, state }, id) {
      if (state.all[id] !== undefined) {
        return;
      }
      const response = await fetch(`/api/attached_file/${id}/`);
      if (response.ok) {
        const attached_file = await response.json();
        commit('getAttachedFileById', attached_file);
      } else {
        // TODO: Display lookup error toast?
      }
    },
    async createNewAttachedFile({ commit }, data) {
      const formData = new FormData();
      formData.append("version_id", data.version_id);
      formData.append("attached_file", data.attached_file);
      const csrftoken = Vue.$cookies.get('csrftoken');
      const response = await fetch('/api/attached_file/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrftoken,
        },
        body: formData,
      });
      if (response.ok) {
        const newAttachedFile = await response.json();
        commit('getAttachedFileById', newAttachedFile);
      } else {
        // TODO: Display lookup error toast?
      }
    },
  },
};

export default AttachedFile;
