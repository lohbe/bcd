# Worked example — 2026-08-04

## Goal
<!-- What concept/skill is today's worked example targeting? -->
vllm

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
vllm inference - sampling params

## Worked example
<!-- The worked example / code goes here or in a sibling file -->

Q: Are there only about 151K vocabulary tokens an LLM has, even in a frontier model
A: no, it varies.

Q: How to reason about logits → temperature scaling → top-k cut → top-p cut → greedy or random sample
A:

Think of the pipeline from raw model outputs to the final picked word as a funnel.
At the start, the model hasn't "chosen" anything yet—it has just calculated a raw, unnormalized score for every single word in its vocabulary. The sampling pipeline progressively cleans, shapes, and filters these scores until only one token remains.
Here is the exact step-by-step mental model for how text generation actually happens under the hood.
The Pipeline at a Glance
 [ Raw Logits ]  -->  [ Temperature ]  -->  [ Softmax (Probs) ]  -->  [ Top-K Cut ]  -->  [ Top-P Cut ]  -->  [ Sample/Greedy ]
  (Raw scores)       (Rescale curve)      (Convert to %)        (Keep top K)        (Keep top Cumulative %)  (Pick 1 Token)

Step 1: Raw Logits (z)
⚬ What they are: Unbounded real numbers (e.g., [-10.2, 3.1, 8.5, ...]) assigned to every token in the vocabulary.
⚬ Mental Model: Uncalibrated votes. Higher means the model thinks the word fits, but they aren't probabilities yet.
Step 2: Temperature Scaling (T)
⚬ What it does: Modifies the logits before converting them to probabilities by dividing each logit by T:  $$z_i' = \frac{z_i}{T}$$
⚬ Mental Model: The "Confidence Adjuster". ⚬ T < 1.0 (Cold): Divides logits by a fraction, making high logits much higher relative to low ones. The distribution becomes sharp/peaked. The model gets confident and predictable. ⚬ T = 1.0 (Neutral): Leaves logits untouched. ⚬ T > 1.0 (Hot): Shrinks the gap between high and low logits. The distribution flattens out, giving lower-ranked tokens a much higher chance. The model gets creative (and potentially nonsensical).
Note: Right after temperature scaling, a Softmax function is applied to turn these scaled logits into probabilities that sum up to 100% (1.0).
Step 3: Top-K Filtering
⚬ What it does: Takes the top K most probable tokens and discards all the rest (sets their probability to 0).
⚬ Mental Model: The "Hard Bouncer". ⚬ If K = 50, the model will strictly only look at the 50 most likely candidate tokens, regardless of how good or bad candidate #51 is. ⚬ Why use it? It prevents the model from picking completely bizarre, low-ranked tail tokens that make no sense in context.
Step 4: Top-P Filtering (Nucleus Sampling)
⚬ What it does: Dynamically sorts remaining tokens from highest to lowest probability, then keeps only the smallest set of tokens whose cumulative probability adds up to P (e.g., 0.90 or 90%).
⚬ Mental Model: The "Context-Aware Bouncer". ⚬ Unlike Top-K (which always keeps a fixed count), Top-P adapts based on how confident the model is: ⚬ High certainty context (e.g., "The cat sat on the..."): The top 2 tokens might already account for 90% of the probability, so Top-P drops everything else. ⚬ Uncertain context (e.g., "Once upon a time, in a..."): It might take 100 different tokens to sum up to 90%, so Top-P keeps a larger set.
Order matters! Usually, Top-K runs first to quickly trim the absolute bottom-tier tokens, and then Top-P runs second to dynamically adjust the candidate pool based on context certainty. Remaining probabilities are re-normalized to sum to 1.0 after filtering.
Step 5: Final Selection (Greedy vs. Random Sample)
Now that you have a short, cleaned-up list of valid candidates and their normalized probabilities, you choose how to pick the winner:
1. Greedy Decoding (T = 0)
⚬ How it works: Always picks the candidate with the absolute highest probability (argmax).
⚬ When to use: Math, code generation, factual Q&A, or tasks where there is a single correct/deterministic answer.
2. Random Categorical Sampling (T > 0)
⚬ How it works: Rolls a weighted die based on the remaining candidate probabilities. If Word A has a 70% chance and Word B has a 20% chance, Word A will be picked 70% of the time, but Word B still has a shot.
⚬ When to use: Creative writing, brainstorming, roleplay, or conversational chat where you want variety and flair.
Summary Mental Cheat-Sheet
Hyperparameter	Question it Answers	Primary Goal
Temperature	How sharp/flat should the probability curve be?	Controls baseline randomness vs. determinism.
Top-K	What is the maximum number of candidates allowed?	Cuts off the extreme "long tail" of bad choices.
Top-P	How much cumulative probability mass should we keep?	Dynamically shrinks or expands options based on context confidence.
Greedy/Sample	Do we take the guaranteed top choice, or roll the die?	Final action to output a token.

## Reflection
<!-- What did you learn? What was hard? -->
i learnt about the chain of events for each inference token. it is good to know, because sampling parameters alter the characteristics of outputs (dynamic). only model weights are fixed.
