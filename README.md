# Otta - Engineering Interview Task

This is the take-home interview task for engineering job applications at Otta.

The goal is to both give you a flavour of the kind of work we do, and give us an idea of your technical (and non-technical) skills.

We expect the task to take one hour. If you require clarification on anything, please don't hesitate to contact us.

## Instructions

Start by cloning this repository using your personal GitHub account. Create a new private repository and push your clone to this new repo (you will need to remove the original remote with `git remote remove origin`). Please ensure all of your work is committed to this - we'll only consider the `master` branch.

The following details the individual tasks. Please complete **all** of the them. You may use any programming language, provided all of the code used can be committed to this repo.

### Task 1

In the `data` folder of this repo there is a CSV file called `reactions.csv`. It contains real data corresponding to how users on Otta have reacted to (saved or discarded) jobs on the platform.

The reaction data consists of four columns:

- `user_id` - the integer ID of the user who liked or disliked the job
- `job_id` - the integer ID of the job the user interacted with
- `direction` - whether the user liked (`true`) or disliked (`false`) the job
- `time` - the timestamp corresponding to when they reacted to the job

**Task**: The similarity score between two users is the number of jobs which they both like. Find the two users with the highest similarity.

**Answer**: Similarity score **181** between users **5193** & **1791**

### Task 2

In the `data` folder there is an additional CSV file called `jobs.csv`. It contains unique integer IDs for over 12,000 jobs, along with integer IDs for the job's associated company.

**Task**: The similarity score between two companies is the number of users who like at least one job at both companies. Using both the `reactions.csv` and `jobs.csv` data, find the two companies with the highest similarity score.

**Answer**: Similarity Score **104** between companies **92** & **46**

### Task 3

Engineering at Otta is truly full-stack. Features are owned end-to-end, from backend and database-level work to front-end finishes.

We don't think it's fair to ask you to build something with a UI, as we know this can take a while and time is precious. Instead, we'd love to see an example of something you've already built and hear about what you learned building it.

**Task**: Share an example of something you've built using front-end web technologies.

- A link to a GitHub repo is ideal
- If the best example of your work is something you've done at a company, it's okay to link to a live deployed version
- If you can't link to anything, a screenshot is also fine

**Answer**: _[Add a link to repo/website/screenshot here]_
![Before](/screenshots/before.png "Before")
![After](/screenshots/screenshot_1.png "After 1")
![After](/screenshots/screenshot_1.png "After 2")


**Task**: Tell us about the biggest challenge you faced in building the above.

**Answer**: _The biggest challenge that I faced when redesigning the category page was trying to cater for the various stakeholders coupled with aiming to improve user conversion on the page itself. As can be seen in the screenshot of the page prior to development there was a lot to be desired from the list of offers at the bottom, which only saw about 10% of the overall interactions on the page._ 

_Trying to bring utility to users such that there was a “journey of exploration” that they would want to take was an incredibly difficult and ambiguous task. However, through rapidly experimenting with different filters, measuring engagement rates as set primary & secondary filters were put in place._

_Regarding the placements that sit at the top of the page, it was a difficult task to meet the merchant team requirements yet clean it up such that it wouldn’t take up the majority of real estate. Using split test and focus groups I built out a system which would allow the site management team to display at most 3 rows of promotions. This was technically difficult to build as it required development across multiple codebases in a plethora of languages. Admittedly there were quite a few things that went wrong in the early stages of development as testing was just something that was done on the fly. However, towards the end I created a robust testing framework that was followed by the rest of my pod when working on this._

_Overall engagement with the page increased by 25% and there is now a 40:60 split between the placements at the top of the page and the list of offers._

## Submission

Once you've completed all of the above tasks, make sure:

- [ ] You've committed all of the code used, and your edited answers, to the `master` branch
- [ ] You've pushed the changes to your repo
- [ ] You add `XavKearney` and `shfranklin` as contributors for your personal repo, and send a link to the repo in an email to us

Good luck!
