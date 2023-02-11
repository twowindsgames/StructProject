<template>
  <div class="q-pa-md">
    <q-card class="q-gutter-y-md column " flat  >

      <div>
        <div class="text-subtitle1">Вы собираетесь удалить подразделение:</div>
         <q-separator class="q-mt-md" ></q-separator>
        <div class="text-h6 text-center q-pa-xs">«{{ group.full_title }}»</div>
         <q-separator ></q-separator>


      </div>
      <div >
        <q-card-actions align="evenly">
        <q-btn  label="Удалить"  color="negative" @click="DeleteNode" v-close-popup/>
        <q-btn label="Отменить" v-close-popup/>
      </q-card-actions>



      </div>



    </q-card>


  </div>
</template>

<script>


export default {
  name: 'delete-form',
  props: ['mode','group'],
  data () {
    return {
    }
  },



  methods:{
    DeleteNode(){
         this.$emit('Delete', this.group.id)
},
  }
  }
</script>

<style lang="sass" scoped>
.post-form
  min-width: 400px
.post-item
  margin-top: 8px
</style>