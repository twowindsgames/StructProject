<template>
  <div class="info">


    <q-page-sticky position="top" expand class="bg-accent text-white">
       <div>
        Подразделение: {{ group.title }}
      </div>
    </q-page-sticky>

    <div v-if=isLoadUnits>...</div>



    <div v-if=!isLoadUnits>
        <div  v-for="unit in units" v-bind:key="unit.id" >
            <div>{{unit.employeeName}}</div>
        </div>
    </div>



  </div>
 <router-view />
</template>




<script>

import axios from 'axios'




export default {
  name: 'GroupInfo',

  data() {
    return {
      group: {},
      units: [],
      isLoadUnits:false,
    }
  },
   mounted() {
     this.isLoadUnits = true;
     this.getGroupDetailInfo()

  },

  methods: {

    getGroupDetailInfo() {

      const tree_hierarchy = this.$route.params.tree_hierarchy
      axios
          .get(`/api/group/${tree_hierarchy}`)
          .then(response => {
           this.group = response.data
           this.getGroupUnits(this.group.id)
          })
          .catch(error => {
            console.log(error)
          })

    },
    getGroupUnits(groupId) {
    axios
        .get("/api/units",{ params: { groupId: groupId }})
        .then(response => {
          this.units = response.data
          this.isLoadUnits = false;
        })
        .catch(error => {
          console.log(error)
        })

  },
},




}
</script>

