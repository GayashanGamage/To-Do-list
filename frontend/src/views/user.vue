<template>
    <div class="">
        <Menubar></Menubar>
        
        <div class="w-full h-screen flex flex-col mt-[20vh]">
            <!-- signin & signup -->
            <div class="flex flex-col gap-4 border max-w-lg w-full p-10 mx-auto rounded-md">
                <!-- title section -->
                <div class="grid grid-cols-2 gap-2">
                    <button class="border py-1 rounded-md" @click="authOption('signin')">SignIn</button>
                    <button class="border py-1 rounded-md" @click="authOption('signup')">SignUp</button>
                </div>
    
                <div class="flex flex-col gap-6">
                    <!-- sign in section-->
                    <div class="flex flex-col gap-2" v-if="signIn">
                        <div class="flex flex-row gap-2">
                            <div class="flex flex-col gap-1">
                                <label for="firstName" class="">First Name</label>
                                <input type="text" class="border w-full" id="firstName">
                            </div>
                            <div class="flex flex-col gap-1">
                                <label for="lastName" class="">Last Name</label>
                                <input type="text" class="border w-full" id="lastName">
                            </div>
                        </div>
                        <div class="flex flex-col gap-1">
                            <label for="email" class="">Email address</label>
                            <input type="text" class="border" id="email">
                        </div>
                        <div class="flex flex-col gap-1">
                            <label for="passwordOne" class="">Password</label>
                            <input type="password" class="border" id="passwordOne">
                        </div>
                        <div class="flex flex-col gap-1">
                            <label for="passwordTwo" class="">Password</label>
                            <input type="text" class="border" id="passwordTwo">
                        </div>
                        
                        <!-- action button -->
                        <button class="border py-1 w-full rounded-md my-4" @click="createAccount">Create account</button>
                    </div>
                    
                    <!-- sign up section-->
                    <div class="py-10" v-if="!signIn">
                        <div class="flex flex-col gap-1">
                            <label for="email" class="">Email address</label>
                            <input type="text" class="border" id="email">
                        </div>
                        <div class="flex flex-col gap-1">
                            <label for="passwordOne" class="">Password</label>
                            <input type="password" class="border" id="passwordOne">
                        </div>

                        <!-- action button -->
                        <button class="border py-1 w-full rounded-md my-4" @click="login">Loging</button>
                    </div>
                </div>
    
            </div>
        </div>
    </div>
</template>

<script setup>
import Menubar from '@/components/menubar.vue';
import axios from 'axios';
import { ref } from 'vue';

const signIn = ref(false)

const authOption = (option) => {

    if(option == 'signin'){
        signIn.value = true
    }else if(option == 'signup'){
        signIn.value = false
    }
}

const createAccount = () => {
    axios.post()
    .then()
    .catch()
}

const login = () => {
    axios.get()
    .then()
    .catch()
}

</script>