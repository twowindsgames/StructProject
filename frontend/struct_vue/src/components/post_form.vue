<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md column" style="min-width: 400px " >

      <q-input outlined v-model="post_data.full_title" placeholder="Управление информационного обеспечения" hint="Полное название подразделения"  />
      <q-input outlined v-model="post_data.title" placeholder="УИО" hint="Краткое название подразделения"  />

      <div>
        <q-btn label="Добавить"  color="primary" @click="PostData" v-close-popup/>
      </div>
    </div>


  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  props: ['mode'],
  data () {
    return {
      post_data:[
           {full_title: ref('')},
           { title: ref(''),}
      ],


    }
  },
  methods:{
    PostData(){
       this.$emit('DataPost', this.post_data)
    }

  }
}
</script>