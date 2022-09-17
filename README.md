# Composer-Predictor
A Python program that uses multinomial probability theory to predict whether Mozart or Bach composed a given piano piece. For more details on the math/code, please refer to the <a href="https://drive.google.com/file/d/1kXaCHOez1-o_YLw8VjFt64t_9xdHVq7C/view?usp=sharing">writeup</a>.

<p align="center">
  <img src="https://imgur.com/mXKxDDx.gif?" alt="Composer Predictor"/>
</p>


### Code Overview
* The program reads in MIDI files of pieces written by Bach and Mozart
* Uses the data to create probability dictionaries that map pitches (represented as MIDI numbers) to the probability that Bach/Mozart wrote that pitch
* Computes a log likelihood ratio using the probability dictionaries to predict who composed a mystery piece (also stored as a MIDI file)

### Setup Instructions
- To run with the provided mystery piece (Ah vous dirai-je, Maman by Mozart), you can just run the file `composer_predictor.py`

- To add your own mystery piece:
  - Add a MIDI file (e.g. `example.mid`) to the testing/ folder. You can find MIDI files for Bach and Mozart pieces on Google.
  - Go to line 126 of `composer_predictor.py` and rename the file path appropriately (e.g. `mystery_piece = "testing/example.mid"`)
  - Now you can run `composer_predictor.py` to see the prediction.
