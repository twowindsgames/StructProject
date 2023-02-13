<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-indigo-4 text-white">
      <q-toolbar class="q-ma-xs">
        <q-btn dense round icon="menu" @click="toggleLeftDrawer"/>
        <q-avatar class="q-ml-sm">
          <q-icon name="groups" size="2em"/>
        </q-avatar>
        <q-toolbar-title>
          <strong>Структура</strong>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above style="height: 100%; width: 360px; max-width: 350px; overflow-x: hidden " class="bg-indigo-1" v-model="leftDrawerOpen" :width="350"
              behavior="desktop" side="left" bordered>
      <router-view name="struct"/>
    </q-drawer>

    <q-page-container>
      <section class="section">
        <q-page>
          <router-view name="info" :key="$route.path"/>
        </q-page>
      </section>
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <i>Тестовое задание</i>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>


<script>
import {ref} from 'vue'

export default {
  setup() {
    const leftDrawerOpen = ref(false)
    return {
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },
}
</script>



