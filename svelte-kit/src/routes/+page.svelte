<script>
    import { onMount } from 'svelte';
    import Box from '../lib/Box.svelte';

    $: guess = ''

    let all_data = {'feedback': {'letter': 'grey', 'hemisphere': 'green', 
                    'continent': 'yellow', 'area': 'grey', 'area_higher_lower': 'lower', 
                    'population': 'yellow', 'pop_higher_lower': 'lower'}, 
        
                    'guess_data': {'guess': guess, 'letter': 'C', 'hemisphere': 'N', 'continent': 'Africa', 
                        'area': '341,500', 'population': '5,518,087'}}     
    let guessCount = 1

    $: guessHemi = all_data.guess_data.hemisphere
    $: guessCont = all_data.guess_data.continent
    $: guessArea = all_data.guess_data.area
    $: guessPop = all_data.guess_data.population

    $: letterColor = all_data.feedback.letter
    $: hemiColor = all_data.feedback.hemisphere
    $: contColor = all_data.feedback.continent
    $: areaColor = all_data.feedback.area
    $: popColor = all_data.feedback.population

    /*          data
        {'feedback': {'letter': 'grey', 'hemisphere': 'grey', 
                        'continent': 'yellow', 'area': 'grey', 'area_higher_lower': 'lower', 
                    'population': 'yellow', 'pop_higher_lower': 'lower'}, 
        
        'guess_data': {'letter': 'C', 'hemisphere': 'B', 'continent': 'Africa', 
                        'area': '341,500', 'population': '5,518,087'}}     
    */
  
    let test = () => {
        console.log(guess.toLowerCase());
        // guess = guess.toLowerCase();
        guessCount++;
        guess = ''
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
    {#if guessCount > 0}
        <div class='feedback-wrapper'>
            <div id='nameBox'>
                <h3 class='header'>NAME</h3>
                    <div class='feedbackBox'>
                        <Box --color={letterColor}>
                            <span>{guess}</span>
                        </Box>
                    </div>
            </div>
            <div id='hemiBox'>
                <h3 class='header'>HEMISPHERE</h3>
                    <div class='feedbackBox'>
                        <Box --color={hemiColor}>
                            <p>{guessHemi}</p>
                        </Box>
                    </div>
            </div>
            <div id='continentBox'>
                <h3 class='header'>CONTINENT</h3>
                    <div class='feedbackBox'>
                        <Box --color={contColor}>
                            <p>{guessCont}</p>
                        </Box>
                    </div> 
            </div>
            <div id='areaBox'>
                <h3 class='header'>AREA (KM^2)</h3>
                    <div class='feedbackBox'>
                        <Box --color={areaColor} >
                            <p>{guessArea}</p>
                        </Box>
                    </div>  
            </div>
            <div id='popBox'>
                <h3 class='header'>POPULATION</h3>
                    <div class='feedbackBox'>
                        <Box --color={popColor}>
                            <p>{guessPop}</p>
                        </Box>
                    </div> 
            </div>
        </div>
    {/if}    
      
      <div id="guessHolder"></div>
  </body>
  
  
  
<style>
 :global(body){
    background-color: #011844;
 }
   
  h1{
    color: antiquewhite;
    font-size: 70px;
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
  
  .feedback-wrapper{
    display: grid;
    max-width: 100%;
    align-items: center;
    justify-content: center;
    grid-auto-columns: 1fr;

  }
  .header{
    position: static;
    color: antiquewhite;

  }
 
  p{
    margin: auto;
    width: 50%;
    padding: 30px;
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
    height: 30p;
  }
  
  #showAnswer {
    position: absolute;
    top: 15px;
    right: 15px;
    
  }
  
  </style>
  