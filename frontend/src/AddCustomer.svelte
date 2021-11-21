<script>

    import {push, pop, replace} from 'svelte-spa-router';

	let first_name = ''
	let middle_name = ''
    let last_name = ''
    let date_of_birth = 'YYYY-MM-DD'
    let gender = ''
    let email = ''
    let shipping_address = ''
    let phone_number = '(XXX) XXX-XXXX'
	let result = null

	async function doPost () {
		const res = await fetch('http://localhost:8000/customers/', {
			method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
			body: JSON.stringify({
				first_name,
				middle_name,
                last_name,
                date_of_birth,
                gender,
                email,
                shipping_address,
                phone_number,
			})
		})

        if (res.ok){
            confirm("Customer Added Successfully!")
            push('/customers')
        }
        else{
            alert("There was an error")
        }

		const json = await res.json()
		result = JSON.stringify(json)
	}

</script>


<div style="text-align: center;">
    
    <label>First Name</label>
    <input type="text" class="input input-bordered" bind:value={first_name} />

    <label>Middle Name</label>
    <input type="text" class="input input-bordered" bind:value={middle_name} />

    <label>Last Name</label>
    <input type="text" class="input input-bordered" bind:value={last_name} />

    <label>Date of Birth (YYYY-MM-DD)</label>
    <input type="text" class="input input-bordered" bind:value={date_of_birth} /> <br><br>

    <label>Gender</label>
    <select class="select select-bordered w-full max-w-xs" bind:value={gender}>
        <option>Male</option> 
        <option>Female</option> 
        <option>Other</option>
    </select>

    <label>Email</label>
    <input type="text" class="input input-bordered" bind:value={email} />

    <label>Shipping Address</label>
    <input type="text" class="input input-bordered" bind:value={shipping_address} />

    <label>Phone Number</label>
    <input type="text" class="input input-bordered" bind:value={phone_number} />
    

    <br><br><br><button type="button" class="btn btn-primary" on:click={doPost} >
        Add Customer
    </button>
</div> 

