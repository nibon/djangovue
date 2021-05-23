<template>
  <div id="app">
    <h1>Appname: {{ ssr.appName }}</h1>
    <h2>Counter: {{ counter }}</h2>
    <button class="btn btn-danger" @click="counter++">+1</button>
    <button class="btn btn-success" @click="counter--">-1</button>
  </div>
</template>

<script>
export default {
  name: 'app1',
  data () {
    return {
      counter: 1,
      /*global ssr:true*/
      ssr: {...ssr},
    }
  }
}
</script>

