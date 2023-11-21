# Difficulties in NLP

**Syntactic ambiguity**

Consider the sentence "At last, a computer that understands you like your mother."

This could be taken to mean either:

- that the computer understands you as well as your mother understands you; or,
- that the computers understands that you like your mother.

**Semantic ambiguity**

"Alice says they've built a computer that understands you like your mother."

Mother could be taken to mean either:

- a female parent; or,
- a stringy slimy substance consisting of yeast cells and bacteria, added to cider or wine to produce vinegar.

This is an instance of **word-sense disambiguation**.

**Discourse-level ambiguity**

"Alice says they've built a computer that understands you like your mother but she..."

- ...doesn't know any details." (referring to Alice)
- ...doesn't understand me at all." (referring to mother)

This is an instance of **anaphora**, where "she" co-refers to some other discourse entity.

**Ambiguity varies across languages**

Tokenisation

English: in the country
Hebrew: בארץ

- Easy task in English - there is a space separator that delineates words.
- Challenging for Semitic languages.

Named entity detection (NED)

English: She saw Jacob
Hebrew: היא ראתה את יעקב

- Easy task in English: capitalisation is a strong hint.
- Challenging for Semitic languages.

This carries across to, for example, interpreting English-language news headlines where keywords are capitalised, whereas there may be no such treatment in many other languages.
