<template>
  <div class="info">




    <div v-if=isLoadUnits>...</div>



 <div class="q-pa-md row items-start q-gutter-md" style="margin-top: 5px">
     <q-intersection class="my-card" v-for="unit in units" v-bind:key="unit.id" transition="fade">
      <q-card-section class="bg-indigo-2 text-black rounded-borders" >
        <div class="text-h6">{{unit.employeeName}}</div>
        <div class="text-subtitle2">{{unit.employeePost}}</div>
        <div class="text-hide">{{unit.dateOfJoining}}</div>
       <q-card-actions align="right">
        <q-btn flat>Action 1</q-btn>
        <q-btn flat>Action 2</q-btn>
      </q-card-actions>
      </q-card-section>
    </q-intersection>
</div>


     <q-page-sticky position="top" expand class="bg-blue-grey-5 text-white ">
       <div>
        Подразделение: {{ group.full_title }}
        ({{ group.title }})
      </div>


    </q-page-sticky>
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
<style lang="sass" scoped>
.my-card
  width: 100%
</style>

