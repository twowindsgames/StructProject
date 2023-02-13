<template>
  <div  class="struct  " style="height: 100%; ">
    <div v-for="group in groups" v-bind:key="group.id" >
      <recursive-tree
          @readyDelete="onShowDeleteTree"
          @showEditTree="onShowEditTree"
          :path="path"
          :group="group"
          :depth="0">
      </recursive-tree>
    </div>

    <modal-menu v-model="editTreeModalView" :title="modalOptions.title">
      <post-form @dataPost="onDataPost" :mode="modalOptions.mode" :current_data=modalOptions.group></post-form>
    </modal-menu>

    <modal-menu v-model="deleteTreeModalView" :title="modalOptions.title">
      <delete-form @delete="onDelete" :mode="modalOptions.mode" :group=modalOptions.group></delete-form>
    </modal-menu>

    <q-page-sticky position="bottom-right" style="margin-right: 30px">
      <q-btn @click="onShowEditTree('add node',null)" round color="indigo" icon="add"></q-btn>
    </q-page-sticky>

  </div>
</template>
<script>

import axios from 'axios'
import RecursiveTree from '../components/RecursiveTree.vue'
import ModalMenu from '../components/ModalMenu.vue'
import PostForm from '../components/PostForm.vue'
import DeleteForm from '../components/DeleteForm.vue'
import NotifyManager from "../components/NotifyManager";


export default {
  name: 'StructMenu',

  data() {
    return {
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
  components: {
    PostForm,
    RecursiveTree,
    ModalMenu,
    DeleteForm,
  },
  methods: {
    getAllGroups() {
      this.path = this.$route.params.hierarchy.split('/')
      axios
          .get('/api/group/all/')
          .then(response => {
            this.groups = response.data

          })
          .catch(error => {
            NotifyManager.methods.pushErrorNotify(error)
          })
    },
    onShowEditTree(mode, group) {
      this.modalOptions.mode = mode
      this.modalOptions.group = group
      if (mode === "edit node") this.modalOptions.title = "Изменить информацию о подразделении"
      else this.modalOptions.title = "Добавить подразделение"
      this.editTreeModalView = true
    },

    onShowDeleteTree(group) {
      this.modalOptions.mode = "delete node"
      this.modalOptions.group = group
      this.modalOptions.title = "Удалить подразделение"
      this.deleteTreeModalView = true
    },
    onDelete(id) {
      axios.delete('api/group/', {params: {group_id: id},}).then(response => {
        NotifyManager.methods.pushResponceNotify(response)
        this.getAllGroups()
      })
          .catch(error => {
            NotifyManager.methods.pushErrorNotify(error)
          })
    },
    onDataPost(postData) {

      let request
      if (this.modalOptions.mode === "add node") request = axios.post('api/group/', postData)
      if (this.modalOptions.mode === "edit node") request = axios.put('api/group/', postData)
      request.then(response => {
        NotifyManager.methods.pushResponceNotify(response)
        this.getAllGroups()
      })
          .catch(error => {
            NotifyManager.methods.pushPostErrorNotify(error)
          })
    },
  }
}
</script>

