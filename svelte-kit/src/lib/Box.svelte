<script>
    export let color;
</script>

<div class="box" style="--color: {color}">
    <slot />
</div>

<style>
    .box {
        display: flex;
        width: 8em;
        height: 3em;
		padding: 0.25em;
        border-radius: 0.35em;
        margin-bottom: 1em;
        background: var(--color, #ddd);
        align-items: center;
        justify-content: center;
    }
</style>
