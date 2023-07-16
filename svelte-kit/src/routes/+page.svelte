<script>
    import { onMount } from 'svelte';

    $: guess = ''

    let all_data = {'feedback': {'letter': 'grey', 'hemisphere': 'grey', 
                    'continent': 'yellow', 'area': 'grey', 'area_higher_lower': 'lower', 
                    'population': 'yellow', 'pop_higher_lower': 'lower'}, 
        
                    'guess_data': {'guess': guess, 'letter': 'C', 'hemisphere': 'B', 'continent': 'Africa', 
                        'area': '341,500', 'population': '5,518,087'}}     
    let guessCount = 1

    $: guessHemi = all_data.guess_data.hemisphere
    $: guessCont = all_data.guess_data.continent
    $: guessArea = all_data.guess_data.area
    $: guessPop = all_data.guess_data.population

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
                <p class='header'>NAME</p>
                <div class='feedbackBox'>
                    <p>{guess}</p>
                </div>
            </div>
            <div id='hemiBox'>
                <p class='header'>HEMISPHERE</p>
                <div class='feedbackBox'>
                    <p>{guessHemi}</p>
                </div>
            </div>
            <div id='continentBox'>
                <p class='header'>CONTINENT</p>
                <div class='feedbackBox'>
                    <p>{guessCont}</p>
                </div>
            </div>
            <div id='areaBox'>
                <p class='header'>AREA (KM^2)</p>
                <div class='feedbackBox'>
                    <p>{guessArea}</p>
                </div>
            </div>
            <div id='popBox'>
                <p class='header'>POPULATION</p>
                <div class='feedbackBox'>
                    <p>{guessPop}</p>
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
    align-items: center;
    justify-content: center;
    color: antiquewhite;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  }
  .header{
    position: static;
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
  