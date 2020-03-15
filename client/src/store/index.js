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
    successfulByCategory: [],
  },

  getters: {
    firstChartData: state => state.firstChartData,
    successfulByCategory: state => state.successfulByCategory,
  },

  actions: {

    fireActions: ({ dispatch }, { payload }) => {
      console.log(payload)
      dispatch('fetchFirstChartData', { payload });
      dispatch('fetchSuccessfulByCategory', { payload });
    },

    fetchFirstChartData: ({ commit }, { payload}) => {
      const path = 'http://localhost:5000/routeOne';
      axios.post(path, payload)
      .then((res) => {
        res.data.sort((a, b) => b - a);
        commit('setFirstChartData', res.data);
      });
    },

    fetchSuccessfulByCategory: ({ commit }, { payload}) => {
      const path = 'http://localhost:5000/SuccessfulByCategory';
      axios.post(path, payload)
      .then((res) => {
        console.log(res.data)
        res.data.sort((a, b) => b - a);
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
