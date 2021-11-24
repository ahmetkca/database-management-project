<script>

    import { onMount } from 'svelte';
    
    const url = 'http://localhost:8000/customers/';
    let data = [];
    
    let columns = ["Customer ID", "First Name", "Middle Name", "Last Name", "Date of Birth",  "Gender",  "Email", "Shipping Address", "Phone Number"]
    onMount(async () => {
        let response = await fetch(url, {mode:"cors"});
        data = await response.json();
        console.log(data)
    });


    import {push, pop, replace} from 'svelte-spa-router';

    
</script>
    
<div class="overflow-x-auto" style="text-align: center;">
        <table class="table w-full table-zebra">
            <thead>
                {#each columns as column}
                    <th>{column}</th>
                {/each}
            </thead>
            <tbody>
                {#each data as column}
                    <tr>
                        <td>{column.customer_id}</td>
                        <td>{column.first_name}</td>
                        <td>{column.middle_name}</td>
                        <td>{column.last_name}</td>
                        <td>{column.date_of_birth}</td>
                        <td>{column.gender}</td>
                        <td>{column.email}</td>
                        <td>{column.shipping_address}</td>
                        <td>{column.phone_number}</td>
                    </tr>
                {/each}
            </tbody>
        </table>

    
    <button class="btn btn-wide btn-lg" on:click={() => push('/view4')}>View Customer Orders</button> <br><br>
    <button class="btn btn-wide btn-lg" on:click={() => push('/addcustomer')}>Add New Customer</button> 
</div>
