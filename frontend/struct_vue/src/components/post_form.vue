<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md column post-form"  >

      <div v-if="mode==='edit node' || mode==='add node'">
      <q-input  class="post-item"  outlined v-model="post_data_node.full_title"  placeholder="Управление информационного обеспечения" hint="Полное название подразделения"  />
      <q-input  class="post-item"  outlined v-model="post_data_node.title" placeholder="УИО" hint="Краткое название подразделения"  />
      </div>
       <div v-else>
      <q-input class="post-item" outlined v-model="post_data_employee.employee_name" placeholder="Иванов Иван Иванович" hint="ФИО сотрудника"  />
      <q-input class="post-item" outlined v-model="post_data_employee.employee_post" placeholder="инженер" hint="Должность сотрудника"  />
      <q-input class="post-item" outlined v-model="post_data_employee.birthday_date" placeholder="23.07.2000" hint="Дата рождения"  >
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date v-model="post_data_employee.birthday_date" mask="YYYY-MM-DD">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
    </q-input>

          <q-input class="post-item" outlined v-model="post_data_employee.date_of_joining" placeholder="23.07.2000" hint="Дата начала работы"  >
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date v-model="post_data_employee.date_of_joining" mask="YYYY-MM-DD">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
    </q-input>

         <q-file
      v-model="post_data_employee.image"
      label="Фото сотрудника (необязательно)"
      filled
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
      post_data_employee:{
           employee_name: '',
           employee_post: '',
           date_of_joining: '',
           birthday_date: '',
           group: '',
           id:'',
           image:'default',
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
      if(this.mode==='edit employee') {
      this.post_data_employee.employee_name = this.current_data.employee_name
      this.post_data_employee.employee_post = this.current_data.employee_post
      this.post_data_employee.date_of_joining = this.current_data.date_of_joining
      this.post_data_employee.birthday_date = this.current_data.birthday_date
      this.post_data_employee.group = this.current_data.group
      this.post_data_employee.id = this.current_data.id

    }

  },

  methods:{
    PostData(){
     if(this.mode==='edit node' || this.mode==='add node')
     {
      if(this.mode==='add node')
       if (this.current_data==null)
          {this.post_data_node.parent = ''}
       else
          {this.post_data_node.parent = this.current_data.id}

       this.$emit('DataPost', this.post_data_node)
     }
     else {
     this.post_data_employee.group = this.group_id
     this.$emit('DataPost', this.post_data_employee)
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