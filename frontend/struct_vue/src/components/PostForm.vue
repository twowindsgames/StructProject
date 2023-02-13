<template>
  <div name="PostForm" class="q-pa-md">
    <form @input="checkForm" class="q-gutter-y-md column post-form">

      <div v-if="mode==='edit node' || mode==='add node'">

        <div>Название подразделения (полное)</div>
        <q-input class="post-item" outlined v-model="post_data_node.full_title" placeholder="Введите полное название"/>

        <div>Название подразделения (сокращенное)</div>
        <q-input class="post-item" outlined v-model="post_data_node.title" placeholder="Введите сокращенное название"/>
      </div>

      <div v-else>
        <q-list >

          <div>Фамилия </div>
          <q-input  class="post-item" outlined v-model="post_data_employee.name" placeholder="Введите фамилию"/>

          <div>Имя </div>
          <q-input class="post-item" outlined v-model="post_data_employee.last_name" placeholder="Введите имя"/>

          <div>Отчество </div>
          <q-input class="post-item" outlined v-model="post_data_employee.patronymic" placeholder="Введите отчество"/>

          <div>Должность</div>
          <q-input class="post-item" outlined v-model="post_data_employee.post"
                   placeholder="Введите должность"/>

          <div>Дата рождения</div>
          <q-input v-model="post_data_employee.birthday_date" outlined type="date"  />

          <div>Дата начала работы</div>
          <q-input v-model="post_data_employee.date_of_joining"  outlined  type="date"  />


          <div>Фото сотрудника</div>
          <q-img v-if="imageURL" style="height: 110px; width: 100px;" class="q-pa-md q-ma-md " :src="imageURL"/>
          <q-file
              v-model="post_data_employee.image"
              @update:model-value="handleUpload()"
              label="Добавьте фото сотрудника (необязательно)"
              filled
          />


        </q-list>
      </div>

      <div>
        <q-btn label="Применить" :disable="!validate" color="primary" @click="postData" v-close-popup/>
      </div>


    </form>


  </div>
</template>

<script>


export default {
  name: 'PostForm',
  props: ['mode', 'current_data', 'group_id'],
  data() {
    return {

      imageURL: '',
      validate: false,
      post_data_node: {
        full_title: '',
        title: '',
        parent: '',
        id: '',
      },
      post_data_employee: {
        name: '',
        last_name: '',
        patronymic: '',
        post: '',
        date_of_joining: '',
        birthday_date: '',
        group: '',
        id: '',
        image: 'default',
      },


    }
  },


  mounted() {
    if (this.mode === 'edit node') {
      this.post_data_node.full_title = this.current_data.full_title
      this.post_data_node.title = this.current_data.title
      this.post_data_node.id = this.current_data.id
      this.post_data_node.parent = this.current_data.parent
    }
    if (this.mode === 'edit employee') {
      this.post_data_employee.name = this.current_data.name
      this.post_data_employee.last_name = this.current_data.last_name
      this.post_data_employee.patronymic = this.current_data.patronymic
      this.post_data_employee.post = this.current_data.post
      this.post_data_employee.date_of_joining = this.current_data.date_of_joining
      this.post_data_employee.birthday_date = this.current_data.birthday_date
      this.post_data_employee.group = this.current_data.group
      this.post_data_employee.id = this.current_data.id
    }

  },

  methods: {
    postData() {
      if (this.mode.includes('node')) {
        if (this.current_data == null) {
          this.post_data_node.parent = ''
        } else {
          if (this.mode.includes('edit'))
            this.post_data_node.parent = this.current_data.parent
          else
            this.post_data_node.parent = this.current_data.id
        }
        this.$emit('dataPost', this.post_data_node)

      } else {
        this.post_data_employee.group = this.group_id
        this.$emit('dataPost', this.post_data_employee)
      }
    },
    handleUpload() {

      if (this.post_data_employee.image) {
        this.imageURL = URL.createObjectURL(this.post_data_employee.image);
      }
    },
    checkForm() {
      if (this.post_data_employee.name
          &&this.post_data_employee.last_name
          &&this.post_data_employee.patronymic
          && this.post_data_employee.post
          && this.post_data_employee.date_of_joining
          && this.post_data_employee.birthday_date
          ||
          this.post_data_node.title
          && this.post_data_node.full_title
      ) {
        this.validate = true
      } else {
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
  margin-bottom: 3px

.img
  border: dashed red
</style>