<script>

    import { onMount } from 'svelte';
    
    const url = 'http://localhost:8000/products/';
    let data = [];
    
    let columns = ["Product ID", "Product Type", "Product Name", " ", " ", " ", "Product Description", "Product Price"]
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
                        <td>{column.product_type.product_type_name}</td>
                        <td>{column.product_name}</td>

                        <td>
                            <div>
                                <div class="font-bold">
                                    {column.spec1.product_specification_value}
                                </div> 
                                <div class="text-sm opacity-50">
                                    {column.spec1.product_specification_name}
                                </div>
                            </div>
                        </td>

                        <td>
                            <div>
                                <div class="font-bold">
                                    {column.spec2.product_specification_value}
                                </div> 
                                <div class="text-sm opacity-50">
                                    {column.spec2.product_specification_name}
                                </div>
                            </div>
                        </td>

                        <td>
                            <div>
                                <div class="font-bold">
                                    {column.spec3.product_specification_value}
                                </div> 
                                <div class="text-sm opacity-50">
                                    {column.spec3.product_specification_name}
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

        <button class="btn btn-wide btn-lg" on:click={() => push('/addproduct')}>Add Product</button> 
</div>
