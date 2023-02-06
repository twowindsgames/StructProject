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
      <q-input  class="post-item"  outlined v-model="post_data_unit.birthdayDate" placeholder="23.07.2000" hint="Дата рождения"  >
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date v-model="post_data_unit.birthdayDate" mask="YYYY-MM-DD">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
    </q-input>

          <q-input  class="post-item"  outlined v-model="post_data_unit.dateOfJoining" placeholder="23.07.2000" hint="Дата рождения"  >
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date v-model="post_data_unit.image" mask="YYYY-MM-DD">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
    </q-input>

         <q-file
      v-model="post_data_unit.image"
      label="Pick one file"
      filled
      style="max-width: 300px"
    />


       </div>

      <div>
        <q-btn label="Применить"  color="primary" @click="PostData" v-close-popup/>
      </div>


    </div>


  </div>
</template>

<script>
import date_input from "@/components/date_input";

export default {
  props: ['mode','current_data', 'group_id'],
  data () {
    return {
      post_data_node: {
        full_title: '',
        title: '',
        parent: '',
        id:'',

      },
      post_data_unit:{
           employeeName: '',
           employeePost: '',
           dateOfJoining: '',
           birthdayDate: '',
           group: '',
           id:'',
           image:'',
      },


    }
  },
  components(){
    date_input
  },
  mounted() {
    if(this.mode==='edit node') {
      this.post_data_node.full_title= this.current_data.full_title
      this.post_data_node.title= this.current_data.title
      this.post_data_node.id= this.current_data.id
      this.post_data_node.parent= this.current_data.parent
    }
      if(this.mode==='edit unit') {
      this.post_data_unit.employeeName= this.current_data.employeeName
      this.post_data_unit.employeePost= this.current_data.employeePost
      this.post_data_unit.dateOfJoining= this.current_data.dateOfJoining
      this.post_data_unit.birthdayDate= this.current_data.birthdayDate
      this.post_data_unit.group= this.current_data.group
      this.post_data_unit.id= this.current_data.id

    }
  },

  methods:{
    PostData(){
     if(this.mode==='edit node' || this.mode==='add node') {
      if(this.mode==='add node') this.post_data_node.parent = this.current_data.id
       this.$emit('DataPost', this.post_data_node)
     }
     else {

     this.post_data_unit.group = this.group_id
     this.$emit('DataPost', this.post_data_unit)
     }
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