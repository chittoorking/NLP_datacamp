# In the previous exercise, you wrote a script using spaCy's PhraseMatcher to find country names in text. Let's use that country matcher on a longer text, analyze the syntax and update the document's entities with the matched countries. The nlp object has already been created.

# The text is available as the variable text, the PhraseMatcher with the country patterns as the variable matcher. The Span class has already been imported.

# Iterate over the matches and create a Span with the label "GPE" (geopolitical entity).
# Overwrite the entities in doc.ents and add the matched span.


text='After the Cold War, the UN saw a radical expansion in its peacekeeping duties, taking on more missions in ten years than it had in the previous four decades.Between 1988 and 2000, the number of adopted Security Council resolutions more than doubled, and the peacekeeping budget increased more than tenfold. The UN negotiated an end to the Salvadoran Civil War, launched a successful peacekeeping mission in Namibia, and oversaw democratic elections in post-apartheid South Africa and post-Khmer Rouge Cambodia. In 1991, the UN authorized a US-led coalition that repulsed the Iraqi invasion of Kuwait. Brian Urquhart, Under-Secretary-General from 1971 to 1985, later described the hopes raised by these successes as a "false renaissance" for the organization, given the more troubled missions that followed. Though the UN Charter had been written primarily to prevent aggression by one nation against another, in the early 1990s the UN faced a number of simultaneous, serious crises within nations such as Somalia, Haiti, Mozambique, and the former Yugoslavia. The UN mission in Somalia was widely viewed as a failure after the US withdrawal following casualties in the Battle of Mogadishu, and the UN mission to Bosnia faced "worldwide ridicule" for its indecisive and confused mission in the face of ethnic cleansing. In 1994, the UN Assistance Mission for Rwanda failed to intervene in the Rwandan genocide amid indecision in the Security Council. Beginning in the last decades of the Cold War, American and European critics of the UN condemned the organization for perceived mismanagement and corruption. In 1984, the US President, Ronald Reagan, withdrew his nation\'s funding from UNESCO (the United Nations Educational, Scientific and Cultural Organization, founded 1946) over allegations of mismanagement, followed by Britain and Singapore. Boutros Boutros-Ghali, Secretary-General from 1992 to 1996, initiated a reform of the Secretariat, reducing the size of the organization somewhat. His successor, Kofi Annan (1997–2006), initiated further management reforms in the face of threats from the United States to withhold its UN dues. In the late 1990s and 2000s, international interventions authorized by the UN took a wider variety of forms. The UN mission in the Sierra Leone Civil War of 1991–2002 was supplemented by British Royal Marines, and the invasion of Afghanistan in 2001 was overseen by NATO. In 2003, the United States invaded Iraq despite failing to pass a UN Security Council resolution for authorization, prompting a new round of questioning of the organization\'s effectiveness. Under the eighth Secretary-General, Ban Ki-moon, the UN has intervened with peacekeepers in crises including the War in Darfur in Sudan and the Kivu conflict in the Democratic Republic of Congo and sent observers and chemical weapons inspectors to the Syrian Civil War. In 2013, an internal review of UN actions in the final battles of the Sri Lankan Civil War in 2009 concluded that the organization had suffered "systemic failure". One hundred and one UN personnel died in the 2010 Haiti earthquake, the worst loss of life in the organization\'s history. The Millennium Summit was held in 2000 to discuss the UN\'s role in the 21st century. The three day meeting was the largest gathering of world leaders in history, and culminated in the adoption by all member states of the Millennium Development Goals (MDGs), a commitment to achieve international development in areas such as poverty reduction, gender equality, and public health. Progress towards these goals, which were to be met by 2015, was ultimately uneven. The 2005 World Summit reaffirmed the UN\'s focus on promoting development, peacekeeping, human rights, and global security. The Sustainable Development Goals were launched in 2015 to succeed the Millennium Development Goals. In addition to addressing global challenges, the UN has sought to improve its accountability and democratic legitimacy by engaging more with civil society and fostering a global constituency. In an effort to enhance transparency, in 2016 the organization held its first public debate between candidates for Secretary-General. On 1 January 2017, Portuguese diplomat António Guterres, who previously served as UN High Commissioner for Refugees, became the ninth Secretary-General. Guterres has highlighted several key goals for his administration, including an emphasis on diplomacy for preventing conflicts, more effective peacekeeping efforts, and streamlining the organization to be more responsive and versatile to global needs.'


# Create a doc and find matches in it
doc =nlp(text)

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Create a Span with the label for "GPE"
    span = Span(doc, start, end, label="GPE")

    # Overwrite the doc.ents and add the span
    doc.ents = list(doc.ents) + [span]

# Print the entities in the document
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == 'GPE'])


# Update the script and get the matched span's root head token.
# Print the text of the head token and the span.
# Create a doc and find matches in it
doc = nlp(text)

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Create a Span with the label for "GPE" and overwrite the doc.ents
    span = Span(doc, start, end, label='GPE')
    doc.ents = list(doc.ents) + [span]
    
    # Get the span's root head token
    span_root_head = span.root.head
    # Print the text of the span root's head token and the span text
    print(span_root_head.text, '-->', span.text)
    
# Namibia --> Namibia
# South --> South Africa
# Cambodia --> Cambodia
# Kuwait --> Kuwait
# Somalia --> Somalia
# Haiti --> Haiti
# Mozambique --> Mozambique
# Somalia --> Somalia
# Rwanda --> Rwanda
# Singapore --> Singapore
# Sierra --> Sierra Leone
# Afghanistan --> Afghanistan
# Iraq --> Iraq
# Sudan --> Sudan
# Congo --> Congo
# Haiti --> Haiti
    
    
    
    
    
    
