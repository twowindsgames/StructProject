<template>
  <div class="recursive_tree" >

    <context_menu
            @ReadyDelete="onReadyDelete()" @Delete="OnDelete" @ShowEditTree="OnShowEditTree"
            :group="group"
            :readyToDelete="checkToDelete()">
        </context_menu>

    <q-item class="struct-item" clickable  :to="'/structure' + group.get_absolute_url"
                      :style="indent"

                      :hide-expand-icon="group.is_leaf_node">
          {{group.slug}}
          <div v-if="checkToDelete()"> toDelete </div>

    <div name="arrow"   v-if="!group.is_leaf_node">

           <q-icon v-if="isShow" name="arrow_drop_down" @click="toggleChildren">  </q-icon>
           <q-icon v-else name="arrow_right" @click="toggleChildren">  </q-icon>

          </div>

      </q-item>




    <div v-if="isShow" transition-show="fade"  >
      <recursive_tree
      v-for="group in group.children"
      v-bind:key="group.id"
        @Delete="OnDelete" @ShowEditTree="OnShowEditTree"
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
        return { transform: `translate(${this.depth * 8}%)` }
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
<style lang="sass" scoped>
.struct-item
  margin: 0px 0px
</style>