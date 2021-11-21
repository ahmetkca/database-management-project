<script>

    import { onMount } from 'svelte';
    
    const url = 'http://localhost:8000/employees/';
    let data = [];
    
    let columns = ["Employee", "SSN", "Email", "Gender", "Date of Birth", "Address", "Phone Number", "Work Place (Store ID)"]
    onMount(async () => {
        let response = await fetch(url, {mode:"cors"});
        data = await response.json();
        console.log(data)
    });
    

    import { randomInt } from "./utils.js";
    let counter = randomInt();

    function randomize(number){
        number = randomInt();
        return number
    }
    

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
            <td>
                <div class="flex items-center space-x-3">
                <div class="avatar">
                    <div class="w-12 h-12 mask mask-squircle">
                    <img src="https://picsum.photos/300/200?random={randomize(counter)}" alt="?">
                    </div>
                </div> 
                <div>
                    <div class="font-bold">
                        {column.first_name} {column.last_name}
                        </div> 
                    <div class="text-sm opacity-50">
                        Employee ID: {column.employee_id}
                        </div>
                </div>
                </div>

                <td>{column.ssn}</td>
                <td>{column.email}</td>
                <td>{column.gender}</td>
                <td>{column.date_of_birth}</td>
                <td>{column.address}</td>
                <td>{column.phone_number}</td>
                <td>{column.work_place}</td>
            
            </tr>
        {/each}


      </tbody> 
    </table>

    <button class="btn btn-wide btn-lg" on:click={() => push('/employees')}>View Current Employees</button> 
</div>
