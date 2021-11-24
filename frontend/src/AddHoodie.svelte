<script>

    import {push, pop, replace} from 'svelte-spa-router';
    import { onMount } from 'svelte';

    let product_name = ''
	let price = ''
    let product_description = ''
    let product_type = 2
    let spec1 = null
    let spec2 = null
    let spec3 = null
    
    const url = 'http://localhost:8000/product-types/';
    let data = [];
    let typedata = {};
    let specifications = [];
    let specdata = [];
    let temp = [];
    let spectypes = [];

    onMount(async () => {
        let response = await fetch(url, {mode:"cors"});
        data = await response.json();

        data.forEach(function(element){
            if(element.product_type_id == product_type){
                typedata = element
            }
        });

        specifications = typedata.specifications
        
        specifications.forEach(function(element){
            
            let tempdict = {}
            let templist = [];

            templist = element.split(',');
            tempdict.spec_id = templist[0]
            tempdict.spec_type = templist[1]
            temp.push(templist[1])
            tempdict.spec_value = templist[2]
            
            specdata = [...specdata, tempdict];

        });

        spectypes = [...new Set(temp)];

    });




	let result = null

	async function doPost () {

		const res = await fetch('http://localhost:8000/products/', {
			method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
			body: JSON.stringify({
				product_name,
                price,
                product_description,
                "product_type_id": product_type,
                "spec1_id": spec1,
                "spec2_id": spec2,
                "spec3_id": spec3
			})
		})

        if (res.ok){
            confirm("Hoodie Added Successfully!")
            push('/view1')
        }
        else{
            alert("There was an error")
        }

		const json = await res.json()
		result = JSON.stringify(json)
	}

</script>


<div style="text-align: center;">
    
    <label>Hoodie Name</label>
    <input type="text" class="input input-bordered" bind:value={product_name} />

    <label>Price</label>
    <input type="text" class="input input-bordered" bind:value={price} />

    <label>{spectypes[0]}</label>
    <select class="select select-bordered w-full max-w-xs" bind:value={spec1}>
        {#each specdata as specification}
            {#if specification.spec_type == spectypes[0]}
                <option value="{specification.spec_id}">{specification.spec_value}</option>
            {/if}
        {/each}
    </select>

    <label>{spectypes[1]}</label>
    <select class="select select-bordered w-full max-w-xs" bind:value={spec2}>
        {#each specdata as specification}
            {#if specification.spec_type == spectypes[1]}
                <option value="{specification.spec_id}">{specification.spec_value}</option>
            {/if}
        {/each}
    </select> <br><br>

    <label>{spectypes[2]}</label>
    <select class="select select-bordered w-full max-w-xs" bind:value={spec3}>
        {#each specdata as specification}
            {#if specification.spec_type == spectypes[2]}
                <option value="{specification.spec_id}">{specification.spec_value}</option>
            {/if}
        {/each}
    </select> <br><br>

    <div class="form-control">
        <label class="label">
          <span class="label-text">Product Description</span>
        </label> 
        <textarea class="textarea h-24 textarea-bordered" bind:value={product_description}></textarea>
    </div>

    <br><br><button type="button" class="btn btn-primary" on:click={doPost} >
        Add Hoodie
    </button>

    <br><br><button class="btn btn-wide btn-lg" on:click={() => push('/addproduct')}>Go Back</button>
    <br><br><button class="btn btn-wide btn-lg" on:click={() => push('/view1')}>View All Products</button>

</div> 

