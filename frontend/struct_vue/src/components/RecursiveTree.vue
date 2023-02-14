<template>
  <div name="recursive-tree" class="q-pa-none q-ma-xs-none">
    <q-item
        clickable
        :inset-level="depth"
        :hide-expand-icon="group.is_leaf_node"
        @mouseenter="hover_edit = true"
        @mouseleave="hover_edit = false"
        active-class="menu-link"
        @click= "onLinkSet"
        :active="link === group.full_title"
    >
        <div name="arrow" class="div1 " v-if="!group.is_leaf_node">
          <q-icon v-if="isShow" name="arrow_drop_down" size="2em" @click="toggleChildren"></q-icon>
          <q-icon v-else name="arrow_right" size="2em" @click="toggleChildren"></q-icon>
        </div>

          <router-link  class="div1" :to="'/structure' + group.get_absolute_url"
                        style="flex-wrap: wrap;
                        color: #2a0e70;
                        text-decoration: #000000;"
                        clickable

          >
            <em class="div1 q-pa-xs"> {{ group.full_title }} </em>
          </router-link>

      <div name="arrow" class="div1  q-pa-xs" >
          <q-icon size="1.2em" name="more_vert" class="div1"  v-show="hover_edit">
        <context-menu
            @readyDelete="onReadyDelete()" @showEditTree="onShowEditTree"
            :group="group"
            :root=false
        />
      </q-icon>
        </div>
      <router-link top side :to="'/structure' + group.get_absolute_url" style="flex: max-content"/>
    </q-item>

    <div v-if="isShow" transition-show="fade">
      <recursive-tree
          v-for="group in group.children" v-bind:key="group.id"
          @readyDelete="onReadyDelete" @showEditTree="onShowEditTree" @openChildren="onOpenChildren"
          :group="group"
          :depth="depth + 1"
          :root="rootListener"
          :path="path"
          :link="link"
           >
      </recursive-tree>

    </div>
  </div>
</template>
<script>
import ContextMenu from './ContextMenu.vue'

export default {
  props: ['group', 'depth', 'root', 'path', 'link'],
  name: 'RecursiveTree',
  data() {
    return {
      isShow: false,
      isReadyToDelete: false,
      rootListener: null,
      hover_edit: false,


    }
  },
  mounted() {

    if (this.root == null) {
      this.rootListener = this
    }
    else {
      this.rootListener = this.root
    }
    if (this.path[this.depth] == this.group.slug && this.path[this.path.length - 1] != this.group.slug) {
      this.isShow = true
    }


  },
  components: {
    ContextMenu,
  },
  methods: {
    toggleChildren() {
      this.isShow = !this.isShow;
    },
    onOpenChildren() {
      this.isShow = true;
      this.$emit('openChildren')
    },
    onReadyDelete() {
      this.rootListener.$emit('readyDelete', this.group)
    },
    onShowEditTree(mode) {
      this.rootListener.$emit('showEditTree', mode, this.group)
    },
    onLinkSet() {
      this.rootListener.$emit('setLink', this.group.full_title)
    },
  },
}
</script>
<style lang="sass" scoped>
.div1
  display: inline-block
.menu-link
  color: rgba(0, 0, 0, 0.97)
  background: rgba(149, 154, 248, 0.45)
</style>