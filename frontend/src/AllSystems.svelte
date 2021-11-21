<script>

    import { onMount } from 'svelte';
    
    const url = 'http://localhost:8000/students/';
    let data = [];
    ////////////////////////////////////////////////////////////////////////////
    let columns = ["Product ID", "Product Name", "Product Description", "Price", "Specification 1", "Specification 1 Value", "Specification 2", "Specification 2 value", "Specification 3", "Specification 3 Value"]
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
                        <!-- -------------------------------------------------- -->
                        <td>{column.product_id}</td>
                        <td>{column.product_name}</td>
                        <td>{column.product_description}</td>
                        <td>{column.price}</td>
                        <td>{column.specification_name}</td>
                        <td>{column.specification_value}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>