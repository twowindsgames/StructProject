<template>
  <div class="struct">

        <div v-for="group in groups" v-bind:key="group.id" >
            <recursive_tree
                @Delete="OnDelete"
                @ShowModal="OnShowModal"
                :slug="group.slug"
                :children="group.children"
                :depth="0"
                :group-id="group.id"
                :get_absolute_url="group.get_absolute_url"
                 >
            </recursive_tree>
        </div>



  </div>
 <router-view />
</template>




<script>

import axios from 'axios'
import recursive_tree from '../components/recursive_tree.vue'
import modal_menu from '../components/modal_menu.vue'
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
    modal_menu,

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
    OnShowModal(mode,id) {
     axios.get('OnShowModal'+mode, {params: {groupId: id}})
    },
  }
})
</script>

