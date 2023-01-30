<template>
  <div class="recursive_tree">
    <div :style="indent" @click="toggleChildren">{{ slug }}</div>
   <div v-if="isShow">
     <recursive_tree
      v-for="group in children"
      v-bind:key="group.id"
      :slug="group.slug"
      :children="group.children"
      :depth="depth + 1"

    >
   </recursive_tree>
   </div>
  </div>
</template>
<script>
  export default {
    props: [ 'slug', 'children', 'depth'],
    name: 'recursive_tree',
    data() {
      return { isShow: false }
    },
    computed: {
      indent() {
        return { transform: `translate(${this.depth * 50}px)` }
      }
    },
     methods: {
      toggleChildren() {
        this.isShow = !this.isShow;
      }
    }
  }
</script>