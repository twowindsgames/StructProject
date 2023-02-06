<template>
<q-card >
      <q-card-section  class="bg-indigo-2 text-black rounded-borders" >
        <div class="text-h6">{{unit.employeeName}}</div>
        <div class="text-subtitle2">{{unit.employeePost}}</div>
        <div class="text-hide">{{unit.dateOfJoining}}</div>
         <q-card-actions align="right">
          <q-btn flat @click="$emit('ShowUnitEdit', 'edit unit', unit)">edit</q-btn>
          <q-btn flat @click="$emit('Delete', unit.id)">del</q-btn>
        </q-card-actions>
      </q-card-section>
</q-card>


</template>
<script>



  export default {
    props: ['unit',  ],
    name: 'unit_list',
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
.my-card
  width: 100%
  align-content: center
</style>