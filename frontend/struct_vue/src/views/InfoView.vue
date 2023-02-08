<template>
  <div class="info">
    <div class="row row-up text-white"  >
      <div class="col-10 col-up bg-indigo-4 text-center">
        <p class="text-h3 text-weight-bold">{{ group.full_title }}</p>
        <p class="text-weight-thin">{{ group.title }}</p>
      </div>
      <div class="col col-up bg-indigo-3 text-italic	">
        <p>Сотрудников: {{statistic['units_count']}} ч.</p>
        <p>Средний возраст: {{statistic['aver_age']}} г.</p>
        <p>Средний стаж: {{statistic['aver_exp']}} г.</p>
      </div>
    </div>

    <div class="row row-up text-white"  >
 <div class="unit-list  q-gutter-md justify-center" >
     <q-intersection  v-for="unit in units" v-bind:key="unit.id" transition="fade">
     <unit_list  @Delete="OnDelete" @ShowUnitEdit="OnShowUnitEdit" :unit="unit"> </unit_list>
     </q-intersection>
    </div>
</div>
<q-page-sticky   position="right" style="margin-right: 30px" >
        <q-btn  @click="OnShowUnitEdit('add unit',null)" round color="green" icon="add" ></q-btn>
</q-page-sticky>
<modal_menu v-model="editUnitModalView" :title="editOptions.title">
      <post_form @DataPost="OnDataPost" :current_data="editOptions.unit" :mode="editOptions.mode" :group_id="group.id" >
      </post_form>
</modal_menu>

  </div>
 <router-view />
</template>




<script>

import axios from 'axios'
import unit_list from "@/components/unit_list.vue";
import modal_menu from '../components/modal_menu.vue'
import post_form from '../components/post_form.vue'



export default {
  name: 'GroupInfo',
  components: {
  unit_list, modal_menu, post_form
  },
  data() {
    return {
      group: {},
      units: [],

      editOptions: {mode: 'режим', title: 'заголовок', unit: null },
      editUnitModalView: false,
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
           this.getGroupUnits(this.group.id)

          })
          .catch(error => {
            console.log(error)
          })


    },
    getGroupUnits(groupId) {
    axios
        .get("/api/units",{ params: { groupId: groupId }})
        .then(response => {
          this.units = response.data
          this.isLoadUnits = false;
        })
        .catch(error => {
          console.log(error)
        })

  },
    OnDelete(id){
     axios.delete('/api/units', {params: {id: id}}).then(response => {
        this.getGroupUnits(this.group.id)

          this.getGroupDetailInfo()
              console.log(response)})
                .catch(error => {console.log(error)})
    },

     OnShowUnitEdit(mode,unit) {

    this.editOptions.mode = mode
    this.editOptions.unit = unit

    if (mode==="edit unit")  this.editOptions.title = "Изменить информацию о сотруднике"
    else  this.editOptions.title = "Добавить сотрудника"
    this.editUnitModalView=true

    },

     OnDataPost(post_data){
     let request

     if (this.editOptions.mode==="add unit")request=axios.post('api/units', post_data,{headers: {"Content-Type": "multipart/form-data"}})
     if (this.editOptions.mode==="edit unit")request= axios.put('api/units', post_data,{headers: {"Content-Type": "multipart/form-data"}})
       request.then(response => {
          this.getGroupUnits(this.group.id)
          this.getGroupDetailInfo()
              console.log(response)})
                .catch(error => {console.log(error)})

    },



},





}
</script>
<style lang="sass" scoped>
.unit-list
  width: 90%
  margin: 0 auto
.row-up
  min-height: 95px
.col-up
  border: 1px solid rgba(138, 139, 185, 0.79)
.col-up p
  margin: 5px 5px
</style>

