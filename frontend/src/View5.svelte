<script>

    import { onMount } from 'svelte';
    
    const url = 'http://localhost:8000/view5/';
    let data = [];
    
    let columns = ["First Name", "Last Name", "Gender", "Works / Worked at Store with ID:", "Date of Birth"]
    onMount(async () => {
        let response = await fetch(url, {mode:"cors"});
        data = await response.json();
        console.log(data)
    });

    import {push, pop, replace} from 'svelte-spa-router';

</script>
    
<div class="overflow-x-auto" style="text-align: center;">
        <table class="table w-full">
            <thead>
                {#each columns as column}
                    <th>{column}</th>
                {/each}
            </thead>
            <tbody>
                {#each data as column}
                    <tr>
                        
                        <td>{column.first_name}</td>
                        <td>{column.last_name}</td>
                        <td>{column.gender}</td>
                        <td>{column.work_place_id}</td>
                        <td>{column.date_of_birth}</td>

                    </tr>
                {/each}
            </tbody>
        </table>

        <button class="btn btn-wide btn-lg" on:click={() => push('/funfacts')}>Go Back</button> <br><br>
</div>
