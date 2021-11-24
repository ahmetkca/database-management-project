<script>

    import { onMount } from 'svelte';
    
    const url = 'http://localhost:8000/view12/';
    let data = [];
    
    let columns = ["Product ID", "Headset Name", " ", " ", " ", "Headset Description", "Headset Price"]
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
                        <td>{column.product_id}</td>
                        <td>{column.product_name}</td>
                        
                        <td>
                            <div>
                                <div class="font-bold">
                                    {column.spec1_value}
                                </div> 
                                <div class="text-sm opacity-50">
                                    {column.spec1_name}
                                </div>
                            </div>
                        </td>

                        <td>
                            <div>
                                <div class="font-bold">
                                    {column.spec2_value}
                                </div> 
                                <div class="text-sm opacity-50">
                                    {column.spec2_name}
                                </div>
                            </div>
                        </td>

                        <td>
                            <div>
                                <div class="font-bold">
                                    {column.spec3_value}
                                </div> 
                                <div class="text-sm opacity-50">
                                    {column.spec3_name}
                                </div>
                            </div>
                        </td>

                        <div class="collapse w-96 border rounded-box border-base-300 collapse-arrow">
                            <input type="checkbox"> 
                            <div class="collapse-title text-s font-small">
                              click
                            </div> 
                            <div class="collapse-content"> 
                              <p>{column.product_description}
                              </p>
                            </div>
                        </div>

                        <td>${column.price}</td><br><br>

                    </tr>
                {/each}
            </tbody>
        </table>

        <button class="btn btn-wide btn-lg" on:click={() => push('/')}>Go Back</button> <br><br>
</div>
