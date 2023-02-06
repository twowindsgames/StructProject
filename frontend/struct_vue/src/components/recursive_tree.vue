<template>
  <div class="recursive_tree" >


<div v-if="checkToDelete()"> toDelete </div>










   <q-expansion-item :to="'/structure' + group.get_absolute_url" :label="group.slug"  :hide-expand-icon="group.is_leaf_node"  @click="toggleChildren">
      <context_menu
            @ReadyDelete="onReadyDelete()" @Delete="OnDelete" @ShowEditTree="OnShowEditTree"
            :group="group"
            :readyToDelete="checkToDelete()">
      </context_menu>
      <recursive_tree
      v-for="g in group.children"
      v-bind:key="g.id"
        @Delete="OnDelete" @ShowEditTree="OnShowEditTree"
        :group="g"
        :depth="depth + 1"
        :isParentReadyToDelete="checkToDelete()"
        :root="rootListener">

      </recursive_tree>
   </q-expansion-item>


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
        return { transform: `translate(${this.depth * 10}px)` }
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