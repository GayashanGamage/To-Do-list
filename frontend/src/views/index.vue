<template>
    <!-- page content -->
    <div class="relative">
        <!-- header section -->
        <Menubar></Menubar>

        <!-- body content -->
        <div class="grid grid-cols-2 gap-6 w-full max-w-7xl mx-auto h-screen py-10">

            <!-- list new tasks -->
            <div class="flex flex-col gap-4 w-full h-fit bg-blue-50/60 p-6 rounded-md border-2 border-gray-200">
                <h2 class="font-semibold text-xl">Create new items</h2>
                <input type="text" class="border py-1 px-4 rounded-md border-gray-300 w-[75%] bg-white" placeholder="Title" v-model="title"> 
                <textarea name="" id="" class="border w-full py-1 px-4 rounded-md border-gray-300 bg-white" placeholder="Description" v-model="description"></textarea>
                <button class="flex flex-row justify-center items-center gap-2 py-1 px-8 w-fit ml-auto rounded-md bg-blue-600 hover:bg-blue-600/80 active:bg-blue-600/70 text-white" @click="addTask">
                    <span class="material-icons text-white">add</span>
                    Add
                </button>
            </div>

            <!-- available todo list -->
            <div class="flex flex-col gap-10 w-full h-full bg-blue-50/60 p-6 rounded-md border-2 border-gray-200">
                
                <!-- tabs area -->
                <div class="grid grid-cols-2 gap-2">
                    <button class="flex flex-row justify-center items-center gap-2 py-2 rounded-l-md" :class="todoTab == true ? 'bg-blue-600 text-white' : 'bg-white text-blue-600 border'" @click="chnageTab('todo')">
                        <span class="material-icons text-white">list</span>
                        ToDo list
                    </button>
                    <button class="flex flex-row justify-center items-center gap-2 py-2 rounded-r-md"  :class="todoTab == false ? 'bg-blue-600 text-white' : 'bg-white text-blue-600 border'" @click="chnageTab('compleated')">
                        <span class="material-icons text-white" :class="todoTab == false ? 'text-blue-600' : 'text-white'">check_circle</span>
                        Compleated list
                    </button>
                </div>

                <!-- to do list -->
                <div class=" w-full h-full" v-if="todoTab">
                    
                    <!-- not found message -->
                    <div class="flex flex-col gap-2" v-if="dataNotAvailable">
                        <div class="flex felx-row gap-4 items-center">
                            <span class="material-icons text-red-300">warning</span>
                            <h1 class="font-black text-2xl">No task available</h1>
                        </div>
                        <p class="text-lg font-light">Still there are no any task available for To-Do</p>
                    </div>
    
                    <!-- error message -->
                    <div class="" v-if="errorMessage">
                        <h1 class="">Something go wrong</h1>
                        <p class="">Try again latter</p>
                    </div>
                    
                    <!-- todo list available -->
                    <div class="flex flex-col gap-4" v-if="dataAvailable">
                        <div class="flex flex-row bg-white p-6 rounded-md" v-for="items in taskstore.newTask">
                            <div class="">
                                <div class="">
                                    <h5 class="font-semibold text-gray-400 text-xs">Title</h5>
                                    <p class="text-lg">{{ items.title }}</p>
                                </div>
                                <div class="">
                                    <h5 class="font-semibold text-gray-400 text-xs">Description</h5>
                                    <p class="text-lg">{{ items.description }}</p>
                                </div>
                                <div class="">
                                    <h5 class="font-semibold text-gray-400 text-xs">Created at</h5>
                                    <p>{{ new Date(items.created_at).getFullYear() }}-{{ String(new Date(items.created_at).getMonth()).padStart(2, '0') }}-{{ String(new Date(items.created_at).getDate()).padStart(2, '0') }}</p>
                                </div>
                            </div>
                            <button class="flex flex-row justify-center items-center gap-2 py-1 px-8 w-fit ml-auto rounded-md bg-blue-600 hover:bg-blue-600/80 active:bg-blue-600/70 text-white h-fit mt-auto" @click="compleateTask(items)">compleat</button>
                        </div>
                    </div>
                </div>

                <!-- compleated list -->
                <div class=" w-full h-full" v-if="!todoTab">
                    
                    <!-- not found message -->
                    <div class="flex flex-col gap-2" v-if="dataNotAvailable">
                        <div class="flex felx-row gap-4 items-center">
                            <span class="material-icons text-red-300">warning</span>
                            <h1 class="font-black text-2xl">No compleated tasks available</h1>
                        </div>
                        <p class="text-lg font-light">Still there are no any task available for To-Do</p>
                    </div>
    
                    <!-- error message -->
                    <div class="" v-if="errorMessage">
                        <h1 class="">Something go wrong</h1>
                        <p class="">Try again latter</p>
                    </div>
                    
                    <!-- todo list available -->
                    <div class="flex flex-col gap-4" v-if="dataAvailable">
                        <div class="flex flex-row bg-white p-6 rounded-md" v-for="items in taskstore.compleatedTasks">
                            <div class="">
                                <div class="">
                                    <h5 class="font-semibold text-gray-400 text-xs">Title</h5>
                                    <p class="text-lg">{{ items.title }}</p>
                                </div>
                                <div class="">
                                    <h5 class="font-semibold text-gray-400 text-xs">Description</h5>
                                    <p class="text-lg">{{ items.description }}</p>
                                </div>
                                <div class="">
                                    <h5 class="font-semibold text-gray-400 text-xs">Created at</h5>
                                    <p>{{ new Date(items.created_at).getFullYear() }}-{{ String(new Date(items.created_at).getMonth()).padStart(2, '0') }}-{{ String(new Date(items.created_at).getDate()).padStart(2, '0') }}</p>
                                </div>
                            </div>
                            <button class="flex flex-row justify-center items-center gap-2 py-1 px-8 w-fit ml-auto rounded-md bg-red-400 hover:bg-red-400/80 active:bg-red-400/70 text-white h-fit mt-auto" @click="deleteTaks(items.id)">delete</button>
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
    // loading.value = true
    axios.get(`${import.meta.env.VITE_API_URL}/tasks/get`, 
        {
            params : {
                'completed' : false
            }
        }
    )
    .then((success) => {
        taskstore.newTask = success.data
        if(taskstore.newTask.length !== 0){
            dataAvailable.value = true
        }else if(taskstore.newTask.length == 0){
            dataNotAvailable.value = true
        }
    })
    .catch((error) => {
        errorMessage.value = true
    })
}
const getCompleatedTask = () => {
    axios.get(`${import.meta.env.VITE_API_URL}/tasks/get`, 
        {
            params : {
                'completed' : true
            }
        }
    )
    .then((success) => {
        taskstore.compleatedTasks = success.data
        if(taskstore.compleatedTasks.length !== 0){
            dataAvailable.value = true
        }else if(taskstore.compleatedTasks.length == 0){
            dataNotAvailable.value = true
        }
    })
    .catch((error) => {
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
    dataAvailable.value = false
    dataNotAvailable.value = false
    errorMessage.value = false

    if(val == 'todo'){
        todoTab.value = true
        getTask()
    }else if(val == 'compleated'){
        todoTab.value = false
        getCompleatedTask()
    }
}

onBeforeMount(() => {
    getTask()
})

</script>