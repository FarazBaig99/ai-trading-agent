# 05 – Charts and Fundamentals in the Foreign Exchange Market

**Source:** H. L. Allen & M. P. Taylor, *Charts and Fundamentals in the Foreign Exchange Market*, Bank of England Discussion Paper No. 40, August 1989 (55 pp. incl. tables, appendix, references). Read in full.

**What it is:** an empirical study of chart (technical) analysis in the London FX market, based on (1) a questionnaire answered by 200+ chief FX dealers and (2) a weekly panel of chartists' 1-week and 4-week forecasts for GBP/USD, USD/DEM and USD/JPY, June 1988 to March 1989.

---

## 1. Background and motivation

- Post-war economics mostly assumed asset prices reflect **fundamentals only** (efficient markets). One consequence: non-fundamental traders should lose money and disappear (Friedman 1953, Fama 1965).
- Practitioners never fully accepted this. Traders keep making abnormal profits, and the data keep producing anomalies:
  - Stock markets are more volatile than fundamentals justify (Shiller 1981).
  - Forward FX rates are poor predictors of future spot rates.
  - Floating exchange rates are extremely volatile.
  - **Meese & Rogoff (1983):** economic exchange-rate models could not beat a simple **random walk** out of sample.
- Newer "noise trader" models (De Long et al. 1987, Black 1986, Kyle 1985) let fundamentalists and non-fundamentalists co-exist. Noise trading can earn positive returns, and it can pay fundamentalists to anticipate and partly copy noise traders.
- Definitions used:
  - **Noise trader:** anyone whose strategy ignores fundamentals.
  - **Chartist / technical analyst:** someone who trades on analysis and extrapolation of past prices only.
  - **Fundamentalist:** someone who looks at the reasons behind price moves (economic data, interest rates, etc.).

## 2. What chart analysis is (as the paper describes it)

- Core belief: the price already **discounts all information**, rational or not, so studying price alone is enough.
- Tools:
  - **Pattern recognition.** Reversal patterns (head and shoulders, double/triple tops) and continuation patterns (triangles).
  - **Support and resistance.** The lower and upper bounds of a trading range.
  - **Mechanical indicators:**
    - *Trend-following*, e.g. "buy when the short moving average crosses above the long one".
    - *Non-trend-following oscillators*, i.e. rate-of-change measures flagging overbought/oversold.
  - **Non-price inputs.** Sentiment surveys (often used contrarian: overwhelming bullishness suggests selling), interest-rate charts, market indices.
- Chart analysis is highly **subjective**, an "art form". There are as many methods as chartists.

## 3. Survey findings (200+ London chief dealers)

### Use depends on time horizon
| Horizon | Finding |
|---|---|
| Intraday to 1 week | ~**90%** use some chart input; **60%** rate charts at least as important as fundamentals |
| 1–3 months | Fundamentals gain weight |
| 6 months–1 year | Fundamentals dominate further |
| 1 year+ | ~**30%** use pure fundamentals; **85%** rate fundamentals above charts |
| All horizons | A steady **~2%** are "pure chartists" who never use fundamentals |

- **Why:** at short horizons there is little fresh economic data, and charts capture swings in market psychology. Over long horizons, fundamentals take over.

### Charts vs fundamentals: complementary, not competing
- Only **8%** saw the two as mutually exclusive. The rest saw them as complements to some degree.
- Common practice: use charts to **confirm** the fundamental view, not to contradict it.
  - Interbank attitude quoted: if the technical view agrees, double the position; if it disagrees, ignore it.
  - Customer desks use fundamentals for direction and charts to answer "by how much?", i.e. targets and levels.
- This contradicts Frankel & Froot (1986b), who modelled chartists and fundamentalists as competitors.

### Self-fulfilling prophecy
- ~**40%** said explicitly that charts are partly **self-fulfilling**: they work because so many people watch them.
- Even fundamentalist dealers said they **must know chart signals** because those signals move other participants.
- One view: charts **delay** fundamentals in the short run. The skill is spotting when the chart picture breaks and price catches up with fundamentals, which produces "fads".

### Sources and tools
- 25% employ in-house technical analysts (vs 38% with in-house economists).
- 21% use outside chartist firms; 43% subscribe to chartist publications.
- **74%** use online data and charting services. This is by far the main source.
- **~65%** use trend-following systems such as moving averages. **40%** combine them with overbought/oversold oscillators.

## 4. Panel of chartists' forecasts (June 1988 – March 1989)

- Respected City chartists were phoned every Thursday for 1-week and 4-week forecasts on $/£, DM/$ and ¥/$. Between 10 and 20 responded each week.
- **Visual findings:**
  1. Errors are much larger at 4 weeks than at 1 week.
  2. Forecasts **miss turning points**. Errors shrink while the market is trending.
  3. Chartists **under-predict in rising markets and over-predict in falling ones**. Expectations are **inelastic**: a 1% move produces less than a 1% revision in the forecast.

### Bias and directional accuracy
- **Unconditional bias** (test: regress forecast error on a constant). No bias at 4 weeks. Some chartists were biased at 1 week, especially on DM/$.
- **Directional ("qualitative") accuracy**, i.e. % of correct up/down calls, was roughly a coin flip:

| | $/£ 1w | DM/$ 1w | ¥/$ 1w | $/£ 4w | DM/$ 4w | ¥/$ 4w |
|---|---|---|---|---|---|---|
| Average accuracy | 51% | 57% | 51% | 46% | 47% | 49% |
| Best individual (L) | 57 | 66 | 51 | 57 | 66 | 69 |

- Accuracy rose when a clear trend was in place and fell right after trend changes. For example, DM/$ 1-week accuracy jumped when a downtrend set in (Sep–Oct) and collapsed when the dollar turned up (Dec). This is more evidence that **chartists are good in trends and bad at turns**.

## 5. Are some chartists systematically better? (non-parametric test)

- Method: the **Friedman two-way analysis of variance by ranks**. At each date, currency and horizon, forecasters are ranked by absolute error (1 = best).
  - Rank sum per forecaster: r_l = Σ over horizons, currencies and dates of r_ijkl.
  - Under the null of no skill difference, expected rank sum = 3T(n+1) and variance = Tn(n+1)/2.
  - Test statistic φ = Σ [r_l − 3T(n+1)]² / [Tn(n+1)/2], which is χ² with n−1 degrees of freedom.
- **Result:** differences across the panel were significant at 10% (just short of 5%). Since rank tests have low power, the authors read this as real evidence of skill differences.
- One forecaster (M) was **better than the group at the 1% level**. Caveat: with many forecasters, someone will look good by chance (pre-test bias).
- **Takeaway:** chartists are **not a homogeneous group**. Methods and skill differ a lot.

## 6. Chartists vs other forecasting methods (% RMSE, log data)

**1-week ahead (RMSE %):**
| Method | $/£ | DM/$ | ¥/$ |
|---|---|---|---|
| Chartist M (best) | 1.21 | **1.30** | 1.33 |
| Median chartist | 1.28 | 1.33 | 1.38 |
| Random walk | 1.25 | 1.38 | 1.35 |
| ARIMA | 1.77 | 2.05 | 2.17 |
| Currency VAR (Bayesian) | **1.05** | 1.37 | 1.29 |
| Economic VAR (Bayesian) | 1.12 | 1.39 | **1.23** |
| Worst chartists (A/F) | ~1.95–1.98 | 1.46–1.85 | ~2.0 |

**4-week ahead (RMSE %):**
| Method | $/£ | DM/$ | ¥/$ |
|---|---|---|---|
| Chartist M | **2.37** | **2.84** | **2.71** |
| Median chartist | 3.00 | 3.38 | 3.33 |
| Random walk | 2.81 | 3.18 | 3.12 |
| Forward rate | 2.71 | 3.07 | 3.10 |
| ARIMA | 4.14 | 4.94 | 4.64 |
| Bayesian VARs | 2.55–3.76 | 3.76 | 3.04–3.28 |

**Key findings:**
- Individual chartists vary widely. The **median (consensus) chartist beats most individual chartists**.
- The median chartist **generally does not beat the random walk**.
- **Chartist M beat the random walk consistently**, and at 4 weeks beat every alternative on every currency. This matters because Meese & Rogoff found no economic model could beat a random walk.
- **ARIMA did worse than most chartists.** Chartism is more than "eyeball Box-Jenkins" extrapolation.
- Unrestricted VARs did badly (too many parameters). Bayesian-restricted VARs did well at 1 week.
- The forward rate performed about as well as a random walk.
- **Bottom line on TA vs FA in FX (1988–89 sample):** the best chartists beat both the random walk and the economic and statistical models over 1–4 weeks. The average chartist does not.

## 7. Do chartists destabilise the market?

Expectation models tested (s = log spot rate; tS^e_{t+n} = expected rate made at time t; S̄ = equilibrium rate):

| Model | Formula | Elasticity of expectations |
|---|---|---|
| Static | S^e − S_t = 0 | = 1 (random walk) |
| **Bandwagon** | S^e − S_t = αΔS_t, α > 0 | **> 1, destabilising** |
| Extrapolative | S^e = (1−β)S_t + βS_{t−1}, 0<β<1 | < 1 |
| Adaptive | S^e_t = S^e_{t−n} + γ(S_t − S^e_{t−n}) | < 1 |
| Regressive | S^e − S_t = −θ(S_t − S̄), θ > 0 | < 1 (mean-reverting) |

- **Test regressions:**
  - Bandwagon/extrapolative: regress (S^e − S_t) on ΔS_t. A positive slope means bandwagon; a negative slope means extrapolative.
  - Adaptive: regress on the previous forecast error.
  - Regressive: regress on S_t. A negative slope means regressive. Because spot FX is I(1), use Dickey-Fuller critical values: −2.93 at 5%.
- **Results:**
  - At 1 week, most chartists could not reject static expectations.
  - Chartists A and M (the most distinctive) often showed **inelastic** expectations (adaptive, regressive or extrapolative).
  - **Bandwagon expectations were never accepted, for any chartist at any horizon.**
- **Conclusion:** chartist advice is **not intrinsically destabilising**. It is unlikely to cause explosive **bubbles**. At most it may cause **temporary, mean-reverting deviations ("fads")** from fundamentals.

## 8. Caveats the authors list

- Small sample over a short period (~9 months), so results are tentative.
- Many chartists prefer to set ranges and levels ("set the parameters") rather than give point forecasts.
- The study measured **accuracy, not profitability**. These are probably correlated but are not the same thing.
- Only 1- and 4-week horizons were studied. Intraday use and any short-term volatility it causes were **not** examined.

## 9. Appendix: chartist methodology summary

- **Daily bar chart:** a vertical bar for the day's range with a tick for the close. (Spot FX had no volume data.)
- **Trendlines:**
  - An up-trendline joins higher lows; a down-trendline joins lower highs.
  - A break is an early reversal warning: breaking an up-line is a sell signal, breaking a down-line is a buy signal.
  - Confirmation filters: e.g. **2 closes beyond the line** or a minimum % move.
- **Trading range:** sideways peaks and troughs bounded by support (lows) and resistance (highs).
- **Head and shoulders:**
  - Left shoulder A, head B, right shoulder C, with the neckline under A and C.
  - The reversal is confirmed when price makes a peak **below** the neckline (point D).
  - Variants: inverse H&S at bottoms; complex H&S; triple top (all peaks equal); double top (two equal peaks).
- **Triangles (continuation):**
  - Symmetric: two converging lines.
  - Ascending: rising lower line and flat top.
  - Descending: falling upper line and flat bottom.
- **Problems with patterns:**
  - Subjective; real patterns rarely match the textbook.
  - **Easy to see after the fact, hard to see in real time.**
  - So analysts add mechanical indicators: MA crosses of price or of two MAs, and rate-of-change extremes that suggest a reversal.
- Pure "anonymous chart" charting is rare. Experienced chartists say each market has its own pattern behaviour, and some markets do not chart well.
- The most common real-world style is pragmatic: look at many indicators and follow the majority signal.
- Footnote: earlier studies (Goodman 1979/80) found **technical advisory services consistently beat the forward rate**, while econometric/fundamental services did not.

---

## 10. Practical takeaways for a short-term trader

1. **At short horizons, technical analysis is what most professionals actually use.** About 90% of dealers use charts for intraday-to-1-week calls, so the levels that crowd watches (support/resistance, trendlines, MA crosses, round numbers) can move price because they are self-fulfilling.
2. **Use fundamentals for direction and charts for timing and levels.** Treat a chart signal that agrees with the fundamental or trend bias as higher quality. Be sceptical of signals that fight it.
3. **Chart forecasts work in trends and fail at turning points.** Expect to be wrong right after a trend change. Reduce size or wait for confirmation (e.g. 2 closes beyond a level) when a trend looks exhausted.
4. **The average chartist is about a coin flip on direction** (about 50% hit rate). An edge exists only for a minority. Keep a written record of your own hit rate and RMSE against a "no-change" benchmark (random walk). If you cannot beat it, you have no edge.
5. **The consensus beats most individuals.** Survey and median views are a useful sanity check against your own idiosyncratic read.
6. **Professional expectations are inelastic.** Pros under-react to recent moves (they under-forecast rallies and sell-offs), which leaves room for momentum continuation inside trends.
7. **Prices can deviate from fundamentals temporarily ("fads") but tend to revert.** Very short-term moves driven by charts can snap back when fundamentals reassert themselves.
8. **Pattern recognition is subjective and easy only in hindsight.** Pair it with objective, rule-based triggers such as MA crossovers and oscillator extremes.
9. **Caution for very short expiries (e.g. minute-level binary/turbo options):** this study covered 1–4 week horizons only. It provides **no evidence** of predictability at seconds-to-minutes horizons, where transaction costs and payout structure matter more.
