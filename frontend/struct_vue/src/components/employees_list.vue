<template>
     <q-card  class="row unit-card bg-indigo-2 text-black rounded-borders" >
      <div class="col-3 unit  text-center" style="margin: auto">
         <q-img  :src=employee.image_url style="height: 220px; width: 200px;  " />
      </div>
       <q-card-section class="col-8 dense bordered padding unit">
        <q-item class="text-h4 text-center">{{employee.employee_name}} </q-item>
        <q-separator></q-separator>
        <q-item class="text-subtitle1">Должность: {{employee.employee_post}}</q-item>
        <q-item class="text-subtitle1">Дата начала работы: {{employee.date_of_joining}}</q-item>
        <q-item class="text-subtitle1">Дата рождения: {{employee.birthday_date}}</q-item>
      </q-card-section>
      <q-card-actions  class=" col-xs-1 unit" >
       <q-btn flat icon="edit" style="margin: auto" size="1.5em" @click="$emit('ShowEmployeeEdit', 'edit employee', employee)"></q-btn>
       <q-btn flat icon="delete" style="margin: auto" size="1.5em" @click="$emit('Delete', employee.id)"></q-btn>
      </q-card-actions>
    </q-card>
</template>
<script>



  export default {
    props: ['employee',  ],
    name: 'employees_list',
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
.unit
  border: 1px solid rgba(221, 218, 255, 0.66)

</style>