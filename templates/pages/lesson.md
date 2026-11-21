# Delivery lesson authoring template

Write each lesson into a `content/[0-9][0-9]-*.json` array. Keep the ID stable when a title changes.

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

## Detail and cross-cutting lessons

Existing pages default to `overview`. A `deep-dive` names its overview `parent`. A `flow` lists the lesson IDs it `touches`. Add `audience` and ordered `detail` sections with stable IDs, titles and blocks. Use text, ordered or unordered lists, captioned tables, code with a language and caption, figures with alt text and a full text equivalent, and labelled callouts. Label stack-dependent code illustrative. Use a dedicated `worked-failure` section.

Before review, identify (1) trigger, location and duration, (2) inputs and permissions, (3) sample settings, (4) observed output, (5) pass rule and its owner, (6) failure responder and first action, (7) Jira record, link and status, (8) failure from the shared fictional dataset, (9) two mistakes and their consequences, (10) Principle, Tool behavior and Team policy callouts, (11) what transfers, and (12) at least two checked primary sources. See project/DEPTH-PLAN.md sections 4 and 5.

For every lesson that describes Kiwi behavior, include the version and evidence basis in the reader-facing text. For the currently checked example use: “Kiwi TCMS 17.2 behavior is drawn from its documentation and published source code. This example has not been demonstrated on a live Kiwi TCMS and Jira setup.” Recheck the cited version when revising the example.

Open every deep dive with two or three plain-language sentences a business analyst can follow. Define specialist terms on first use, including on direct entry to the lesson. When an example uses a custom script, name a real off-the-shelf equivalent in “What transfers”, verify its documentation, and identify any material difference in inputs or enforcement.
