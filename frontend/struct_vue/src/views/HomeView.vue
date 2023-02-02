<template>
  <div class="home">

<div class="columns  ">
      <div class="column is-one-quarter  has-background-primary-dark has-text-centered  ">

        <div v-for="group in groups" v-bind:key="group.id" >

                <recursive_tree :slug="group.slug" :children="group.children" :depth="0"></recursive_tree>
            </div>
      </div>
      <div class=" column is-three-quarters has-background-info-dark has-text-centered ">
            <div v-for="group in groups" v-bind:key="group.id" >

                <recursive_tree :slug="group.slug" :children="group.children" :depth="0"></recursive_tree>
            </div>
      </div>
 </div>


  </div>
</template>

<script>
import axios from 'axios'
import recursive_tree from '../components/recursive_tree.vue'
export default {
  name: 'HomeView',
  data() {
    return {
      groups: []
    }
  },
  mounted() {
    this.getLatestProducts()

  },
  components:{
    recursive_tree
  }
  ,
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

    },
    winter: function () {

      axios
          .get('/api/v1/winter-products/', {params: {category: 2}})
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