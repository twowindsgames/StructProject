<template>

      <q-menu transition-duration="0"
        touch-position
        context-menu>

        <q-list dense style="min-width: 100px">

           <q-item v-show="readyToDelete" clickable v-close-popup >
            <q-item-section @click="$emit('Delete')"> Подтвердить удаление</q-item-section>
          </q-item>
          <q-item  v-show="!readyToDelete" clickable  v-close-popup  @click="OpenMenu" >
            <q-item-section  @click="$emit('ReadyDelete')"  >Удалить</q-item-section>
          </q-item>



          <q-separator />
          <q-item clickable>
            <q-item-section>Редактировать</q-item-section>
            <q-item-section side>
              <q-icon name="keyboard_arrow_right" />
            </q-item-section>

            <q-menu anchor="top end" self="top start">
              <q-list>
                <q-item clickable v-close-popup @click="$emit('ShowEditTree','edit node')">
                   <q-item-section>Изменить информацию о подразделении </q-item-section>
                </q-item>
                <q-item clickable v-close-popup @click="$emit('ShowEditTree','add node')">
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




export default {
  name: "context_menu",
  props: [ 'group', "readyToDelete"],



  methods: {
    showModal() {
      this.modalVisible = true;
    },





}
  }

</script>

<style scoped>


</style>