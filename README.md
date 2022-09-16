# Composer-Predictor
A Python program that uses multinomial probability theory to predict whether Mozart or Bach composed a given piano piece. For more details on the math/code, please refer to the <a href="https://drive.google.com/file/d/1kXaCHOez1-o_YLw8VjFt64t_9xdHVq7C/view?usp=sharing">writeup</a>.

<p align="center">
  <img src="https://imgur.com/mXKxDDx.gif?" alt="Composer Predictor"/>
</p>

### Code Overview
* The program reads in MIDI files of pieces written by Bach and Mozart
* Uses the data to create probability dictionaries that map pitches (represented as MIDI numbers) to the probability that Bach/Mozart wrote that pitch
* Computes a log likelihood ratio using the probability dictionaries to predict who composed a mystery piece (also stored as a MIDI file)
