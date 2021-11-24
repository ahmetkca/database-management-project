<script>
    import backdrop from './assets/gradient-background.jpg'
    import {push, pop, replace} from 'svelte-spa-router'

    import oldest from './assets/view3.png'
    import millenium from './assets/view5.jpg'

</script>

<body style="background-image: url({backdrop}); background-size: 100% 100%;"> 
    
    <!-- View 3 -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={oldest} class="rounded-lg shadow-lg" style="width: 300px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Who is the Oldest Employee in Each Store?</h2> 
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/view3')}>Click to View</button>
            </div>
        </div>
        </div>
    </div>
    <!-- View 3 -->

    <!-- View 5 -->  
    <div class="flex items-center w-full px-4 py-10 bg-cover card">
        <div class="card glass lg:card-side text-neutral-content">
        <figure class="p-6">
            <img alt="?" src={millenium} class="rounded-lg shadow-lg" style="width: 300px; height: 337px; object-fit: cover;">
        </figure> 
        <div class="max-w-md card-body">
            <h2 class="card-title">Millenium Showdown</h2> 
            <h2>Who are the current employees born after 2000 and the fired employees born before 2000?</h2>
            <div class="card-actions">
            <button class="btn glass rounded-full" on:click={() => push('/view5')}>Click to View</button>
            </div>
        </div>
        </div>
    </div>
    <!-- View 5 -->

</body>