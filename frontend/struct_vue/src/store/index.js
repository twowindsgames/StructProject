import { createStore } from 'vuex'

export default createStore({
  state: {
    group_id: 0
  },
  getters: {
     get_group_id(state){
            return state.group_id
        }
  },
  mutations: {
      change_group_id(state, id){
            state.group_id = id
        }
  },
  actions: {
       change_group_id (context, id) {
      context.commit('change_group_id',id)
    },

  },
  modules: {
  }
})
