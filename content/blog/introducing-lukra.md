---
title: What Lukra is — and why it plans for profit, not just enough feed
eyebrow: Introducing Lukra
stand: Lukra is a profit-maximising feed-budget planner for pasture-based dairy. It plans the whole season at once, with real nutritional modelling and an explicit profit objective — not just matching intake to the feed wedge.
date: 2026-06-01
displayDate: June 2026
seoTitle: "What Is Lukra? Profit-First Dairy Feed Budgeting"
seoDescription: "Lukra is a whole-season feed-budget planner for pasture-based dairy farms that optimises your feeding plan for profit — not just 'enough feed.' See how it works."
ogTitle: "What Lukra is — and why it plans for profit, not just enough feed"
---

Most feed decisions on a pasture-based dairy farm get made one round at a time. You walk the farm, read the **feed wedge** — the ranked picture of how much pasture each paddock is carrying — and judge whether the herd's **dry-matter intake** is about to fall short. If it is, you buy in **supplement** to cover the gap. It works, and for the day-to-day grazing call it's the right tool. But notice the horizon: the question it answers is a short one — *do the cows have enough to eat this fortnight?*

Lukra works at a different level, around a different question: **what feed plan makes the most money across the whole season?**

> "Enough feed" is a constraint, not a goal. Lukra treats it as the floor and optimises for the thing you actually care about — profit.

## What Lukra is, in one line

Lukra is a whole-season feed-budget planner for pasture-based dairy — New Zealand and Australian systems, seasonal calving, twelve monthly periods across the year. You give it your farm, your herd and your feed options; it returns the feeding plan that maximises your annual **margin** (milk income minus feed and the costs that go with it).

The word doing the heavy lifting is *whole-season*. Lukra doesn't optimise this week and hope the rest falls into line. It plans all twelve periods together, because feed decisions are linked across time: condition you put on a cow in autumn is energy she draws on in spring; supplement you commit to in one month changes what's optimal in the next.

It's built first for grazing systems — that's where this post stays — but the modelling isn't fundamentally tied to pasture. In principle it applies just as well to a total mixed ration (TMR) system, where pasture simply becomes one more feed in the mix, or none at all.

## Why "enough feed" isn't the goal

Matching intake to the wedge is really matching feed *supply* to animal *demand* — and topping up with supplement when supply falls short. It's sensible as far as it goes. But it leans on a quiet assumption: that you already know what the demand is.

In practice, demand is set by a **target milk yield**, and that target is usually chosen up front without reference to the economics. Is it the *right* target given today's milk price and the cost of pasture, silage and bought-in feed? Wedge-matching never asks — it feeds to hit a number that may not be the profitable one.

The same blind spot shows up in feed choice. When you're short, the wedge says add supplement, but not *which* one. A cheaper or more energy-dense option might deliver more margin per dollar than the one you reach for out of habit — and you'd never know without comparing the alternatives on the same economic footing.

Because each call is made one round at a time, with no plan for the season sitting above it, the costs compound out of sight: supplement bought reactively when it's dearest; a surplus in one period and a pinch in the next treated as separate problems when they're really one; body condition — which is just stored energy — drifting, instead of being spent and rebuilt deliberately where it pays.

None of this shows up if the only test is "are the cows full." It shows up the moment the test becomes "is this the most profitable plan for the year." Lukra doesn't take the milk target as given — it works out the target, the feeds and the timing together, and picks the combination that pays best.

<div class="note">
  <span class="lbl">TWO LAYERS, ONE GOAL</span>
  A feed wedge is tactical: given where the farm is right now, it guides the day-to-day grazing call. Lukra is strategic: it sets where the farm should be heading across the season — and the target the wedge then works toward. Different layers of the same job, not rival answers to it.
</div>

## Real nutrition under the bonnet

A profit number is only as good as the biology behind it, so Lukra doesn't treat a cow as a tank that's either full or empty. It models how energy is actually spent.

Energy a cow eats is spent in a priority order: **maintenance** first (just staying alive and walking the farm), then **growth** if she's still maturing, then **pregnancy**. What's left over isn't simply "milk" — it gets *split* between milk and body fat, and the split shifts with circumstances. Early in lactation a cow leans hard toward milk (and even draws from condition); later in the season she sets more aside as condition. And the more energy she's fed above her needs, the larger the share that goes to fat rather than milk. That's why feeding more doesn't buy milk one-for-one, and why *when* you feed across the season matters as much as how much.

<details class="deep">
  <summary>Go deeper: how the energy gets partitioned <span class="tag">For beta-testers</span></summary>
  <div class="body">
    <p>For each period, Lukra works in metabolisable energy (ME). Requirements are built up from their components rather than assumed, and met in order:</p>
    <ul>
      <li><strong>Maintenance</strong> scales with liveweight and is paid before anything else.</li>
      <li><strong>Growth</strong> applies to younger stock still reaching mature weight, drawn down as they mature.</li>
      <li><strong>Pregnancy</strong> ramps through gestation, concentrated in the final trimester.</li>
    </ul>
    <p>Energy <em>above</em> those requirements is partitioned between <strong>milk</strong> and <strong>body fat</strong>. The split isn't fixed — it depends on two things: the stage of lactation, and how far intake sits above requirement. Early in lactation the partition favours milk; as the season advances the balance tips toward laying down condition. Independently, the higher the energy intake above requirement, the larger the proportion that goes to fat rather than milk — so milk's response to each extra unit of feed diminishes.</p>
    <p>Body reserves are two-directional: condition gained now can be mobilised later, at a realistic efficiency penalty. That's what lets Lukra deliberately build condition in one period to spend it in another, with the energy accounting carried across the whole twelve-period horizon.</p>
  </div>
</details>

## How it actually chooses a plan

Under the modelling sits an optimiser. Lukra frames the season as a single problem — every feed source, every period, every nutritional and physical limit at once — and solves for the combination that maximises annual margin. It isn't picking a plan from a shortlist or following a rule of thumb; it's searching the full space of feasible plans and returning the best one.

And it gives you more than the plan. Because of how the problem is solved, Lukra can also tell you what each binding limit is *costing* you — the value of one more tonne of pasture, say, or one more day a feed is available — and the price at which a feed you're not using would become worth including (or one you are using would drop out). That turns the answer from a single recommendation into something you can interrogate and pressure-test against your own prices.

<details class="deep">
  <summary>Go deeper: the optimisation, briefly <span class="tag">For beta-testers</span></summary>
  <div class="body">
    <p>The engine is a linear program (LP). The objective is annual margin — milk income minus feed and associated costs. The decision variables are how much of each feed source to allocate in each of the twelve periods.</p>
    <p>The constraints are the realism: energy requirements must be met in every period (the "enough feed" floor), intake can't exceed what a cow can physically eat, feed availability is bounded, and the nutritional accounting above ties periods together. The LP respects all of it simultaneously and returns the global best plan for the season — not a locally sensible decision that looks fine this round but costs you later.</p>
    <p>A useful by-product of solving an LP is its <strong>dual information</strong>. Shadow prices put a value on each binding constraint — how much annual margin would change if that limit eased by one unit (an extra tonne of available pasture, more grazing days, a higher intake ceiling). Reduced costs do the same for feeds left out of the plan: how much cheaper a feed would have to get before it earns a place, or how much dearer before one currently used drops out. So beyond the plan itself, Lukra shows you where the binding limits are and at what prices the answer would change.</p>
  </div>
</details>

## Where the feed wedge fits

None of this makes the feed wedge wrong — it makes it *tactical*. A wedge is the right tool for the day-to-day decision: given the cover you've got right now, how much to graze, which paddocks, when to step in with supplement. What it can't do on its own is tell you what to aim for. It needs a target — a target milk yield, or a target pasture intake per period — and that target has to come from somewhere.

That's the layer Lukra sits in. It works out the strategic targets for the season — what production is worth chasing given prices and feed costs, how much pasture to plan to harvest in each period — and hands them down as the inputs a wedge tool runs on. With the target set, the wedge does what it does best: turn live pasture data into a sound grazing call, day by day.

This is why Lukra doesn't compete with pasture-measurement tools — from a rising plate meter, to a towed or drive-over pasture meter, to the apps that turn cover readings into a feed wedge. It complements them. Once your pasture allowance is known, the open questions are exactly the ones Lukra answers: which supplements to buy, in what quantities, in which periods, and how to react when prices shift. Lukra sets the course for the season; pasture measurement helps you sail it — and the better that measurement, the sharper Lukra's answers.

Tighter, more automatic links to whatever you already use to measure pasture are a natural next step for us.

## Built on a validated model

A profit optimiser is only trustworthy if its underlying nutrition is right, so we checked it against the standards the industry already trusts. Lukra's milk predictions were validated against **NRC 2001** and **NASEM 2021** across nine New Zealand scenarios — three breeds, both heifers and mature cows. In every run the predictions landed within a few percent of one of those standards. The single larger divergence, a Kiwi Cross heifer, is understood and explained rather than papered over. If you want the detail, it's the subject of [our validation post](/blog/validating-lukra).

<div class="note warm">
  <span class="lbl">HONESTLY</span>
  Lukra plans for profit, but it can't promise a number for your farm — that depends on your prices, your pasture and your herd. What it does promise is that the plan it gives you is the most profitable one its model can find, with the nutrition checked against recognised standards.
</div>

## The short version

The feed wedge is the right tool for today's grazing call, but it can't tell you what to aim for. Lukra supplies that: it plans the whole year at once, accounts for energy the way a cow actually uses it, and optimises explicitly for margin — then hands the targets down to the tools that run your day-to-day. Strategy from Lukra, execution at the wedge, working toward the same number.

Smarter feeding. Greater profit.
