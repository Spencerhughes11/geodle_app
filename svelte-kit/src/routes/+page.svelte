<script>
    import { onMount } from 'svelte';
    import Box from '../lib/Box.svelte';
    import Feedback from '../lib/Feedback.svelte';
    import { backendURL } from '$lib/urls';
	import data from '../../../data.json';
	import { json } from '@sveltejs/kit';
	import countryList  from '../lib/countrylist';
  import * as THREE from 'three';

    
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
	let guessedCountries = [];

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
	const territories = ['cayman islands', 'u.s. virgin islands', 'us virgin islands', 
                    'british virgin islands', 'guam','samoa', 'american samoa',
                    "samoa", 'turks and caicos', 'bermuda']
	
	let newGame = () => {
		guess = ''
		guessCount = 0
		guessHolder = []
		guessedCountries = []
		randomIndex = Math.floor(Math.random() * countryNames.length);
		secretCountry = countryNames[randomIndex];
	}

    let fetchData = async () => {
		try {
			if ( territories.includes(guess.toLowerCase())){
				alert(`'${guess.toUpperCase()}' is considered a territory`);
			}
			if (guessedCountries.includes(guess.toLowerCase())) {
				alert(`Already guessed '${guess}'`)
				guess = ''
				return
			} 
			if (guessCount == 7 && guess.toLowerCase() != secretCountry.toLowerCase()) {
				alert(`Out of guesses :( The secret country was: ${secretCountry}`)				// FIXME
				newGame();
			}
				const timeLabel = `Fetching data for ${guess}`
				guessedCountries.push(guess.toLowerCase());

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
				// console.log('Guess Data: ', guessData)
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
				// console.log('Secret country:', secretCountry)
				if (guess.toLowerCase() == secretCountry.toLowerCase()) {
					alert(`You've guessed correctly in ${guessCount} tries!`)
					newGame();
				} 
				guess = ''
		}  catch (error) {
	console.error('Error:', error);
	if (!territories.includes(guess.toLowerCase()))
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

  let infoText = () => {
    alert('Rules for Geodle... coming soon!');
  }
  let settingsPopup = () => {
    alert('Settings for Geodle... coming soon!\nWill include difficulty, theme, and more.');
  }

</script>
  
  
<body>
    <div class="headerWrapper">
        <div class='title-bar'>
            <div class='left-section'>
                <!-- <p>Guesses:</p> -->
                <p id='guessTotal'>Guesses: {guessCount} / 8</p>
                
            </div>
            <div class='center-section'>
                <h1 class='head'>GEODLE</h1>
            </div>
            <div class='right-section'>

                <a href='/' on:click={settingsPopup}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke="antiquewhite" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="settings">
                        <circle cx="12" cy="12" r="3"></circle>
                        <path fill='transparent' d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 
                        0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 
                        1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 
                        0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65
                        0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0
                        0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2
                        2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 
                        2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z">
                        </path>
                    </svg>
                </a>
                <a href="/" on:click={infoText} class="active" aria-current="page" aria-label="help" data-cy="home-link">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="info" height="24" width="24">
                      <path fill="black dark:white" d="M12 22c-5.52-.006-9.994-4.48-10-10v-.2C2.11 6.305 6.635 1.928 12.13
                       2c5.497.074 9.904 4.569 9.868 10.065C21.962 17.562 17.497 22 12 22zm-.016-2H12a8 8 0 1 0-.016 0zM13 
                       18h-2v-2h2v2zm0-3h-2a3.583 3.583 0 0 1 1.77-3.178C13.43 11.316 14 10.88 14 10a2 2 0 1 0-4 0H8v-.09a4
                        4 0 1 1 8 .09a3.413 3.413 0 0 1-1.56 2.645A3.1 3.1 0 0 0 13 15z">
                      </path>
                  </svg>
              </a>
            </div>
        </div>
    <!-- </div> -->
    
                
                <!-- <button id="showAnswer" on:click={showAnswer}>Show Answer</button> -->
                <!-- <div>
                    <label class="switch">
                        <input type="checkbox">
                        <span class="slider round"></span>
                    </label>
                </div> -->
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
        </div>
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
            <div class='feedback-wrapper'>
				
                <div id='box'>
                        <!-- <div class='feedback-box'> -->
                            <Box color={guessData.letterColor}>
                                <p class="guessStuff" >{guessData.guess.toUpperCase()}</p>
                            </Box>
                        <!-- </div> -->
                    </div>
                <div id='box'>
                        <!-- <div class='feedback-box'> -->
                            <Box color={guessData.hemiColor}>
                                <p class="guessStuff" >{guessData.guessHemi}</p>
                            </Box>
                        <!-- </div> -->
                </div>
                <div id='box'>
                        <!-- <div class='feedback-box'> -->
                            <Box color={guessData.contColor}>
                                <p class="guessStuff" >{guessData.guessCont}</p>
                            </Box>
                        <!-- </div>  -->
                </div>
                <div id='box'>
                        <!-- <div class='feedback-box'> -->
                            <Box color={guessData.areaColor}>
                                <p class="guessStuff" >{guessData.guessArea}</p>
                            </Box>
                        <!-- </div>   -->
                </div>
                <div id='box'>
                        <!-- <div class='feedback-box'> -->
                            <Box color={guessData.popColor}>
                                <p class="guessStuff" >{guessData.guessPop}</p>
                            </Box>
                        <!-- </div>  -->
                </div>
            </div>
        {/if}    
    {/each}  
      <!-- <div id="guessHolder"></div> -->
       
  </body>
  
  
  
<style>
 :global(body){
    background-color: #011844;
 }
  h1{
    display: grid;
    color: antiquewhite;
    width: 50%;
    justify-content: space-between;
    font-size: 60px;

  }
  /* h1:after {
    content:' ';
    display:block;
    border:2px solid #d0d0d0;
    border-radius:4px;
    -webkit-border-radius:4px;
    -moz-border-radius:4px;
    box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
    -webkit-box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
    -moz-box-shadow:inset 0 1px 1px rgba(0, 0, 0, .05);
} */
  .input{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.2%;
    height: 2em;
    margin: 1em 0 1em 0;
  }

  #userGuess {
    /* display: flex; */
    height: 100%;
    width: 20%;
    border-radius: 5px;
    /* padding: 3px; */
    border: none;
  }
  #enter {
    /* display: flex; */
    font-size: medium;
    background-color: antiquewhite;
    cursor: pointer;
    height: 100%;
    width: 5%;
    border-radius: 5px;
    padding: 3px;
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
  .headers-wrapper,
.feedback-wrapper {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0;
    width: 80%;
    max-width: 65%;
    margin: 0 auto;
    align-items: center;
    justify-content: center;
}

.guessStuff {
  font-size: clamp(1rem, 1vw, 1.5rem);
  color: #011844;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
.header{
    font-size: clamp(1rem, 1.5vw, 1.5rem);
    color: antiquewhite;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
}

  .feedback-box {
    display: flex;
    align-items: center;
    justify-content: center;
	text-align: center;
  }
 
  p{
    margin: auto;
    width: 50%;
    padding: 16px;
    text-align: center;
	justify-content: center;
  }

  #box{
    display: flex;
    align-items: center;
    justify-content: center;
    /* grid-row: 1 / span 12; */
    text-align: center;
  }
  
  .head{
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .headerWrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    /* height: 5em; */
    width: 100%;
}

.title-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    max-width: 75%;
    border-bottom: 1px solid antiquewhite;
    /* margin: 5em 0 7em 0; */
    height: 5em;
    padding: 0%;
}

.left-section {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 30%;
    color: antiquewhite;
}

.center-section {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40%;

}

.right-section {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: 30%;
    gap: 1em;
}

/* #guessTotal {
    text-align: left;
    color: antiquewhite;
    width: 25%;
} */

  
  #showAnswer {
    position: absolute;
    top: 15px;
    right: 15px;
    
  }


.guessCounter {
	color: antiquewhite;
	/* position: absolute;
	top: 15px;
	left: 15px; */
}



.info {
  position: flex;
  align-items: left;
  justify-content: left;
  fill: antiquewhite;
}

.settings {
  position: flex;
  align-items: right;
  justify-content: right;
}


  </style>
  