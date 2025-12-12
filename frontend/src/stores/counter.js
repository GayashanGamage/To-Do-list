import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useTaskStore = defineStore('task', () => {
  const newTask = ref([
    'Sample Task 1',
    'Sample Task 2',
    'Sample Task 3',
  ])
  const compleatedTasks = ref([])

  return { newTask, compleatedTasks }
})
