<script>
    import { onMount } from 'svelte';
    import Box from '../lib/Box.svelte';

    

    let all_data = {'feedback': {'letter': 'yellow', 'hemisphere': 'green', 
                    'continent': 'yellow', 'area': 'grey', 'area_higher_lower': 'lower', 
                    'population': 'yellow', 'pop_higher_lower': 'lower'}, 
        
                    'guess_data': {'letter': 'C', 'hemisphere': 'N', 'continent': 'Africa', 
                        'area': '341,500', 'population': '5,518,087'}} ;    
    let guessCount = 0;

    let guessHolder = [];

    $: guess = ''
    $: guessHemi = all_data.guess_data.hemisphere;
    $: guessCont = all_data.guess_data.continent;
    $: guessArea = all_data.guess_data.area;
    $: guessPop = all_data.guess_data.population;

    $: letterColor = all_data.feedback.letter;
    $: hemiColor = all_data.feedback.hemisphere;
    $: contColor = all_data.feedback.continent;
    $: areaColor = all_data.feedback.area;
    $: popColor = all_data.feedback.population;

    
        let test = () => {
            if (guessCount < 8){

                console.log(guess.toLowerCase());
                // guess = guess.toLowerCase();
                guessCount++;
                guessHolder.push(guess);
            } else {
                alert("CUM")
            }
            // fetch('/', {
            // method: 'GET',
            // headers: {
            //     'Content-Type': 'application/json'
            // },
            // body: JSON.stringify({ guess: guess })
            // })
            // .then(response => response.json())
            // .then(data => {
            //     console.log(data);
            // })
            // .catch(error => {
            //     console.error('Error:', error);
            // });
        };
    

    function handleKeydown(event) {
		if (event.key === 'Enter') {
            test();
        }

	}

</script>
  
  
  <body>
        <div class="showAnswer">
            <h1 class='head'>GEODLE</h1>
            <button id="showAnswer">Show Answer</button>
        </div>

        <div class="input">
            <!-- <form method="POST" action="/"> -->
            <input type="text" id="userGuess" placeholder="Enter country name here: " bind:value={guess} on:keydown={handleKeydown}> <br> 
            <button id="enter" on:click={test}>Enter</button> 
            <!-- </form>   -->
        </div>
      <!-- <select id="countryDropdown"></select> -->
    <!--  feedback boxes -->
    
    <div class="headers-wrapper gap-1">
        <p class='header'>NAME</p>
        <p class='header'>HEMISPHERE</p>
        <p class='header'>CONTINENT</p>
        <p class='header'>AREA</p>
        <p class='header'>POPULATION</p>
    </div> 
    <div class="board"></div>
    {#each guessHolder as guess}
        {#if guessCount > 0}
            <div class='feedback-wrapper gap-1'>
                <div id='nameBox'>
                    <!-- <h3 class='header'>NAME</h3> -->
                        <div class='feedback-box'>
                            <Box --color={letterColor}>
                                <p>{guess.toUpperCase()}</p>
                            </Box>
                        </div>
                    </div>
                <div id='hemiBox'>
                    <!-- <h3 class='header'>HEMISPHERE</h3> -->
                        <div class='feedback-box'>
                            <Box --color={hemiColor}>
                                <p>{guessHemi}</p>
                            </Box>
                        </div>
                </div>
                <div id='continentBox'>
                    <!-- <h3 class='header'>CONTINENT</h3> -->
                        <div class='feedback-box'>
                            <Box --color={contColor}>
                                <p>{guessCont}</p>
                            </Box>
                        </div> 
                </div>
                <div id='areaBox'>
                    <!-- <h3 class='header'>AREA (KM^2)</h3> -->
                        <div class='feedback-box'>
                            <Box --color={areaColor} >
                                <p>{guessArea}</p>
                            </Box>
                        </div>  
                </div>
                <div id='popBox'>
                    <!-- <h3 class='header'>POPULATION</h3> -->
                        <div class='feedback-box'>
                            <Box --color={popColor}>
                                <p>{guessPop}</p>
                            </Box>
                        </div> 
                </div>
            </div>
        
        {/if}    
    {/each}  
      <div id="guessHolder"></div>
  </body>
  
  
  
<style>
 :global(body){
    background-color: #011844;
 }
   
  h1{
    color: antiquewhite;
    font-size: 50px;
  }
  
  h1:after {
    content:' ';
    display:block;
    border:2px solid #d0d0d0;
    border-radius:4px;
    -webkit-border-radius:4px;
    -moz-border-radius:4px;
    box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
    -webkit-box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
    -moz-box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
}
  .input{
    display: flex;
    align-items: center;
    justify-content: center;
  }
  #enter {
    background-color: antiquewhite;
    cursor: pointer;
  
  }
  
  #countryDropdown {
    background-color: antiquewhite;
    cursor: pointer;
  }
  
  #guessHolder {
    color: antiquewhite;
  }
/*   
  .wrapper{
    display: flexbox;
    align-items: center;
    justify-content: center;
    width: 75%;
    margin: auto
  } */
  
  .feedback-wrapper{
    display: grid;
    width: 40%;
    margin: auto;
    align-items: center;
    justify-content: center;
    grid-auto-columns: 1fr;
    /* grid-template-columns: (5,minmax(0,1fr)); */
  }
  .gap-1 {
    column-gap: 7px;
  }

  .headers-wrapper{
    height: 65px;
    display: grid;
    width: 35%;
    margin: auto;
    align-items: center;
    justify-content: center;
    grid-auto-columns: 1fr;
    /* grid-template-columns: (5,minmax(0,1fr)); */
  }
  
  .header{
    font-size: 18px;
    color: antiquewhite;
    text-align: center;
    align-items: center;
    justify-content: center;
    grid-row: 1 / span 12;
    height: 25px
  }

  .feedback-box {
    display: flex;
    align-items: center;
    justify-content: center;
  }
 
  p{
    margin: auto;
    width: 50%;
    padding: 16px;
    text-align: center;
  }

  #nameBox{
    align-items: center;
    justify-content: center;
    grid-row: 1 / span 12;
    text-align: center;
  }
  #hemiBox{
    text-align: center;
    align-items: center;
    justify-content: center;
    grid-row: 1 / span 12;
  }
  #continentBox{
    text-align: center;
    align-items: center;
    justify-content: center;
    grid-row: 1 / span 12;
  }
  #areaBox{
    text-align: center;
    align-items: center;
    justify-content: center;
    grid-row: 1 / span 12;
  }
  #popBox{
    text-align: center;
    align-items: center;
    justify-content: center;
    grid-row: 1 / span 12;
  }
  
  
  .head{
    display: flexbox;
    align-items: center;
    justify-content: center;
  }
  .showAnswer {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100px;
  }
  
  #showAnswer {
    position: absolute;
    top: 15px;
    right: 15px;
    
  }
  
  </style>
  