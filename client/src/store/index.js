import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({

  state: {
    firstChartData: [],
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
