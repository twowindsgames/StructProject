<template>
  <div class="recursive_tree" >
    <div :style="indent"  @click="toggleChildren">
      <router-link :to="'/structure' + get_absolute_url" class="button is-dark">{{ slug }}
        <context_menu @clickToDelete="onClickToDelete()" :group_id="groupId" :readyToDelete="checkToDelete()"></context_menu></router-link>
      <div v-if="checkToDelete()"> toDelete </div>
    </div>

   <div v-if="isShow">
      <recursive_tree
      v-for="group in children"

      v-bind:key="group.id"
      :slug="group.slug"
      :children="group.children"
      :depth="depth + 1"
      :group-id = "group.id"
      :get_absolute_url = "group.get_absolute_url"
      :isParentReadyToDelete="checkToDelete()"

      >

   </recursive_tree>
   </div>
  </div>
</template>
<script>
  import axios from "axios";
  import context_menu from './context_menu.vue'
  export default {
    props: [ 'slug', 'children', 'depth', 'groupId', 'get_absolute_url', 'clickToDelete', 'isParentReadyToDelete' ],
    name: 'recursive_tree',
    data() {
      return {
        isShow: false,
        isReadyToDelete: false
      }
    },
    computed: {
      indent() {
        return { transform: `translate(${this.depth * 50}px)` }
      }
    },
    components:{
    context_menu,
  },
     methods: {
      toggleChildren() {
        this.isShow = !this.isShow;
      },
       getUnitsByGroup: function (id) {

      axios
          .get('api/group/units', {params: {groupId: id}})
          .then(response => {
            this.groups = response.data
          })
          .catch(error => {
            console.log(error)
          })

    },

    onClickToDelete() {
      this.isReadyToDelete = true
    },

    checkToDelete(){
        return (this.isReadyToDelete || this.isParentReadyToDelete)
                   }

 },
  }
</script>