<template>
  <div>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>

    <h1>UserView</h1>
    <h2>{{ userId }}번 User의 페이지</h2>

    <button @click="goHome">Home</button>

    <button @click="routeUpdate">100번 유저의 페이지</button>

    <!-- 중첩 라우트의 컴포넌트가 렌더링 -->
    <RouterView />
  </div>


</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useRoute, useRouter } from 'vue-router'
// Leave : 페이지 떠날때 실행되는 가드
// Update : 페이지 url 변경될때 실행되는 가드
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()

const router = useRouter()

const userId = ref(route.params.id)

const goHome = function() {

  // router.push() : 이전 페이지로 돌아갈수 있음(히스토리에 추가) // A -> B -> C
  // router.replace() : 이전 페이지로 돌아갈수 없음(히스토리에 추가 X) // A -> B -> C
  router.replace({ name: 'home' })
}

const routeUpdate = function () {
  router.push({ name:'user', params: {id: 100} })
}

onBeforeRouteLeave((to, from) => {
  //confirm : 사용자에게 묻기
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false // 아니요 --> 페이지 이동 false
  }
})
// from : 1번, to : 100번
onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})

</script>

<style scoped>


</style>