<template>
  <q-layout view="hHh LpR fFf" >

  <q-header elevated  class="bg-indigo-4 text-white ">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar>
            <q-icon name="groups" size="2em"/>
          </q-avatar>
          Структура
        </q-toolbar-title>
      </q-toolbar>
    </q-header>


   <q-drawer show-if-above style="height: 100%" v-model="leftDrawerOpen" behavior="desktop" side="left" bordered>
     <q-list style="height: 100%" >
          <router-view name="struct"/>
      </q-list>
   </q-drawer>

    <q-page-container>
       <section class="section">
         <q-page><router-view name="info" :key="$route.path" /></q-page>
      </section>
   </q-page-container>



    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <div>Тестовое задание</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>


import { ref } from 'vue'





export default {

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },

}
</script>



