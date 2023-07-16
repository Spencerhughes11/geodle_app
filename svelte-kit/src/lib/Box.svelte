<div class="box">
    <slot />
</div>

<style>
	.box {
		width: 8em;
		height: 5em;
		border-radius: 0.5em;
		margin: 0 0 1em 0;
		background: var(--color, #ddd);
        align-items: center;
        justify-content: center;
	}
</style>