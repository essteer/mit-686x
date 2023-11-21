# NLP - Parsing

Parsing refers to understanding the syntactic structure of a sentence.

The categorisation of NLP technologies as "mostly solved" is not quite accurate; there is enormous divergence across languages - compare translation abilities for English versus Arabic, for example, or less-spoken languages for which there is only a fraction of data available.

**Machine translation**

Some language pairs will have a large amount of data available, such as English and French, whereas there will be much less available for the pairing of Korean and Hungarian.

Simple substitution of words in one language for words in another would lead to a very poor solution. Solutions require developing a good way of understanding the meaning of the source sentence and finding a good counterpart for the whole phrase in target sentence.

Machine translation under low-resource setting (low amount of training data) results in significantly worse quality than under high-resource setting and this is still a challenging open problem for NLP community to solve.

News translations may be quite advanced, but other domains such as cooking recipes, which rely on a type of instruction very different to language used in news reporting, are far behind.

This is less a problem of the task being more difficult, but more a case of lacking comparable volumes of data on which to train.

Most recent state of the art approaches to machine translation including the Neural Machine Translation (NMT) based approach, achieve excellent accuracy values by training on datasets consisting of millions of examples which were not available a decade or two ago.

**Question answering**

For questions with simple factual answers, machines may outperform humans because of their access to vastly larger databases of knowledge than are immediately available to human memory, and across a greater number of domains.

Questions that require reasoning to solve, however, are far more challenging for machines.

Compare:

"William Wilkinson's 'An account of the principalities of Wallachia and Moldovia' inspired this author's most famous novel?"

"What was the inspiration for 'Flowers of Algernon'?"

The second question requires more context than the first, but an answer may still be readily available via a search engine request.

A contextual question, that requires interpretation of a passage in order to deduce details (think of a typical foreign language passage in a textbook, followed by mutliple choice questions to check understanding) may be far more challenging because it involves logical reasoning.
