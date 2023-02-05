<template>
  <div class="recursive_tree" >

    <div :style="indent"  @click="toggleChildren">

      <router-link :to="'/structure' + group.get_absolute_url" class="button is-dark">{{ group.slug }}
        <context_menu @ReadyDelete="onReadyDelete()" @Delete="OnDelete" @ShowEditTree="OnShowEditTree" :group="group" :readyToDelete="checkToDelete()"></context_menu>
      </router-link>

      <div v-if="checkToDelete()"> toDelete </div>
    </div>

   <div v-if="isShow">
      <recursive_tree
      v-for="group in group.children"
      v-bind:key="group.id"
        @Delete="OnDelete"
        @ShowEditTree="OnShowEditTree"
        :group="group"
        :depth="depth + 1"
        :isParentReadyToDelete="checkToDelete()"
        :root="rootListener">
      </recursive_tree>
   </div>

  </div>
</template>
<script>
  import context_menu from './context_menu.vue'

  export default {
    props: ['group',  'depth', 'clickToDelete', 'isParentReadyToDelete', 'root' ],
    name: 'recursive_tree',
    data() {
      return {
        isShow: false,
        isReadyToDelete: false,
        rootListener: null,

    }
    },
    mounted() {
      if (this.root == null){
        this.rootListener = this
      }
      else {
         this.rootListener = this.root
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
    OnDelete() {
       this.rootListener.$emit('Delete', this.group.id)
    },
    OnShowEditTree(mode) {
       this.rootListener.$emit('ShowEditTree', mode, this.group)
    },

    checkToDelete(){
        return (this.isReadyToDelete || this.isParentReadyToDelete)
                   }

 },
  }
</script>