<script>
  
  /* Routing */
  import Router, {location, link} from 'svelte-spa-router'
  import Home from './Home.svelte';
  import NotFound from './NotFound.svelte';
  import Stores from './Stores.svelte';
  import logo from './assets/GameStartLogo.png'
  import AllGames from './AllGames.svelte';
  import AllSystems from './AllSystems.svelte';
  import AllMonitors from './AllMonitors.svelte';
  import AllHeadsets from './AllHeadsets.svelte';
  import AllChargers from './AllChargers.svelte';
  import AllHoodies from './AllHoodies.svelte';
  import Employees from './Employees.svelte';
  import FiredEmployees from './FiredEmployees.svelte';
  import Customers from './Customers.svelte';
  import Inventories from './Inventories.svelte';
  import StorageContainers from './StorageContainers.svelte';
  import AllProducts from './AllProducts.svelte';
  import CustomerOrders from './CustomerOrders.svelte';
  import AddCustomer from './AddCustomer.svelte';
  /* Routing */

  
</script>

<!-- Navbar -->
<div class="navbar mb-2 shadow-lg bg-neutral text-neutral-content rounded-box">
  <div class="flex-none px-2 mx-2">
    <span class="text-lg font-bold">
            Game Start
          </span>
  </div> 
  <div class="flex-1 px-2 mx-2">
    <div class="items-stretch hidden lg:flex">
      <a class="btn btn-ghost btn-sm rounded-btn" href="/" use:link>
              Home
            </a> 
      <a class="btn btn-ghost btn-sm rounded-btn" href="/stores" use:link>
              Stores
            </a>
            <a class="btn btn-ghost btn-sm rounded-btn" href="/employees" use:link>
              Employees
            </a>  
            <a class="btn btn-ghost btn-sm rounded-btn" href="/customers" use:link>
              Customers
            </a>  
            <a class="btn btn-ghost btn-sm rounded-btn" href="/inventories" use:link>
              Inventories
            </a>  
            <a class="btn btn-ghost btn-sm rounded-btn" href="/storagecontainers" use:link>
              Storage Containers
            </a>  
            <a class="btn btn-ghost btn-sm rounded-btn" href="/allproducts" use:link>
              All Products
            </a>  
    </div>
  </div> 
  <div class="flex-none">
    <div class="avatar">
      <div class="rounded-full w-10 h-10 m-1">
        <img alt="?" src={logo}>
      </div>
    </div>
  </div>
</div>
<!-- Navbar -->


<Router routes={{
  
  '/': Home,
  '/stores': Stores,
  '/allgames': AllGames,
  '/allsystems': AllSystems,
  '/allmonitors':AllMonitors,
  '/allheadsets': AllHeadsets,
  '/allchargers': AllChargers,
  '/allhoodies': AllHoodies,
  '/employees': Employees,
  '/firedemployees': FiredEmployees,
  '/customers': Customers,
  '/customerorders': CustomerOrders,
  '/inventories': Inventories,
  '/storagecontainers': StorageContainers,
  '/allproducts': AllProducts,
  '/addcustomer': AddCustomer,
  
  '*': NotFound 
}} />

