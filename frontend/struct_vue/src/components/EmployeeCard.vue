<template>
  <q-card class="row unit-card bg-indigo-2 text-black rounded-borders">

    <div class="col-2 unit text-center" style="margin: auto">
      <q-img class="q-pa-md q-ma-md" :src=employee.image style="height: 220px; width: 200px;  "/>
    </div>

    <q-card-section class="col-9 dense bordered padding unit ">
      <q-item class="text-h4 text-center q-la-md ">
        {{ employee.name }}
        {{ employee.last_name }}
        {{ employee.patronymic }} </q-item>
      <q-separator></q-separator>
      <q-item class="text-subtitle1 q-pa-md">Должность: {{ employee.post }}</q-item>
      <q-item class="text-subtitle1 q-pa-md">Дата начала работы: {{ employee.date_of_joining }}</q-item>
      <q-item class="text-subtitle1 q-pa-md">Дата рождения: {{ employee.birthday_date }}</q-item>
    </q-card-section>

    <div class="col-xs-1 div1  unit ">
      <q-btn flat icon="edit" class="q-ma-md q-pa-lg " size="1.5em"
             @click="$emit('showEmployeeEdit', 'edit employee', employee)"></q-btn>
      <q-btn flat icon="delete" class="q-ma-md q-pa-lg" size="1.5em" @click="$emit('delete', employee.id)"></q-btn>
    </div>

  </q-card>
</template>
<script>

export default {
  props: ['employee',],
  name: 'EmployeeCard',
  data() {
    return {
      isShow: false,
      isReadyToDelete: false,
      rootListener: null,
    }
  },
  mounted() {
    if (this.root == null) {
      this.rootListener = this
    } else {
      this.rootListener = this.root
    }
  },
  methods: {
    toggleChildren() {
      this.isShow = !this.isShow;
    },
    onDelete() {
      this.rootListener.$emit('delete', this.group.id)
    },
    onShowEditTree(mode) {
      this.rootListener.$emit('showEditTree', mode, this.group)
    },
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