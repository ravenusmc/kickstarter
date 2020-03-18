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
    failuresByCategory: [
      ["Category", "Count"],
      ["Food", 6555],
      ["Music", 5502],
      ["Film & Video", 5127],
      ["Fashion", 4996],
      ["Technology", 3832],
      ["Art", 3544],
      ["Photography", 3260],
      ["Publishing", 2941],
      ["Crafts", 2594],
      ["Theater", 2215],
      ["Comics", 1988],
      ["Design", 1861],
      ["Games", 1606],
      ["Journalism", 1000],
      ["Dance", 640]
    ],
  },

  getters: {
    firstChartData: state => state.firstChartData,
    successfulByCategory: state => state.successfulByCategory,
    failuresByCategory: state => state.failuresByCategory,
  },

  actions: {

    fireActions: ({ dispatch }, { payload }) => {
      dispatch('fetchFirstChartData', { payload });
      dispatch('fetchSuccessfulByCategory', { payload });
      dispatch('fetchFailuresByCategory', { payload });
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
        commit('setSuccessfulByCategory', res.data);
      });
    },

    fetchFailuresByCategory: ({ commit }, { payload}) => {
      const path = 'http://localhost:5000/FailuresByCategory';
      axios.post(path, payload)
      .then((res) => {
        res.data.sort((a, b) => b[1] - a[1]);
        console.log(res.data)
        commit('setFailuresByCategory', res.data);
      });
    },

  },

  mutations: {

    setFirstChartData(state, data) {
      state.firstChartData = data;
    },

    setSuccessfulByCategory(state, data) {
      state.successfulByCategory = data;
    },

    setFailuresByCategory(state, data) {
      state.failuresByCategory = data;
    }


  },

})
