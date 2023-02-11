import { createStore } from 'vuex'

export default createStore({
  state: {
    path: []
  },
  getters: {
     get_group_id(state){
            return state.group_id
        }
  },
  mutations: {
      change_group_id(state, tree_hierarchy){
            state.path = tree_hierarchy
        }
  },
  actions: {
       change_group_id (context, tree_hierarchy) {
      context.commit('change_group_id',tree_hierarchy)
    },

  },
  modules: {
  }
})
