<template>
  <div class="struct " style="height: 100%">

    <q-list  v-for="group in groups" v-bind:key="group.id" >
      <recursive_tree
          @Delete="OnDelete"
          @ShowEditTree="OnShowEditTree"
          :group="group"
          :depth="0">
      </recursive_tree>
    </q-list>

      <div name="no-node-zone" style="height: 100%" >
          <context_menu :root=true @ShowEditTree="OnShowEditTree"/>
      </div>

      <modal_menu v-model="editTreeModalView" :title="modalOptions.title">
        <post_form @DataPost="OnDataPost" :mode="modalOptions.mode" :current_data=modalOptions.group ></post_form>
      </modal_menu>

  </div>


</template>

<script>

import axios from 'axios'
import recursive_tree from '../components/recursive_tree.vue'
import modal_menu from '../components/modal_menu.vue'

import post_form from '../components/post_form.vue'
import context_menu from '../components/context_menu.vue'

export default {
  name: 'StructMenu',
  data() {
    return {
      groups: [],
      modalOptions: {mode: 'режим', title: 'заголовок', group: Object},
      editTreeModalView: false
    }
  },
  mounted() {
    this.GetAllGroups()

  },
  components:{
    post_form,
    recursive_tree,
    modal_menu,
    context_menu,


  },
  methods: {

    getAllGroups() {
      axios
          .get('/api/group/all/')
          .then(response => {
            this.groups = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    OnShowEditTree(mode,group) {
      this.modalOptions.mode = mode
    this.modalOptions.group = group
    if (mode==="edit")  this.modalOptions.title = "Изменить информацию о подразделении"
    else  this.modalOptions.title = "Добавить подразделение"
    this.editTreeModalView=true
    },
        OnDelete(id){
     axios.delete('api/group/', {params: {group_id: id},}).then(response => {
        this.getLatestProducts()
              console.log(response)})
                .catch(error => {console.log(error)})
    },
    OnDataPost(post_data){

     let request
     if (this.modalOptions.mode==="add node")  request = axios.post('api/group/', post_data)
     if (this.modalOptions.mode==="edit node") request = axios.put('api/group/', post_data)
     request.then(response => {
        this.getLatestProducts()
              console.log(response)})
                .catch(error => {console.log(error)})
    },
  }
}
</script>

