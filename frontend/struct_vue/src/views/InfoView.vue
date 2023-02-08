<template>
  <div class="info">
    <div class="row row-up  text-white">
      <div class="col-10 col-up bg-indigo-4 text-center ">
        <p class="text-h3 text-weight-bold">{{ group.full_title }}</p>
        <p class="text-weight-thin">{{ group.title }}</p>
      </div>
      <div class="col col-up bg-indigo-3 text-italic q-pa-xs 	">
        <p>Сотрудников: {{statistic['employees_count']}} ч.</p>
        <p>Средний возраст: {{statistic['aver_age']}} г.</p>
        <p>Средний стаж: {{statistic['aver_exp']}} г.</p>
      </div>
    </div>

 <div class="row row-up text-white">
 <div class="employee-list  q-gutter-md justify-center" >
     <q-intersection v-for="employee in employees" v-bind:key="employee.id" transition="fade">
     <employees_list @Delete="OnDelete" @ShowEmployeeEdit="OnShowEmployeeEdit" :employee="employee"> </employees_list>
     </q-intersection>
    </div>
</div>


<q-page-sticky   position="right" style="margin-right: 30px" >
        <q-btn @click="OnShowEmployeeEdit('add employee',null)" round color="green" icon="add" ></q-btn>
</q-page-sticky>
<modal_menu v-model="editEmployeeModalView" :title="editOptions.title">
      <post_form @DataPost="OnDataPost" :current_data="editOptions.employee" :mode="editOptions.mode" :group_id="group.id" >
      </post_form>
</modal_menu>

  </div>
 <router-view />
</template>




<script>

import axios from 'axios'
import employees_list from "../components/employees_list.vue";
import modal_menu from '../components/modal_menu.vue'
import post_form from '../components/post_form.vue'



export default {
  name: 'GroupInfo',
  components: {
  employees_list, modal_menu, post_form
  },
  data() {
    return {
      group: {},
      employees: [],
      editOptions: {mode: 'режим', title: 'заголовок', employee: null },
      editEmployeeModalView: false,
      statistic: ''
    }
  },
   mounted() {

     this.getGroupDetailInfo()

  },

  methods: {

    getGroupDetailInfo() {

      const tree_hierarchy = this.$route.params.tree_hierarchy
      axios
          .get(`/api/group/${tree_hierarchy}`)
          .then(response => {
           this.group = response.data
           this.statistic = response.data.get_group_stat
           this.getGroupEmployees(this.group.id)

          })
          .catch(error => {
            console.log(error)
          })


    },
    getGroupEmployees(group_id) {
    axios
        .get("/api/employees",{ params: { group_id: group_id }})
        .then(response => {
          this.employees = response.data
          this.isLoadUnits = false;
        })
        .catch(error => {
          console.log(error)
        })

  },
    OnDelete(id){
     axios.delete('/api/employees', {params: {id: id}}).then(response => {
        this.getGroupEmployees(this.group.id)

          this.getGroupDetailInfo()
              console.log(response)})
                .catch(error => {console.log(error)})
    },

     OnShowEmployeeEdit(mode, employee) {

    this.editOptions.mode = mode
    this.editOptions.employee = employee

    if (mode==="edit employee")  this.editOptions.title = "Изменить информацию о сотруднике"
    else  this.editOptions.title = "Добавить сотрудника"
    this.editEmployeeModalView=true

    },

     OnDataPost(post_data){
     let request

     if (this.editOptions.mode==="add employee")request=axios.post('api/employees', post_data,{headers: {"Content-Type": "multipart/form-data"}})
     if (this.editOptions.mode==="edit employee")request= axios.put('api/employees', post_data,{headers: {"Content-Type": "multipart/form-data"}})
       request.then(response => {
          this.getGroupEmployees(this.group.id)
          this.getGroupDetailInfo()
              console.log(response)})
                .catch(error => {console.log(error)})

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

