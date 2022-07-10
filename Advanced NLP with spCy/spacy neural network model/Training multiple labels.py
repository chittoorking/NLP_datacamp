# Here's a small sample of a dataset created to train a new entity type WEBSITE. The original dataset contains a few thousand sentences. In this exercise, you'll be doing the labeling by hand. In real life, you probably want to automate this and use an annotation tool – for example, Brat, a popular open-source solution, or Prodigy, our own annotation tool that integrates with spaCy.

# After this exercise you will be nearly done with the course! If you enjoyed it, feel free to send Ines a thank you via Twitter - she'll appreciate it! Tweet to Ines
TRAINING_DATA = [
    ("Reddit partners with Patreon to help creators build communities", 
     {'entities': [(0, 6, 'WEBSITE'), (21, 28, 'WEBSITE')]}),
  
    ("PewDiePie smashes YouTube record", 
     {'entities': [(0,len('PewDiePie'),'PERSON'), (18, 25, 'WEBSITE')]}),
  
    ("Reddit founder Alexis Ohanian gave away two Metallica tickets to fans", 
     {'entities': [(0, 6, 'WEBSITE'), (15,15+len('Alexis Ohanian'),'PERSON')]}),
    # And so on...
]
