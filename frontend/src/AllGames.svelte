<script>

import { onMount } from 'svelte';

const url = 'http://localhost:8000/students/';
let data = [];

let columns = ["ID", "First Name", "Last Name", "Student ID"]
onMount(async () => {
    let response = await fetch(url, {mode:"cors"});
    data = await response.json();
    console.log(data)
});

</script>

<div class="overflow-x-auto">
    <table class="table w-full table-zebra">
        <thead>
            {#each columns as column}
                <th>{column}</th>
            {/each}
        </thead>
        <tbody>
            {#each data as column}
                <tr>
                    <td>{column.id}</td>
                    <td>{column.fname}</td>
                    <td>{column.lname}</td>
                    <td>{column.sid}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>