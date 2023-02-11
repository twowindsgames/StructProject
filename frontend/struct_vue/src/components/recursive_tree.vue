<template>
  <div>


        <q-item
                 clickable
                :inset-level="depth"
                :hide-expand-icon="group.is_leaf_node"
                 @mouseenter="hover_edit = true"
                 @mouseleave="hover_edit = false"
        >
          <router-link :to="'/structure' + group.get_absolute_url">
                <div name="arrow" class="q-pa-none q-ma-none div1"  v-if="!group.is_leaf_node">
                   <q-icon v-if="isShow" name="arrow_drop_down"  size="2em" @click="toggleChildren">  </q-icon>
                   <q-icon v-else name="arrow_right" size="2em" @click="toggleChildren">  </q-icon>
                </div>
                <div class="q-pa-none  q-ma-none div1 ">
                  <em style="flex-wrap: wrap"> {{group.full_title}} </em>

                </div>
            </router-link>

                <q-btn  icon="edit" size="5px"  v-show="hover_edit"  >
                                <context_menu
                                @ReadyDelete="OnReadyDelete()"  @ShowEditTree="OnShowEditTree"
                                :group="group"

                                :root=false />
                </q-btn>

             <router-link top side :to="'/structure' + group.get_absolute_url" style="flex: max-content" >
             </router-link>

        </q-item>

        <div  v-if="isShow" transition-show="fade"  >
          <recursive_tree
          v-for="group in group.children"
          v-bind:key="group.id"
            @ReadyDelete="OnReadyDelete" @ShowEditTree="OnShowEditTree" @OpenChildren="OnOpenChildren"
            :group="group"
            :depth="depth + 1"

            :root="rootListener"
            :path="path">
          </recursive_tree>

        </div>


  </div>
</template>
<script>
  import context_menu from './context_menu.vue'

  export default {
    props: ['group',  'depth',   'root', 'path'],
    name: 'recursive_tree',
    data() {
      return {
        isShow: false,
        isReadyToDelete: false,
        rootListener: null,
        hover_edit: false

    }
    },
    mounted() {

      if (this.root == null){
        this.rootListener = this
      }
      else {
         this.rootListener = this.root
      }
      if (this.path[this.depth]==this.group.slug && this.path[this.path.length-1]!=this.group.slug){
        this.isShow=true
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

      OnReadyDelete() {
          this.rootListener.$emit('ReadyDelete', this.group)
      },

      OnShowEditTree(mode) {
         this.rootListener.$emit('ShowEditTree', mode, this.group)
      },


 },
 }
</script>
<style lang="sass" scoped>

.div1
  display: inline-block
</style>