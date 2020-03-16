import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    firstChartData: [
      ["State", "Count"],
      ["failed", 312],
      ["successful", 245],
      ["canceled", 62],
    ],
    successfulByCategory: [
      ["Category", "Count"],
      ["Music", 5715],
      ["Theater", 4286],
      ["Food", 3133],
      ["Art", 2870],
      ["Film & Video", 2831],
      ["Comics", 2302],
      ["Fashion", 2086],
      ["Photography", 1812],
      ["Dance", 1502],
      ["Publishing", 1375],
      ["Design", 1157],
      ["Technology", 1113],
      ["Crafts", 956],
      ["Games", 643],
      ["Journalism", 446],
    ],
  },

  getters: {
    firstChartData: state => state.firstChartData,
    successfulByCategory: state => state.successfulByCategory,
  },

  actions: {

    fireActions: ({ dispatch }, { payload }) => {
      dispatch('fetchFirstChartData', { payload });
      dispatch('fetchSuccessfulByCategory', { payload });
    },

    fetchFirstChartData: ({ commit }, { payload}) => {
      const path = 'http://localhost:5000/routeOne';
      axios.post(path, payload)
      .then((res) => {
        res.data.sort((a, b) => b[1] - a[1]);
        commit('setFirstChartData', res.data);
      });
    },

    fetchSuccessfulByCategory: ({ commit }, { payload}) => {
      const path = 'http://localhost:5000/SuccessfulByCategory';
      axios.post(path, payload)
      .then((res) => {
        res.data.sort((a, b) => b[1] - a[1]);
        console.log(res.data)
        commit('setSuccessfulByCategory', res.data);
      });
    },

  },

  mutations: {

    setFirstChartData(state, data) {
      state.firstChartData = data;
    },

    setSuccessfulByCategory(state, data) {
      state.successfulByCategory = data;
    }


  },

})
