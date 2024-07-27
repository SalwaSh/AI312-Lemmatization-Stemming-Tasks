
## Overview 
Computational Morphology
What is Morphology?
Morphology studies the internal structure of words, how words are built up from smaller meaningful units called “morpheme”.

Morphemes is the  smallest (meaningful / grammatical) parts of words.
such as  dogs
 2 morphemes, ‘dog’ and ‘s’
 ● ‘s’ is a plural marker of nouns

 For many NLP tasks, it is desirable to remove inflectional morphology (which does not change the meaning or part of speech of words) but leave derivational morphology behind.
 ● For example, in information retrieval if you search for "repurpose" you probable 
also want to return "repurposing", "repurposes", and "repurposed" but probably not purpose.
 ● To do this, data may be normalized using:
 ○ stemming (which “chops off ” inflectional affixes to yield a “stem”) or 
○ lemmatization (which returns the “dictionary” form i.e. “lemma” of a word)

<table>
  <thead>
    <tr>
      <th>Stemming</th>
      <th>Lemmatization</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Can reduce words to a stem that is not an existing word</td>
      <td>Reduces inflected words to their lemma, which is always an exisiting word</td>
    </tr>
     <tr>
      <td>Simpler and faster</td>
      <td>More accurate but slower</td>
     </tr>
     <tr>
      <td>achieving -> achiev</td>
      <td>achieving -> achieve</td>
    </tr>
  </tbody>
</table>

Task
Lemmatization:
Task-1: transform each word in the file “wiki_mountain_def.txt” into its Lemma form using “built-in lemma_ function of SpaCy”.
Task-2: how many total words are changed due to this lemmatization process?
 
Stemming:
Task-1: transform each word in the file “wiki_mountain_def.txt” into its Stem form 
by coding  only the following rules of Porter Stemming

SSES -> SS   caresses -> caress
IES -> I     ponies -> poni
ties -> ti   SS -> SS
caress ->    Caress S -> 
cats -> cat

Task-2: how many total words are changed due to this stemming process?
