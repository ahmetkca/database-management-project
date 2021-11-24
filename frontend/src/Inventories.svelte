<script>

    import { onMount } from 'svelte';
    
    const url = 'http://localhost:8000/inventories/';
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
    
   

<body style="background-image: url({backdrop}); background-size: 100% 100%;">
    {#each data as column}
        <div class="flex items-center w-full px-4 py-10 bg-cover card">
            <div class="card glass lg:card-side text-neutral-content">
            <figure class="p-6">
                <img alt="?" src="https://picsum.photos/300/200?random={randomize(counter)}" class="rounded-lg shadow-lg">
            </figure> 
            <div class="max-w-md card-body">
                <h2 class="card-title">Inventory ID {column.inventory_id}</h2> 
                <h2><b>Contained Within Store with ID: </b></h2><p>{column.fk_building.store_id}</p> 
            </div>
            </div>
        </div>
    {/each}
</body>