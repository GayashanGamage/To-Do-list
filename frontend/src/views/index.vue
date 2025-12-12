<template>
    <!-- page content -->
    <div class="relative">
        <!-- header section -->
        <Menubar></Menubar>

        <!-- body content -->
        <div class="grid grid-cols-2 gap-6 w-full max-w-7xl mx-auto h-screen py-10">

            <!-- list new tasks -->
            <div class="flex flex-col gap-4 w-full h-fit bg-gray-100 p-6 rounded-md border-2 border-gray-200">
                <h2 class="font-semibold text-xl">Create new items</h2>
                <input type="text" class="border py-1 px-4 rounded-md border-gray-400 w-[75%]" placeholder="Title" v-model="title"> 
                <textarea name="" id="" class="border w-full py-1 px-4 rounded-md border-gray-400" placeholder="Description" v-model="description"></textarea>
                <button class="py-1 px-8 w-fit ml-auto rounded-md bg-black hover:bg-black/80 active:bg-black/80 text-white" @click="addTask">Add</button>
            </div>

            <!-- available todo list -->
            <div class="w-full h-full">
                
                <!-- tabs area -->
                <div class="grid grid-cols-2 gap-2">
                    <button class="py-2 rounded-l-md" :class="todoTab == true ? 'bg-black text-white' : 'bg-white text-black border'" @click="chnageTab('todo')">ToDo list</button>
                    <button class="py-2 rounded-r-md"  :class="todoTab == false ? 'bg-black text-white' : 'bg-white text-black border'" @click="chnageTab('compleated')">Compleated list</button>
                </div>

                <!-- to do list -->
                <div class=" w-full h-full p-10" v-if="todoTab">
                    
                    <!-- loading effect -->
                    <div class="w-full h-[10vh] border-2 border-gray-200 animate-pulse bg-gray-200/70 rounded-lg" v-if="loading"></div>
                    
                    <!-- not found message -->
                    <div class="" v-if="dataNotAvailable">
                        <h1 class="">No task available</h1>
                        <p class="">Still there are no any task available for To-Do</p>
                    </div>
    
                    <!-- error message -->
                    <div class="" v-if="errorMessage">
                        <h1 class="">Something go wrong</h1>
                        <p class="">Try again latter</p>
                    </div>
                    
                    <!-- todo list available -->
                    <div class="flex flex-col gap-4" v-if="dataAvailable">
                        <div class="flex flex-row" v-for="items in taskstore.newTask">
                            <p class="w-full">{{ items }}</p>
                            <button class="border" @click="compleateTask(items)">compleat</button>
                        </div>
                    </div>
                </div>

                <!-- compleated list -->
                <div class=" w-full h-full p-10" v-if="!todoTab">
                    <!-- loading effect -->
                    <div class="w-full h-[10vh] border-2 border-gray-200 animate-pulse bg-gray-200/70 rounded-lg" v-if="loading"></div>
                    
                    <!-- not found message -->
                    <div class="" v-if="dataAvailable">
                        <h1 class="">No task available</h1>
                        <p class="">Still there are no any task available for To-Do</p>
                    </div>
    
                    <!-- error message -->
                    <div class="" v-if="errorMessage">
                        <h1 class="">Something go wrong</h1>
                        <p class="">Try again latter</p>
                    </div>
                    
                    <!-- todo list available -->
                    <div class="flex flex-col gap-4" v-if="dataAvailable">
                        <div class="flex flex-row" v-for="items in taskstore.compleatedTasks">
                            <p class="w-full">{{ items }}</p>
                            <button class="border" @click="deleteTaks(items.id)">delete</button>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>

        <!-- floating message -->
        <Floatingmessage
            v-if="toastVisible"
            :toastMessage= ttile
            :toastDescription= tmessage
            :duration="3000"
            @closed="toastVisible = false"
        />
    </div>
</template>

<script setup>
import { onBeforeMount, ref } from 'vue';
import { useTaskStore } from '../stores/counter';
import Menubar from '@/components/menubar.vue';
import axios from 'axios';
import Floatingmessage from '@/components/floatingmessage.vue';

const taskstore = useTaskStore()

// UI management states
const loading = ref(false)
const dataAvailable = ref(false) 
const dataNotAvailable = ref(false) 
const errorMessage = ref(false)
const toastVisible = ref(false)
const todoTab = ref(true)

// input states
const title = ref(null)
const description = ref(null)

// toast messsage props
const ttile = ref(null)
const tmessage = ref(null)

const addTask = () => {
    axios.post(`${import.meta.env.VITE_API_URL}/tasks`, 
        {
            "title": title.value,
            "description": description.value
        }
    )
    .then((success) => {
        console.log(success.data)
        title.value = null
        description.value = null
        showToast('Successfull', 'New task added')
        getTask()
    })
    .catch((error) => {
        console.log(error.data)
    })
}

const getTask = () => {
    loading.value = true
    axios.get(`${import.meta.env.VITE_API_URL}/tasks/get`, 
        {
            params : {
                'completed' : false
            }
        }
    )
    .then((success) => {
        loading.value = false
        taskstore.newTask = success.data
        if(taskstore.newTask.length !== 0){
            dataAvailable.value = true
        }else if(taskstore.newTask.length == 0){
            dataNotAvailable.value = true
        }
    })
    .catch((error) => {
        loading.value = false
        errorMessage.value = true
    })
}
const getCompleatedTask = () => {
    loading.value = true
    axios.get(`${import.meta.env.VITE_API_URL}/tasks/get`, 
        {
            params : {
                'completed' : true
            }
        }
    )
    .then((success) => {
        loading.value = false
        taskstore.compleatedTasks = success.data
        if(taskstore.compleatedTasks.length !== 0){
            dataAvailable.value = true
        }else if(taskstore.compleatedTasks.length == 0){
            dataNotAvailable.value = true
        }
    })
    .catch((error) => {
        loading.value = false
        errorMessage.value = true
    })
}

const compleateTask = (task) => {
    axios.patch(`${import.meta.env.VITE_API_URL}/tasks/update/${parseInt(task.id)}`, 
        {
            "title": task.title,
            "description": task.description,
            "completed": !task.completed
        }
    )
    .then((success) => {
        showToast('Successfull', 'task compleated')
        getTask()
    })
    .catch((error) => {
        showToast('Error', 'Something go wrong. try again')
    })
}

const deleteTaks = (id) => {
    console.log(id)
    axios.delete(`${import.meta.env.VITE_API_URL}/tasks/remove/${id}`)
    .then((success) => {
        showToast('Deleted', 'compleated task deleted')
        getCompleatedTask()
    })
    .catch((error) => {
        console.log('execute three')
        showToast('Error', 'Something go wrong. try again')
    })
}

const showToast = (title, description) => {
    ttile.value = title
    tmessage.value = description
    toastVisible.value = true
    setTimeout(() => {
        ttile.value = null
        tmessage.value = null
    },3000)
}

const chnageTab = (val) => {
    if(val == 'todo'){
        todoTab.value = true
    }else if(val == 'compleated'){
        todoTab.value = false
        getCompleatedTask()
    }
}

onBeforeMount(() => {
    getTask()
})

</script>