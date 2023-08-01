<script>
    import { onMount } from 'svelte';
    import Box from '../lib/Box.svelte';
    import Feedback from '../lib/Feedback.svelte';
    import { backendURL } from '$lib/urls';
	import data from '../../../data.json';
	import { json } from '@sveltejs/kit';
	import countryList  from '../lib/countrylist';
    
	// Dummy Data for test
    // $: all_data = {'feedback': {'letter': 'grey', 'hemisphere': 'green', 'continent': 'yellow', 'area': 'grey', 
    // 'area_higher_lower': 'lower', 'population': 'grey', 'pop_higher_lower': 'lower'}, 
    // 'guess_data': {'letter': 'C', 'hemisphere': 'N', 'continent': 'Asia', 'area': '9,388,211', 'population': '1,439,323,776'}} ;    
	
	// -------------------- Random Country Selection --------------------
	// let generateSecretCountry = () => {
	let countryNames = Object.keys(data);
	let randomIndex = Math.floor(Math.random() * countryNames.length);
	let secretCountry = countryNames[randomIndex];
	// }
		// console.log(countryList)

	let guessCount = 0;

    let guessHolder = [];

    let all_data = {};
    let guessHemi;
    let guessCont;
    let guessArea;
    let guessPop;
    
    let letterColor;
    let hemiColor;
    let contColor;
    let areaColor;
    let popColor;

    let guessData;
    // onMount(async () => {
    //     fetchData();
    // })
    let guess = ''
    // const secretCountry = 'Germany';

    let fetchData = async () => {
		try {
			const timeLabel = `Fetching data for ${guess}`
			console.time(timeLabel);

			const response = await fetch(backendURL(`/?guess=${guess}&secret_country=${secretCountry}`));
			console.timeEnd(timeLabel); 
			if (!response.ok) {
				throw new Error(`Request failed with status ${response.status}`);
			}
			all_data = (await response.json());
			console.log('All Data: ', all_data)

			guessHemi = all_data.guess_data.hemisphere ? all_data.guess_data.hemisphere : '';
			guessCont = all_data.guess_data.continent ? all_data.guess_data.continent : '';
			guessArea = all_data.guess_data.area ? all_data.guess_data.area : '' ;
			guessPop = all_data.guess_data.population ? all_data.guess_data.population : '';

			letterColor = all_data.feedback.letter ? all_data.feedback.letter : '' ;
			hemiColor = all_data.feedback.hemisphere ? all_data.feedback.hemisphere : '';
			contColor = all_data.feedback.continent ? all_data.feedback.continent : '' ;
			areaColor = all_data.feedback.area ? all_data.feedback.area : '' ;
			popColor = all_data.feedback.population ? all_data.feedback.population : '' ;
			guessData = all_data.guess_data
			// console.log(guessData)
			// guessHolder.push(guess);
			guessHolder.push({
				guess: guess,
				guessHemi: guessHemi,
				guessCont: guessCont,
				guessArea: guessArea,
				guessPop: guessPop,
				letterColor: letterColor,
				hemiColor: hemiColor,
				contColor: contColor,
				areaColor: areaColor,
				popColor: popColor
			});
			console.log('guessHolder: ', guessHolder)
			// console.log('popColor: ', popColor)

			guessCount++;
			console.log('Guess:', guess)
			console.log('Secret country:', secretCountry)
			if (guess == secretCountry){
				alert(`You've guessed correctly in ${guessCount} tries!`)
				guess = ''
				guessHolder = []
				randomIndex = Math.floor(Math.random() * countryNames.length);
			    secretCountry = countryNames[randomIndex];

			}
			guess = ''
		}  catch (error) {
	console.error('Error:', error);
	alert(`'${guess}' not found in database`)				// FIXME: might apply to different error
	}
		
    }

    // TEST for Dummy Data
    // let test = async () => {
    // if (guessCount < 8) {
    //     console.log(guess.toLowerCase());
    //     console.log(guessData)
    //     console.log('All Data: ', all_data);

    //     guessCount++;
    //     guessHolder.push(guess);

    // }
            
    //     };
    

    function handleKeydown(event) {
		if (event.key === 'Enter') {
            fetchData();
        }

	}

	let showAnswer = () => {
		alert(`Secret country is ${secretCountry}`);
	}

</script>
  
  
  <body>
        <div class="showAnswer">
            <h1 class='head'>GEODLE</h1>
            <button id="showAnswer" on:click={showAnswer}>Show Answer</button>
        </div>

        <div class="input">
            <!-- <form method="POST" action="/"> -->
            <input list='countries' id="userGuess" placeholder="Enter country name here: " bind:value={guess} on:keydown={handleKeydown} autocapitalize="on"> 
			<datalist id='countries'>
				{#each countryList.sort() as country}
					<option value={country} />
				{/each}
			</datalist>
            <button id="enter" on:click={fetchData}>Enter</button> 
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
    {#each guessHolder as guessData}
        {#if guessCount > 0}
            <div class='feedback-wrapper gap-1'>
				<!-- <Feedback guessData={guessData}>
				
				</Feedback> -->
                <div id='nameBox'>
                        <div class='feedback-box'>
                            <Box --color={guessData.letterColor}>
                                <p>{guessData.guess.toUpperCase()}</p>
                            </Box>
                        </div>
                    </div>
                <div id='hemiBox'>
                        <div class='feedback-box'>
                            <Box --color={guessData.hemiColor}>
                                <p>{guessData.guessHemi}</p>
                            </Box>
                        </div>
                </div>
                <div id='continentBox'>
                        <div class='feedback-box'>
                            <Box --color={guessData.contColor}>
                                <p>{guessData.guessCont}</p>
                            </Box>
                        </div> 
                </div>
                <div id='areaBox'>
                        <div class='feedback-box'>
                            <Box --color={guessData.areaColor} >
                                <p>{guessData.guessArea}</p>
                            </Box>
                        </div>  
                </div>
                <div id='popBox'>
                        <div class='feedback-box'>
                            <Box --color={guessData.popColor}>
                                <p>{guessData.guessPop}</p>
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
	justify-content: center;
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
  