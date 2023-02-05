<template>
  <div class="info">




    <div v-if=isLoadUnits>...</div>



 <div class="q-pa-md row items-start q-gutter-md" style="margin-top: 5px">
     <q-intersection class="my-card" v-for="unit in units" v-bind:key="unit.id" transition="fade">
     <unit_list @Delete="OnDelete" @ShowUnitEdit="OnShowUnitEdit" :unit="unit"> </unit_list>
    </q-intersection>
</div>

    <modal_menu v-model="editUnitModalView" :title="editOptions.title">
      <post_form @DataPost="OnDataPost" :current_data="editOptions.unit" :mode="editOptions.mode" :group_id="editOptions.group_id" >
      </post_form>
    </modal_menu>

     <q-page-sticky  expand  align="right" position="top"   class="bg-blue-grey-5 text-white ">
       <div >
        Подразделение: {{ group.full_title }}
        ({{ group.title }})


      </div>



    </q-page-sticky>
     <q-page-sticky  expand  align="right" position="top-right"   >
        <q-btn  @click="OnShowUnitEdit('add unit',null)" round color="green" icon="add" ></q-btn>
    </q-page-sticky>


  </div>
 <router-view />
</template>




<script>

import axios from 'axios'
import unit_list from "@/components/unit_list";
import modal_menu from '../components/modal_menu.vue'
import post_form from '../components/post_form.vue'



export default {
  name: 'GroupInfo',
  components: {unit_list,
  modal_menu, post_form
  },
  data() {
    return {
      group: {},
      units: [],
      isLoadUnits:false,
      editOptions: {mode: 'режим', title: 'заголовок', unit: null , group_id: null},
      editUnitModalView: false
    }
  },
   mounted() {
     this.isLoadUnits = true;
     this.getGroupDetailInfo()

  },

  methods: {

    getGroupDetailInfo() {

      const tree_hierarchy = this.$route.params.tree_hierarchy
      axios
          .get(`/api/group/${tree_hierarchy}`)
          .then(response => {
           this.group = response.data
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
     axios.get('api/delete', {params: {groupId: id}})
    },

     OnShowUnitEdit(mode,unit) {

    this.editOptions.mode = mode
    this.editOptions.unit = unit
    if (unit!==null)this.editOptions.group_id = unit.group.id
    if (mode==="edit unit")  this.editOptions.title = "Изменить информацию о сотруднике"
    else  this.editOptions.title = "Добавить сотрудника"
    this.editUnitModalView=true

    },
      OnDataPost(post_data){
     axios.get('api/postaddunit', {params: {data: post_data.employeeName}})
     if (this.modalOptions.mode==="edit unit")  axios.get('api/posteditunit', {params: {data: post_data.employeeName}})
    },
},





}
</script>
<style lang="sass" scoped>
.my-card
  width: 100%

</style>

