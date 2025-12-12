<template>
    <div class="w-full bg-blue-600">
        <div class="flex flex-row justify-between w-full max-w-7xl mx-auto py-4 text-white">
            <RouterLink to="/">
                <div class="flex flex-col gap-2">
                    <div class="flex flex-row items-center gap-2">
                        <span class="material-icons text-blue-300">add_task</span>
                        <h1 class="font-black text-3xl">TODO List</h1>
                    </div>
                    <p class="font-bold text-sm">Stay organize and get things done</p>
                </div>
            </RouterLink>
            <!-- <RouterLink to="/user">
                <button class="border">User</button>
            </RouterLink> -->
        </div>
    </div>
</template>

<script setup></script>
