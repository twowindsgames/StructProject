<template>
  <div class="struct">


        <div v-for="group in groups" v-bind:key="group.id" >
            <recursive_tree  :slug="group.slug" :children="group.children" :depth="0"  :group-id="group.id" :get_absolute_url="group.get_absolute_url"></recursive_tree>
        </div>




  </div>
 <router-view />
</template>




<script>

import axios from 'axios'

import recursive_tree from '../components/recursive_tree.vue'


export default {
  name: 'StructMenu',

  data() {
    return {
      groups: []
    }
  },
  mounted() {
    this.getLatestProducts()

  },
  components:{
    recursive_tree,

  },
  methods: {

    getLatestProducts() {

      axios
          .get('/api/group/all/')
          .then(response => {
            this.groups = response.data
          })
          .catch(error => {
            console.log(error)
          })

    }
  }
}
</script>

