from src.keyphrase_extraction.keyphrase_extraction import get_keyphrases, print_keyphrases

toy_text = """
Elephants are large mammals of the family Elephantidae
and the order Proboscidea. Two species are traditionally recognised,
the African elephant and the Asian elephant. Elephants are scattered
throughout sub-Saharan Africa, South Asia, and Southeast Asia. Male
African elephants are the largest extant terrestrial animals. All
elephants have a long trunk used for many purposes,
particularly breathing, lifting water and grasping objects. Their
incisors grow into tusks, which can serve as weapons and as tools
for moving objects and digging. Elephants' large ear flaps help
to control their body temperature. Their pillar-like legs can
carry their great weight. African elephants have larger ears
and concave backs while Asian elephants have smaller ears
and convex or level backs.
"""

result = get_keyphrases(corpus=toy_text, method='col', number_of_keyphrases=5)
print "##### Keyphrases extracted via Collocation method #####"
print_keyphrases(keyphrases=result)

print

result = get_keyphrases(corpus=toy_text, method='wtp', number_of_keyphrases=5)
print "##### Keyphrases extracted via Weighted Tag-based Phrase extraction method #####"
print_keyphrases(keyphrases=result)

