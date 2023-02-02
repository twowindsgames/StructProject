<template>
  <div class="unit_list" >

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