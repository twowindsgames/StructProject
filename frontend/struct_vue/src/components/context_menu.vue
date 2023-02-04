<template>

      <q-menu transition-duration="0"
        touch-position
        context-menu>

        <q-list dense style="min-width: 100px">

           <q-item v-show="readyToDelete" clickable v-close-popup >
            <q-item-section @click="DeleteNode" > Подтвердить удаление</q-item-section>
          </q-item>
          <q-item  v-show="!readyToDelete" clickable  v-close-popup  @click="OpenMenu" >
            <q-item-section  @click="ReadyToDeleteNode"  >Удалить</q-item-section>
          </q-item>



          <q-separator />
          <q-item clickable>
            <q-item-section>Редактировать</q-item-section>
            <q-item-section side>
              <q-icon name="keyboard_arrow_right" />
            </q-item-section>

            <q-menu anchor="top end" self="top start">
              <q-list>
                <q-item clickable v-close-popup>
                   <q-item-section>Изменить данные </q-item-section>
                </q-item>
                <q-item clickable v-close-popup>
                   <q-item-section>Добавить подчиненное подрзделение </q-item-section>
                </q-item>
              </q-list>
            </q-menu>

          </q-item>
          <q-separator />
          <q-item clickable v-close-popup>
            <q-item-section>Закрыть</q-item-section>
          </q-item>
        </q-list>

      </q-menu>


</template>

<script>



import axios from "axios";

export default {
  name: "context_menu",
  props: [ 'group_id', "readyToDelete"],
  setup () {


    return {
        OpenMenu(){

        }

    }
  },
  mounted() {

  },


  methods: {
       ReadyToDeleteNode() {
       this.$emit('clickToDelete')

},
       DeleteNode() {
       axios.get('api/delete', {params: {groupId: this.group_id}})

}
  }
}
</script>

<style scoped>


</style>