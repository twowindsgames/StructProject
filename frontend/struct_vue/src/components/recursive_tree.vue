<template>
  <div class="recursive_tree" >

    <div :style="indent"  @click="toggleChildren">

      <router-link :to="'/structure' + get_absolute_url" class="button is-dark">{{ slug }}
        <context_menu @ReadyDelete="onReadyDelete()" @Delete="OnDelete" :group_id="groupId" :readyToDelete="checkToDelete()"></context_menu>
      </router-link>

      <div v-if="checkToDelete()"> toDelete </div>
    </div>

   <div v-if="isShow">
      <recursive_tree
      v-for="group in children"
      v-bind:key="group.id"
        @Delete="OnDelete"
        :slug="group.slug"
        :children="group.children"
        :depth="depth + 1"
        :group-id = "group.id"
        :get_absolute_url = "group.get_absolute_url"
        :isParentReadyToDelete="checkToDelete()">
      </recursive_tree>
   </div>

  </div>
</template>
<script>
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

    onReadyDelete() {
      this.isReadyToDelete = true
    },
        OnDelete(id) {
        this.$emit('Delete', id)

    },

    checkToDelete(){
        return (this.isReadyToDelete || this.isParentReadyToDelete)
                   }

 },
  }
</script>