<template>
  <div class="units">


    <q-page-sticky position="top" expand class="bg-accent text-white">
       <div>
        ssssssss {{ group.title }}
      </div>



    </q-page-sticky>





  </div>
 <router-view />
</template>




<script>

import axios from 'axios'



export default {
  name: 'UnitsList',

  data() {
    return {
      group: {}

    }
  },
  mounted() {
    this.getLatestProducts()

  },
  methods: {

    getLatestProducts() {

      const tree_hierarchy = this.$route.params.tree_hierarchy
      axios
          .get(`/api/group/${tree_hierarchy}`)
          .then(response => {
            this.group = response.data
          })
          .catch(error => {
            console.log(error)
          })

    }
  },


}
</script>
<style lang="sass" scoped>
.struct-item
  margin: 2px 5px
</style>
