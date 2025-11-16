Python: Premium vs Standard Conversion Lift (1 mark)
HoloMart: Premium Upsell Signal
HoloMart runs six months of multichannel campaigns. Executives want to know which channel converts Premium shoppers best relative to Standard shoppers so they can reassign budget and refine the vibe analysis prompts for automated campaign ideation.

Dataset
month: Cohort month for attribution
channel: Channel name
segment: Standard or Premium subscriber tier
sessions: Total visits attributed to the channel
conversions: Transactions attributed to the channel
Your Python task
Load the CSV into Pandas.
Aggregate by channel and segment to compute total sessions & conversions.
Calculate conversion rates (conversions ÷ sessions) per channel/segment.
Pivot to compare Premium vs Standard and compute the lift: Premium - Standard.
Return the channel with the largest positive lift.
Download the marketing performance log: 

Which channel shows the greatest Premium uplift over Standard conversion rate?
Affiliate
Correct
Use Pandas pivoting (pivot_table) or groupby with unstack to compare the segments.

----------------------------------------------------------------------------------------

Here’s the short, simple explanation of what this question means and what your teacher wants you to learn:

✅ What the question is about — In Simple Words

You have marketing data from different channels (like Email, Search, Social, Affiliate).

Each channel has results for two customer types:

Standard shoppers

Premium shoppers

Your goal:
👉 Find which channel converts Premium shoppers better than Standard shoppers.

This difference is called conversion lift.

✅ What your teacher is trying to teach you

Your teacher wants you to learn four core data-analysis skills using Python + Pandas:

1. Loading real marketing data

Using Pandas to read a CSV file.

2. Grouping & aggregating data

Summarizing values by channel + customer segment.

3. Calculating ratios

Computing conversion rate = conversions / sessions.

4. Using pivot tables

So you can compare:

| Channel | Standard CR | Premium CR |

5. Identifying uplift

Premium uplift = Premium CR − Standard CR
Then picking the highest uplift channel.

🧠 Why this is important

This is how real marketing teams measure:

Which channel brings high-value (Premium) customers

How to reallocate marketing spend

Which messages work better for Premium shoppers

This is also very common in:

✔ Growth marketing
✔ Product analytics
✔ Customer segmentation
✔ Business intelligence

🎯 Short answer

Your teacher is teaching you:

👉 How to analyze segmented marketing performance and find which channel shows the strongest uplift for Premium users using Pandas.