<template>
  <div>
       <context_menu
            @ReadyDelete="onReadyDelete()" @Delete="OnDelete" @ShowEditTree="OnShowEditTree"
            :group="group"
            :readyToDelete="checkToDelete()"
            :root=false />


        <q-item :class="[checkToDelete() ? 'bg-red-2 ' :  '']"
                :to="'/structure' + group.get_absolute_url"
                :inset-level="depth"
                :hide-expand-icon="group.is_leaf_node"
                clickable>

                        <div name="arrow" class="q-pa-none q-ma-none div1"  v-if="!group.is_leaf_node">
                           <q-icon v-if="isShow" name="arrow_drop_down"  size="2em" @click="toggleChildren">  </q-icon>
                           <q-icon v-else name="arrow_right" size="2em" @click="toggleChildren">  </q-icon>
                        </div>
                        <div class="q-pa-none  q-ma-none div1 ">
                          <em style="flex-wrap: wrap"> {{group.full_title}}  </em>
                          <i v-if="checkToDelete()"> (подтвердите)</i>
                        </div>




        </q-item>

        <div  v-show="isShow" transition-show="fade"  >
          <recursive_tree
          v-for="group in group.children"
          v-bind:key="group.id"
            @Delete="OnDelete" @ShowEditTree="OnShowEditTree" @OpenChildren="OnOpenChildren"
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
        canBuild: false,
        isReadyToDelete: false,
        rootListener: null,
        current_group_id: this.$store.getters.get_group_id
    }
    },




    mounted() {

      if (this.root == null){
        this.rootListener = this
      }
      else {
         this.rootListener = this.root
      }
       if (this.$store.getters.get_group_id==this.group.id){
            this.$emit('OpenChildren')
       }





    },









    components:{
    context_menu,
  },
     methods: {
      toggleChildren() {
        this.isShow = !this.isShow;
      },
        OnOpenChildren() {
        this.isShow = true;
        this.$emit('OpenChildren')
      },



      onReadyDelete() {
        this.isReadyToDelete = !this.isReadyToDelete
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

.div1
  display: inline-block
</style>