<script>
    
</script>


<div class="box">
    <slot />
</div>

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
        text-align: left;
	}
</style>