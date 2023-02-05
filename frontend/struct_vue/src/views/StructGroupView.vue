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
<modal_menu v-model="editTreeModalView" :title="modalOptions.title"> <post_form @DataPost="OnDataPost"></post_form>  </modal_menu>
  </div>
 <router-view />
</template>




<script>

import axios from 'axios'
import recursive_tree from '../components/recursive_tree.vue'
import modal_menu from '../components/modal_menu.vue'
import { defineComponent } from "vue";
import post_form from '../components/post_form.vue'

export default defineComponent({
  name: 'StructMenu',

  data() {
    return {
      groups: [],
      modalOptions: {mode: 'режим', title: 'заголовок', group: null},
      editTreeModalView: false


    }
  },
  mounted() {
    this.getLatestProducts()

  },
  components:{
    post_form,
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
    OnDataPost(post_data){
     if (this.modalOptions.mode==="add")  axios.get('api/postadd', {params: {data: post_data.title}})
     if (this.modalOptions.mode==="edit")  axios.get('api/postedit', {params: {data: post_data.title}})
    },
    OnShowEditTree(mode,group) {
    this.modalOptions.mode = mode
    this.modalOptions.group = group
    if (mode==="edit")  this.modalOptions.title = "Изменить информацию о подразделении"
    else  this.modalOptions.title = "Добавить подчиненное подрзделение"
    this.editTreeModalView=true
    },
  }
})
</script>

