<script>
    import backdrop from './assets/gradient-background.jpg'
    import gamesBackdrop from './assets/games.png'
    import games from './assets/games2.png'
    import logo from './assets/GameStartLogo.png'
    import systems from './assets/systems.jpg'
    import systemsBackdrop from './assets/systems2.jpg'
    import monitorsBackdrop from './assets/monitors.png'
    import monitors from './assets/monitors2.jpg'
    import headsetsBackdrop from './assets/headsets.jpg'
    import headsets from './assets/headsets2.jpg'
    import chargersBackdrop from './assets/chargers.jpg'
    import chargers from './assets/chargers2.jpg'
    import hoodiesBackdrop from './assets/hoodies.jpg'
    import hoodies from './assets/hoodies2.jpg'

    import {push, pop, replace} from 'svelte-spa-router'

</script>


<body>

    <!-- Hero Logo -->  
    <div class="hero min-h-screen" style="background-image: url({backdrop});">
        <div class="flex-col hero-content lg:flex-row-reverse">
        <img alt="?" src={logo} class="max-w-sm rounded-lg shadow-2xl"> 
        <div>
            <h1 class="mb-5 text-5xl font-bold">
                Welcome to Your GameStart <br> Management System
                </h1> 
            <p class="mb-5">
                The management system for the world's largest retailer of video game products and PC entertainment software. We sell new and used video game hardware, video game software and accessories, as well as PC entertainment software, and related accessories and other merchandise.
                </p> 
        </div>
        </div>
    </div>
    <!-- Hero Logo -->  


    <!-- Games -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card bg-base-200" style="background-image: url({gamesBackdrop});">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={games} class="rounded-lg shadow-lg" style="width: 300px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Games</h2> 
            <p>Search for and view video games of your choice. GameStart is the home for all your top games from the most well known developers.</p> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/allgames')}>View All Games</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Games -->


    <!-- Systems -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card bg-base-200" style="background-image: url({systemsBackdrop});">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={systems} class="rounded-lg shadow-lg" style="width: 700px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Systems</h2> 
            <p>Search for and view gaming systems of your choice. GameStart is the home for all your top gaming systems from the most well known manufacturers.</p> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/allsystems')}>View All Systems</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Systems -->


    <!-- Monitors -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card bg-base-200" style="background-image: url({monitorsBackdrop});">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={monitors} class="rounded-lg shadow-lg" style="width: 700px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Monitors</h2> 
            <p>Search for and view monitors of your choice. GameStart is the home for all your top gaming monitors from the most well known brands.</p> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/allmonitors')}>View All Monitors</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Monitors -->


    <!-- Headset -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card bg-base-200" style="background-image: url({headsetsBackdrop});">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={headsets} class="rounded-lg shadow-lg" style="width: 300px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Headsets</h2> 
            <p>Search for and view headsets of your choice. GameStart is the home for all your top gaming headsets from the most well known makers.</p> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/allheadsets')}>View All Headsets</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Headset -->


    <!-- Chargers -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card bg-base-200" style="background-image: url({chargersBackdrop});">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={chargers} class="rounded-lg shadow-lg" style="width: 700px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Chargers</h2> 
            <p>Search for and view chargers of your choice. GameStart is the home for all your top chargers from the most well known manufacturers.</p> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/allchargers')}>View All Chargers</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Chargers -->


    <!-- Hoodies -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card bg-base-200" style="background-image: url({hoodiesBackdrop});">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={hoodies} class="rounded-lg shadow-lg" style="width: 700px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Hoodies</h2> 
            <p>Search for and view hoodies of your choice. GameStart is the home for all your top hoodies from the most well known brands.</p> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/allhoodies')}>View All Hoodies</button>
            </div>
        </div>
        </div>
    </div>
    <!-- Hoodies -->



</body>
