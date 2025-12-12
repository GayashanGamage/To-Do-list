<!-- <template>
    <div class="border p-3 rounded-xl w-fit h-fit absolute right-5 bottom-5">
        <h1 class="">{{ toastMessage }}</h1>
        <p class="">{{ toastDescription }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
    toastMessage : String,
    toastDescription : String
})

const hideFloatingMessage = () => {
    setTimeout(() => {
    toastVisible.value = false
  }, 4000)
}

</script> -->

<template>
  <div
    v-if="visible"
    class="fixed bottom-5 right-5 max-w-sm w-full bg-white border border-gray-200 rounded-xl shadow-lg p-4 transition-all duration-300 ease-out"
    :class="visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4 pointer-events-none'"
  >
    <h1 class="text-lg font-semibold text-gray-900">{{ toastMessage }}</h1>
    <p class="text-sm text-gray-600 mt-1">{{ toastDescription }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

// Props to customize the message
const props = defineProps({
  toastMessage: {
    type: String,
    default: 'Notification'
  },
  toastDescription: {
    type: String,
    default: 'This is a floating message.'
  },
  duration: {
    type: Number,
    default: 3000 // 3 seconds
  } 
})

// Emits when the toast is closed
const emit = defineEmits(['closed'])

const visible = ref(false)
let timeoutId = null

// Show the toast
const show = () => {
  visible.value = true
  
  // Clear any existing timeout
  if (timeoutId) clearTimeout(timeoutId)
  
  // Auto hide after duration
  timeoutId = setTimeout(() => {
    hide()
  }, props.duration)
}

// Hide with animation
const hide = () => {
  visible.value = false
  setTimeout(() => {
    emit('closed')
  }, 300) // Wait for fade-out animation to complete
}

// Expose show method so parent can trigger it
defineExpose({ show })

// Auto-show on mount (optional - remove if you want manual control only)
onMounted(() => {
  show()
})

// Watch for prop changes (useful if reusing the component)
watch(() => [props.title, props.message], () => {
  if (visible.value) {
    show() // Restart timer if content changes
  }
})
</script>