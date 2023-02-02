
<template>
  <q-layout view="hhh lpr fff">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          Title
        </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>
      <div>


        <div v-for="group in groups" v-bind:key="group.id" >
                <recursive_tree :slug="group.slug" :children="group.children" :depth="0"></recursive_tree>
        </div>
      </div>

      <!-- drawer content -->
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          <div>Title</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>





<script>
import axios from 'axios'
import { ref } from 'vue'
import recursive_tree from '../components/recursive_tree.vue'

export default {
  name: 'HomeView',
  setup () {
    const leftDrawerOpen = ref(false)

    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },
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