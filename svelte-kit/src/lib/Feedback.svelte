
<script>
    import Box from './Box.svelte';

    export let guessData = {
        guessColor: '',
        guessFeedback: '',
    }
</script>

<div id='box'>
                    <!-- <h3 class='header'>HEMISPHERE</h3> -->
    <div class='feedback-box'>
        <Box --color={guessData.guessColor}>
            <p>{guessData.guessFeedback}</p>
        </Box>
    </div>

</div>