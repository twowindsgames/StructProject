<template>
  <div class="info">
    <div class="row row-up  text-white">
      <div class="col-10 col-up bg-indigo-4 text-center ">
        <p class="text-h3 text-weight-bold">{{ group.full_title }}</p>
        <p class="text-weight-thin">{{ group.title }}</p>
      </div>

      <div class="col col-up bg-indigo-3 text-italic q-pa-xs 	">
        <p>Сотрудников: {{ statistic['employees_count'] }} ч.</p>
        <p>Средний возраст: {{ statistic['aver_age'] }} г.</p>
        <p>Средний стаж: {{ statistic['aver_exp'] }} г.</p>
      </div>
    </div>

    <div class="row row-up text-white">
      <div class="employee-list  q-gutter-md justify-center">
        <q-intersection v-for="employee in employees" v-bind:key="employee.id" transition="fade">
          <employees-card @Delete="onDelete" @showEmployeeEdit="onShowEmployeeEdit"
                          :employee="employee"></employees-card>
        </q-intersection>
      </div>
    </div>

    <q-page-sticky position="right" style="margin-right: 30px">
      <q-btn @click="onShowEmployeeEdit('add employee',null)" round color="green" icon="add"></q-btn>
    </q-page-sticky>
  </div>

  <modal-menu v-model="editEmployeeModalView" :title="editOptions.title">
    <post-form @DataPost="onDataPost" :current_data="editOptions.employee" :mode="editOptions.mode"
               :group_id="group.id">
    </post-form>
  </modal-menu>

</template>


<script>

import axios from 'axios'
import EmployeesCard from "../components/EmployeeCard";
import ModalMenu from '../components/ModalMenu.vue'
import PostForm from '../components/PostForm.vue'
import NotifyManager from '../components/NotifyManager.vue'


export default {
  name: 'GroupInfo',
  components: {
    EmployeesCard,
    ModalMenu,
    PostForm
  },
  data() {
    return {
      group: {},
      employees: [],
      editOptions: {mode: 'режим', title: 'заголовок', employee: null},
      editEmployeeModalView: false,
      statistic: ''
    }
  },
  mounted() {
    this.getGroupDetailInfo()
  },

  methods: {
    updateInfo() {
      this.getGroupEmployees(this.group.id)
      this.getGroupDetailInfo()
    },


    getGroupDetailInfo() {
      const hierarchy = this.$route.params.hierarchy
      if (hierarchy==0) return;
      axios
          .get(`/api/group/${hierarchy}`)
          .then(response => {
            this.group = response.data
            this.statistic = response.data.get_group_stat
            this.getGroupEmployees(this.group.id)

          })
          .catch(error => {
            NotifyManager.methods.pushErrorNotify(error)
          })
    },

    getGroupEmployees(group_id) {
      axios
          .get("/api/employees", {params: {group_id: group_id}})
          .then(response => {
            this.employees = response.data
          })
          .catch(error => {
            NotifyManager.methods.pushErrorNotify(error)
          })

    },

    onShowEmployeeEdit(mode, employee) {
      this.editOptions.mode = mode
      this.editOptions.employee = employee
      if (mode === "edit employee")
        this.editOptions.title = "Изменить информацию о сотруднике"
      else
        this.editOptions.title = "Добавить сотрудника"
      this.editEmployeeModalView = true

    },
    onDataPost(postData) {
      let request
      if (this.editOptions.mode === "add employee")
        request = axios.post('api/employees', postData, {headers: {"Content-Type": "multipart/form-data"}})
      if (this.editOptions.mode === "edit employee")
        request = axios.put('api/employees', postData, {headers: {"Content-Type": "multipart/form-data"}})
      request.then(response => {
        NotifyManager.methods.pushResponceNotify(response)
        this.updateInfo()
      })
          .catch(error => {
            NotifyManager.methods.pushPostErrorNotify(error)
          })

    },
    onDelete(id) {

      axios.delete('/api/employees', {params: {id: id}})
          .then(response => {
            NotifyManager.methods.pushResponceNotify(response)
            this.updateInfo()
          })
          .catch(error => {
            NotifyManager.methods.pushErrorNotify(error)
          })
    },
  },
}
</script>
<style lang="sass" scoped>
.employee-list
  width: 90%
  margin: 0 auto

.row-up
  min-height: 95px

.col-up
  border: 1px solid rgba(138, 139, 185, 0.79)

.col-up p
  margin: 5px 5px
</style>

