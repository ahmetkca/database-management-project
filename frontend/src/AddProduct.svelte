<script>
    import backdrop from './assets/gradient-background.jpg'
    import games from './assets/games2.png'
    import systems from './assets/systems.jpg'
    import monitors from './assets/monitors2.jpg'
    import headsets from './assets/headsets2.jpg'
    import chargers from './assets/chargers2.jpg'
    import hoodies from './assets/hoodies2.jpg'

    import {push, pop, replace} from 'svelte-spa-router'

</script>

<body style="background-image: url({backdrop}); background-size: 100% 100%;"> 
    <!-- Games -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={games} class="rounded-lg shadow-lg" style="width: 300px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Games</h2> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/addgame')}>Add a Game</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Games -->


    <!-- Systems -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={systems} class="rounded-lg shadow-lg" style="width: 700px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Systems</h2> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/addsystem')}>Add a System</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Systems -->


    <!-- Monitors -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={monitors} class="rounded-lg shadow-lg" style="width: 700px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Monitors</h2> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/addmonitor')}>Add a Monitor</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Monitors -->


    <!-- Headset -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={headsets} class="rounded-lg shadow-lg" style="width: 300px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Headsets</h2> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/addheadset')}>Add a Headset</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Headset -->


    <!-- Chargers -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={chargers} class="rounded-lg shadow-lg" style="width: 700px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Chargers</h2> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/addcharger')}>Add a Charger</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Chargers -->


    <!-- Hoodies -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={hoodies} class="rounded-lg shadow-lg" style="width: 700px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Hoodies</h2> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/addhoodie')}>Add a Hoodie</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Hoodies -->



</body>