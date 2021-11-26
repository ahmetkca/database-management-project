<script>

    import { onMount } from 'svelte';
    import {push, pop, replace} from 'svelte-spa-router';
    
    const url = 'http://localhost:8000/view3/';
    let data = [];
    
    onMount(async () => {
        let response = await fetch(url, {mode:"cors"});
        data = await response.json();
        console.log(data)
    });
    

    import { randomInt } from "./utils.js";
    import backdrop from './assets/gradient-background.jpg'
    let counter = randomInt();

    function randomize(number){
        number = randomInt();
        return number
    }
</script>
    
   

<body style="background-image: url({backdrop}); background-size: 100% 100%; text-align: center;">
    {#each data as column}
        <div class="flex items-center w-full px-4 py-10 bg-cover card">
            <div class="card glass lg:card-side text-neutral-content">
            <figure class="p-6">
                <img alt="?" src="https://picsum.photos/300/200?random={randomize(counter)}" class="rounded-lg shadow-lg">
            </figure> 
            <div class="max-w-md card-body">
                <h2 class="card-title">{column.first_name} {column.last_name}</h2> 
                <h2><b>Oldest Employee in Store with ID: </b></h2><p>{column.work_place}</p> 
                <h2><b>Date of Birth: </b></h2><p>{column.date_of_birth}</p> 
            </div>
            </div>
        </div>
    {/each}

    <button class="btn btn-wide btn-lg" on:click={() => push('/funfacts')}>Go Back</button> 
</body>