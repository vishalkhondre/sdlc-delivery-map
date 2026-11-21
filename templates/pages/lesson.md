# Delivery lesson authoring template

Write each lesson into a `content/0*.json` array. Keep the ID stable when a title changes.

| Key | Question to answer |
| --- | --- |
| id, title, phase | Where does this topic sit and what permanent link identifies it? |
| summary | What does the reader learn to decide, build, verify or restore? |
| owner | Which role acts and which person or tool receives the result? |
| inputs | What artifacts, signals or policy information start the work? |
| steps | What actions make the outcome repeatable? |
| evidence | What record would let someone verify the handoff later? |
| example | How does the fictional approval-routing feature exercise the decision? |
| failure | What is held, repaired or requalified when it fails? |
| measure | Which observation would show that the practice works? |
| sources | Which public primary references support the explanation? Supply title and HTTPS URL. |

Use a list of strings for inputs and steps, an array of reference objects for sources and strings for all other fields.
