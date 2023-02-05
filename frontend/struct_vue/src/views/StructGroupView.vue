<template>
  <div class="struct">

        <div v-for="group in groups" v-bind:key="group.id" >
            <recursive_tree
                @Delete="OnDelete"
                @ShowEditTree="OnShowEditTree"
                :group="group"
                :depth="0"
                 >
            </recursive_tree>
        </div>





  </div>
 <router-view />
</template>




<script>

import axios from 'axios'
import recursive_tree from '../components/recursive_tree.vue'

import { defineComponent } from "vue";

export default defineComponent({
  name: 'StructMenu',

  data() {
    return {
      groups: [],
      modalOptions: [
            {mode: 'title', id: 'По названию'},
            {mode: 'body', id: 'По содержимому'},
        ]
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

    },
    OnDelete(id){
     axios.get('api/delete', {params: {groupId: id}})
    },
    OnShowEditTree(mode,group) {
     axios.get('OnShowModal'+group.slug, {params: {groupId: group.id}})
    },
  }
})
</script>

