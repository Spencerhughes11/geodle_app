<div class="box">
    <slot />
</div>

<style>
	.box {
		width: 8em;
		height: 5em;
		border-radius: 0.35em;
		/* margin: 0 0 0 0; */
        margin-bottom: 25px;
		background: var(--color, #ddd);
        align-items: center;
        justify-content: center;
	}
</style>