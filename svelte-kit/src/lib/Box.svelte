<script>
    // export let unfilled = 8
</script>

<!-- {#each { length: unfilled } as i} -->
	<div class="box">
		<slot />
	</div>
<!-- {/each} -->

<!-- {#if filled} -->
	<style>
		.box {
			width: 6em;
			height: 3em;
			border-radius: 0.35em;
			/* margin: 0 0 0 0; */
			margin-bottom: 25px;
			background: var(--color, #ddd);
			align-items: center;
			justify-content: center;
			text-align: center;
		}
	</style>
<!-- {:else}
	<style>
		.box {
			width: 6em;
			height: 3em;
			border-radius: 0.35em;
			/* margin: 0 0 0 0; */
			margin-bottom: 25px;
			border: antiquewhite solid;
			/* background: var(--color, #ddd); */
			align-items: center;
			justify-content: center;
			text-align: center;
		}
	</style>
{/if} -->
