<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md column post-form"  >

      <div v-if="mode==='edit node' || mode==='add node'">
      <q-input  class="post-item"  outlined v-model="post_data_node.full_title"  placeholder="Управление информационного обеспечения" hint="Полное название подразделения"  />
      <q-input  class="post-item"  outlined v-model="post_data_node.title" placeholder="УИО" hint="Краткое название подразделения"  />
      </div>
       <div v-else>
      <q-input  class="post-item"  outlined v-model="post_data_unit.employeeName"  placeholder="Иванов Иван Иванович" hint="ФИО сотрудника"  />
      <q-input  class="post-item"  outlined v-model="post_data_unit.employeePost" placeholder="инженер" hint="Должность сотрудника"  />
      <q-input  class="post-item"  outlined v-model="post_data_unit.dateOfJoining" placeholder="23.07.2010" hint="Дата начала работы в подразделении"  />
      </div>

      <div>
        <q-btn label="Применить"  color="primary" @click="PostData" v-close-popup/>
      </div>


    </div>


  </div>
</template>

<script>


export default {
  props: ['mode','current_data'],
  data () {
    return {
      post_data_node:[
           {full_title:''},
           { title:'',}
      ],
      post_data_unit:[
           {employeeName: ''},
           {employeePost: ''},
           {dateOfJoining: ''},
           {groupId: 0},
      ],


    }
  },
  methods:{
    PostData(){
     if(this.mode==='edit node' || this.mode==='add node')  this.$emit('DataPost', this.post_data_node)
     else this.$emit('DataPost', this.post_data_unit)
    }

  }
}
</script>

<style lang="sass" scoped>
.post-form
  min-width: 400px
.post-item
  margin-top: 8px
</style>