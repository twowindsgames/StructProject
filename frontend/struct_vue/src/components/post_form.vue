<template>
  <div class="q-pa-md">
    <form @input="checkForm"  class="q-gutter-y-md column post-form"  >

      <div v-if="mode==='edit node' || mode==='add node'">
        <div>Название подразделения (полное)</div>
      <q-input  class="post-item"  outlined v-model="post_data_node.full_title"  placeholder="Введите полное название"  />
        <div>Название подразделения (сокращенное)</div>
      <q-input  class="post-item"  outlined v-model="post_data_node.title" placeholder="Введите сокращенное название"  />
      </div>
       <div v-else>
<q-list>
      <div>ФИО сотрудника</div>
      <q-input class="post-item" outlined v-model="post_data_employee.employee_name"  placeholder="Введите ФИО"   />
       <div>Должность</div>
      <q-input class="post-item" outlined v-model="post_data_employee.employee_post" placeholder="Введите должность"   />

       <div>Дата рождения</div>
     <q-input class="post-item" outlined v-model="post_data_employee.birthday_date" placeholder="Установите дату рождения"   >
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date v-model="post_data_employee.birthday_date" v-close-popup @click="checkForm()"  mask="YYYY-MM-DD">

              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
    </q-input>
<div>Дата начала работы</div>
    <q-input class="post-item" outlined   v-model="post_data_employee.date_of_joining" placeholder="Установите дату начала работы"   >
        <template v-slot:prepend >
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date  v-model="post_data_employee.date_of_joining" v-close-popup @click="checkForm()"   mask="YYYY-MM-DD">
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
    </q-input>
<div>Фото сотрудника</div>

   <q-img v-if="imageURL" style="height: 220px; width: 200px;" class="q-pa-md q-ma-md "    :src="imageURL"  />
         <q-file
      v-model="post_data_employee.image"
      @update:model-value="handleUpload()"
      label="Добавьте фото сотрудника (необязательно)"
      filled
    />


</q-list>
       </div>

      <div>
        <q-btn label="Применить" :disable="!validate"  color="primary" @click="PostData" v-close-popup/>
      </div>


    </form>


  </div>
</template>

<script>







export default {

  props: ['mode','current_data', 'group_id'],
  data () {
    return {

      imageURL: '',
      validate:false,
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

  methods: {
    PostData() {
      if (this.mode.includes('node')) {
        if (this.current_data == null) {
          this.post_data_node.parent = ''
        } else {
          if (this.mode.includes('edit'))
            this.post_data_node.parent = this.current_data.parent
          else
            this.post_data_node.parent = this.current_data.id
        }
        this.$emit('DataPost', this.post_data_node)

      } else {
        this.post_data_employee.group = this.group_id
        this.$emit('DataPost', this.post_data_employee)
      }
    },
     handleUpload ()  {

      if ( this.post_data_employee.image) {

        this.imageURL = URL.createObjectURL( this.post_data_employee.image);
      }
    },
    checkForm(){
      if (this.post_data_employee.employee_name
          && this.post_data_employee.employee_post
          && this.post_data_employee.date_of_joining
          && this.post_data_employee.birthday_date
          )
      {
        this.validate = true
      }
      else
      {
        this.validate = false
      }

    }


  }

  }


</script>

<style lang="sass" scoped>
.post-form
  min-width: 400px
.post-item
  margin-top: 0px
  margin-bottom: 8px
.img
  border: dashed red
</style>