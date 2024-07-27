# Stemming and Lemmatization ✂️✨
## Overview 🌐

**What is Morphology?**
Morphology studies the internal structure of words, how words are built up from smaller meaningful units called “morpheme”, such as  "dogs":
- 2 morphemes, ‘dog’ and ‘s’.
- ‘s’ is a plural marker of nouns.

For many NLP tasks, it is desirable to remove inflectional morphology (which does not change the meaning or part of speech of words) but leave derivational morphology behind. For example, in information retrieval if you search for "repurpose" you probable also want to return "repurposing", "repurposes", and "repurposed" but probably not purpose.

To do this, data may be normalized using:
- **stemming** (which “chops off ” inflectional affixes to yield a “stem”) or
- **lemmatization** (which returns the “dictionary” form i.e. “lemma” of a word)

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

## Tasks  📝

### Lemmatization:
- Task-1: transform each word in the file “wiki_mountain_def.txt” into its Lemma form using “built-in lemma_ function of SpaCy”.
- Task-2: how many total words are changed due to this lemmatization process?
 
### Stemming:
- Task-1: transform each word in the file “wiki_mountain_def.txt” into its Stem form 
by coding  only the following rules of Porter Stemming

  - SSES -> SS  || caresses -> caress
  - IES -> I    || ponies -> poni
  - ties -> ti  || SS -> SS
  - caress ->   || Caress S -> 
  - cats -> cat

- Task-2: how many total words are changed due to this stemming process?

## Outputs 📷
1. stemming output
![image](https://github.com/user-attachments/assets/1da402e8-1408-431b-bd9e-a7da8b4ec076)
2. lemmatization output
![image](https://github.com/user-attachments/assets/b38554fd-052b-4c90-a97d-3f72cd14452f)


## How to Run ⚙️

1. Download the stemming.py and lemmatization.py files.
```
 git clone https://github.com/SalwaSh/AI312-Lemmatization-Stemming-Tasks.git
```
**Note: You need to install spacy**

2. To run stemming.py
```
python stemming.py
```
**Note: it takes some time to see the output**

3. To run lemmatization.py
```
python lemmatization.py
```
**Note: it takes some time to see the output**

## Contributor ✍️
- Salwa Shamma
