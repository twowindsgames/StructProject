<template>

  <q-scroll-area  class="struct  " style="height: 100%; ">
    <q-list  v-for="group in groups" v-bind:key="group.id" >
      <recursive_tree
          @ReadyDelete="OnShowDeleteTree"
          @ShowEditTree="OnShowEditTree"
          :path="path"
          :group="group"
          :depth="0">
      </recursive_tree>
    </q-list>



      <modal_menu v-model="editTreeModalView" :title="modalOptions.title">
        <post_form @DataPost="OnDataPost" :mode="modalOptions.mode" :current_data=modalOptions.group ></post_form>
      </modal_menu>

       <modal_menu v-model="deleteTreeModalView" :title="modalOptions.title">
        <delete_form @Delete="OnDelete" :mode="modalOptions.mode" :group=modalOptions.group ></delete_form>
      </modal_menu>




        <q-page-sticky   position="bottom-right" style="margin-right: 30px" >
                <q-btn @click="OnShowEditTree('add node',null)" round color="indigo" icon="add" ></q-btn>
        </q-page-sticky>

  </q-scroll-area>


</template>

<script>

import axios from 'axios'
import recursive_tree from '../components/recursive_tree.vue'
import modal_menu from '../components/modal_menu.vue'

import post_form from '../components/post_form.vue'
import delete_form from '../components/delete_form.vue'
import notify_manager from "@/components/notify_manager";




export default {
  name: 'StructMenu',

  data() {
    return {
      can_build: false,
      groups: [],
      modalOptions: {mode: 'режим', title: 'заголовок', group: Object},
      editTreeModalView: false,
      deleteTreeModalView: false,
      path: []
    }
  },



  mounted() {


    this.getAllGroups()

  },
  components:{

    post_form,
    recursive_tree,
    modal_menu,
    delete_form,



  },

  methods: {

    getAllGroups() {
       this.path  =  this.$route.params.tree_hierarchy.split('/')

      axios
          .get('/api/group/all/')
          .then(response => {
            this.groups = response.data

          })
          .catch(error => {
            notify_manager.methods.PushErrorNotify(error)
          })
    },
    OnShowEditTree(mode,group) {
    this.modalOptions.mode = mode
    this.modalOptions.group = group
    if (mode==="edit node")  this.modalOptions.title = "Изменить информацию о подразделении"
    else  this.modalOptions.title = "Добавить подразделение"
    this.editTreeModalView=true
    },

    OnShowDeleteTree(group) {
    this.modalOptions.mode = "delete node"
    this.modalOptions.group = group
    this.modalOptions.title = "Удалить подразделение"
    this.deleteTreeModalView=true
    },
    OnDelete(id){
    axios.delete('api/group/', {params: {group_id: id},}).then(response =>
    {
        notify_manager.methods.PushResponceNotify(response)
        this.getAllGroups()})
        .catch(error => {notify_manager.methods.PushErrorNotify(error)})
    },
    OnDataPost(post_data){

     let request
     if (this.modalOptions.mode==="add node")  request = axios.post('api/group/', post_data)
     if (this.modalOptions.mode==="edit node") request = axios.put('api/group/', post_data)
     request.then(response => {
        notify_manager.methods.PushResponceNotify(response)
        this.getAllGroups()})
        .catch(error => {notify_manager.methods.PushPostErrorNotify(error)})
    },
  }
}
</script>

