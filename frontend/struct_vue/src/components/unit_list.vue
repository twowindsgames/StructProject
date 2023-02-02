<template>
  <div class="recursive_tree" >
    <div :style="indent"  @click="toggleChildren"><div  @click="getUnitsByGroup(groupId)">{{ slug }}</div></div>

   <div v-if="isShow">
      <recursive_tree
      v-for="group in children"

      v-bind:key="group.id"
      :slug="group.slug"
      :children="group.children"
      :depth="depth + 1"
      :group-id = "group.id"
      >

   </recursive_tree>
   </div>
  </div>
</template>
<script>
  import axios from "axios";

  export default {
    props: [ 'slug', 'children', 'depth', 'groupId'],
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

    }
    },

  }
</script>