
<script>
    import Box from './Box.svelte';
</script>
<div id='box'>
                    <!-- <h3 class='header'>HEMISPHERE</h3> -->
    <div class='feedback-box'>
        <Box --color={guessData.hemiColor}>
            <p>{guessData.guessHemi}</p>
        </Box>
    </div>

</div>