# Immigrant Calculator
## _Calculating family expenses in immigration can be quite tricky..._
<img align="right" src="https://github.com/Neuka/ImmigrantCalculator/blob/main/photo_2023-07-21_13-35-34.jpg" width=300 />

Hey there,
I've put together a simple calculator code for our family to help us with our weekly expenses. It's a small project and actually my first expirience at programming.
This README is also for practice, jaja 😏


> When we arrived in Argentina, we encountered some challenges with currency exchanges.
> 
> There are various exchange rates for the dollar, depending on whether we exchange cash, cryptocurrencies, or use automatic conversion from a bank card.
> 
> Considering inflation in Argentina, these differences can have a massive impact on the final amount. The exchange rate changes every week, sometimes significantly - so there is a need to adjust it before each report.

## How it works and why

<li>rate_something - exchange rates from various sources: crypto or bank of Georgia (BoG) autoexchange</li>

<li>somebody_cash & somebody_bog - expenses per week, depending on how they were paid. I also put payments through the card of local banks in cash variable, since the money comes there from the exchange of crypto.</li>

<li>nastya_bog_sum - deposit of money that Nastya put on my card. There are difficulties with payment from her bank of georgia card, so we use mine for daily payments.</li>

<li>N_delta - a variable for the loop below, in case one of us (Nastya actually...) paid more.</li>

Loop considers the overall count and automates the calculation of who owes how much to whom by the end of the week.
At the end we have a total like this:

<img align="center" src="https://github.com/Neuka/ImmigrantCalculator/blob/main/result%20of%20work.jpg" width=300 />
