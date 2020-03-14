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
  },

  getters: {
    firstChartData: state => state.firstChartData,
  },

  actions: {

    fireActions: ({ dispatch }, { payload }) => {
      console.log(payload)
      dispatch('fetchFirstChartData', { payload });
    },

    fetchFirstChartData: ({ commit }, { payload}) => {
      const path = 'http://localhost:5000/routeOne';
      axios.post(path, payload)
      .then((res) => {
        res.data.sort((a, b) => b - a);
        console.log(res.data)
        commit('setFirstChartData', res.data);
      });
    },

  },

  mutations: {

    setFirstChartData(state, data) {
      state.firstChartData = data;
    },

  },

})
