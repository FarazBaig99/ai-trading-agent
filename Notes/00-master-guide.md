# Trading Master Guide (8 books ka nichor)

> Yeh guide `notes/` folder ki 8 files ka khulasa hai. Har section ke aakhir mein source likha hai, taake detail chahiye ho to us file mein dekh sakein.
>
> **Source ki warning:** Murphy (02) aur Elder (04) wali PDFs asal kitaabein nahi, Bookey summaries hain. In dono ki jo settings/rules PDF mein nahi thay, woh model ki maloomat se bhare gaye hain aur yahan **[verify]** se mark hain. Inhein asal kitaab ya apne charts par khud check karein.
>
> Yeh educational notes hain, financial advice nahi.

---

## 1. Sab se pehle: haqeeqat (reality check)

1. **Trading zero-sum hai, costs ke baad minus-sum.** Jeetne walon ko paisa haarne walon se milta hai, aur broker dono se kamata hai. Zyada tar log haarte hain. (Elder, 04)
2. **Average chartist ki direction ki prediction ~50% sahi hoti hai**, yani sikka uchhalne jaisi. Bank of England ki study mein sirf 1 chartist ne random guess ko consistently haraya. Edge sirf kuch logon ke paas hota hai. (05)
3. **Charts trend mein kaam karte hain, turning points par fail hote hain.** (05)
4. **Charts ki research 1 se 4 hafte ke horizon ki hai.** Seconds ya 1-5 minute ki expiry par predictability ka koi saboot in kitaabon mein nahi hai. (05)
5. **Fixed-payout (binary/digital) trades ka hisaab:** agar jeetne par payout 80% hai aur haarne par poori raqam jaati hai, to sirf barabar rehne ke liye **55.6% trades jeetni zaroori hain**. Payout 85% ho to 54.1%. Yani "50% sahi" ka matlab hai lagataar nuqsan.
   - Formula: zaroori win rate = 1 / (1 + payout). Misaal: 1 / 1.80 = 0.556.
6. **Analysis kami nahi, mind asal masla hai.** Bohot ache analysts bure traders hain. (Douglas, 03)

**Natija:** apna edge saabit karne se pehle demo account par kam az kam 20, behtar hai 100 trades ka record banayein, aur dekhein ke win rate breakeven se upar hai ya nahi.

---

## 2. Teen sutoon: Mind, Method, Money (Elder)

| Sutoon | Matlab | Is guide mein |
|---|---|---|
| **Mind** | Psychology, discipline | Section 9 |
| **Method** | Analysis aur system | Sections 3-7 |
| **Money** | Risk aur position size | Section 8 |
| (4th) **Records** | Har trade ka hisaab | Section 10 |

Teeno mein se ek bhi kamzor ho to baaki do bekaar hain. (04)

---

## 3. Trend: sab se pehla sawal

### 3.1 Trend ki pehchaan
- **Uptrend:** higher highs + higher lows. **Downtrend:** lower highs + lower lows. **Sideways:** dono nahi. (02, 07)
- Market ka taqreeban ek tihai ya us se zyada waqt sideways guzarta hai. Us waqt trend wale tools (MA crossover) whipsaw karte hain. (02)
- **Dow theory ke 3 trend:** primary (mahine/saal), secondary (correction, hafte se mahine, aam taur par pichhli move ka 1/3 se 2/3 wapas), minor (chand din, zyada tar noise). (02, 07)

### 3.2 Multi-timeframe: sab kitaabon ka mushtarka usool
- **Pehle bara timeframe dekho, phir chhota.** Bara timeframe direction deta hai, chhota timeframe entry ka waqt. (Murphy 02, Elder 04, Douglas 03, Cofnas 08)
- **Factor of five (Elder):** timeframes ko ~5 guna ke fark se chunein. Misaal ke taur par:

| Aapki trade | Direction (bara) | Setup | Entry |
|---|---|---|---|
| 1-5 min | 1 ghanta / 30 min | 5 min | 1 min |
| 15 min | 4 ghante | 15-30 min | 5 min |
| Daily | Weekly | Daily | Ghanta |

- **Cofnas (08):** 5-minute trader jo lambe trend ki direction mein trade karta hai, uske jeetne ke chances zyada hain.
- **Nison (01):** major trend ke khilaf reversal signal naye trade ke liye nahi, sirf maujooda trade se nikalne ke liye hai.

### 3.3 Trend ke tools
- **EMA slope (Elder):** EMA upar ja raha ho to sirf buy, neeche ja raha ho to sirf sell. Slope hi asal paigham hai. (04)
- **Trendline:** kam az kam 2 points se banti hai, 3rd touch se confirm hoti hai. Break tab maana jata hai jab **close** line ke paar ho; intraday chhoona kaafi nahi. Bari lines ke liye ~3% filter ya 2 closes ka rule. (02)
- **ADX:** upar jata ADX = trend, MA tools use karein. 20 se neeche ya girta ADX = range, oscillators use karein. (02, 04) [verify: Elder ki 13 setting]

---

## 4. Support, Resistance aur levels

- **Support:** jahan khareedar girawat rok dete hain. **Resistance:** jahan bechne wale tezi rok dete hain. Pichhle peaks aur troughs par lagayein, behtar hai zone ki shakal mein. (02, 04, 07)
- **Mazbooti ke factors:** kitni baar touch hua, kitna waqt wahan guzra, wahan kitna volume tha, kitna recent hai. (02, 04)
- **Role reversal (polarity):** toota hua support resistance ban jata hai aur toota hua resistance support. Wajah: jo log wahan phanse thay, woh breakeven par nikalna chahte hain. (01, 02, 04, 07)
- **Round numbers** (1.1000, 1.1050 waghaira) psychological levels hain. Order un se thora hat kar lagayein. (02)
- **False breakout** sab se ache signals mein se hai: price range se bahar jhaank kar wapas aaye to range ki doosri taraf ke liye trade karein. (Elder 04; Nison ne isay spring/upthrust kaha, 01)
- **Fibonacci retracement:** 38.2%, 50%, 61.8%. Sirf level par pohanchna signal nahi; wahan **candle confirmation ka intezar** karein. Retracement 2/3 se zyada ho jaye to aksar correction nahi, reversal hai. (01, 02)
- **Gaps (windows):** rising window support hai, falling window resistance. Window ka bahar wala kinara close ki bunyad par toot jaye to signal khatam. Forex mein gaps zyada tar weekly open aur news par aate hain. (01, 07)

---

## 5. Candlesticks (Nison, poori kitaab OCR karke padhi gayi)

### 5.1 Bunyadi usool
1. **Context pattern se zyada ahem hai.** Bottom pattern ke liye pehle girawat zaroori hai, top pattern ke liye pehle tezi. Range ke beech mein pattern bekaar hai.
2. **Close ka intezar karein.** Pattern candle band hone par confirm hota hai.
3. **Resistance par bullish pattern ya support par bearish pattern = kharab trade.** Pehle level ke paar close ka intezar karein.
4. **Candles target nahi deteen.** Target Western tools se nikalein (Section 7.3).
5. **"Reversal" ka matlab trend change hai**, zaroori nahi ke ulti direction. Aksar market sideways ho jata hai.
6. **Har trade ka ek level hona chahiye jo saabit kare aap ghalat hain**, aam taur par pattern ka extreme point.

### 5.2 Pattern table

| Pattern | Pehle trend | Signal | Confirmation chahiye? | Stop / level |
|---|---|---|---|---|
| **Hammer** | Neeche | Bullish | Nahi | Hammer ka low |
| **Hanging man** | Upar (lamba) | Bearish | **Haan:** agla close iski body se neeche | Iska high |
| **Inverted hammer** | Neeche | Bullish | **Haan** | Low |
| **Shooting star** | Upar | Bearish | Behtar hai | High |
| **Doji (tezi ke baad)** | Upar | Top ki warning | Close doji se neeche | Doji + pichhli white candle ka high |
| **Doji (girawat ke baad)** | Neeche | Kamzor | Bohot zyada | Sirf support par maane |
| **Bullish engulfing** | Neeche | **Major** reversal | Nahi | Dono candles ka lowest low |
| **Bearish engulfing** | Upar | **Major** reversal | Nahi | Highest high |
| **Piercing** | Neeche | Bullish | 50% se kam ho to pattern nahi | Low |
| **Dark cloud cover** | Upar | Bearish | 50% se kam ho to intezar | High |
| **Harami / harami cross** | Koi bhi | Trend neutral | Behtar hai | Cross zyada taqatwar, khas kar top par |
| **Morning star** | Neeche | **Major** bullish | Nahi | 3 candles ka lowest low |
| **Evening star** | Upar | **Major** bearish | Nahi | 3 candles ka highest high |
| **Three white soldiers** | Neeche/base | Bullish | | Der se milta hai, pullback ka intezar |
| **Three black crows** | Upar | Bearish | | Der se milta hai |
| **Rising/falling three methods** | Trend | Continuation | | Pehli lambi candle ka extreme |

### 5.3 Shakal ke rules (yaad rakhne wale)
- **Hammer / hanging man:** chhoti body upar wale hisse mein, neeche ka saaya body ka **kam az kam 2 guna**, upar saaya na hone ke barabar.
- **Shooting star / inverted hammer:** chhoti body neeche, upar lamba saaya.
- **Engulfing:** doosri candle ki **body** pehli ki poori body ko dhaanp le (saaye zaroori nahi), rang ulta ho.
- **Piercing / dark cloud:** doosri candle pehli body ke **50% se aage** band ho.
- **Forex mein** open aksar pichhle close ke barabar hota hai, is liye gap wale rules (stars waghaira) mein narmi rakhein.

### 5.4 Pattern ko mazboot karne wali cheezein
- Pehli candle chhoti, doosri bohot bari ho.
- Pattern lambi ya tez move ke baad bane (overextended market).
- Doosri candle par volume zyada ho.
- Pattern kisi aur level par bane: support/resistance, trendline, MA, Fibonacci, ya RSI/Stochastic ki extreme zone. Nison ise **convergence** kehte hain: ek jagah jitne zyada signals, utne zyada chances.

### 5.5 Pattern der se mukammal ho to
Hammer ka lamba saaya, star ki teesri lambi candle, ya bara engulfing: entry stop se door ho jaati hai. **Pattern ke support/resistance tak pullback ka intezar karein**, phir entry karein taake stop qareeb ho. (01)

---

## 6. Indicators: settings aur signals

### 6.1 Teen qismein (Elder)
1. **Trend-following** (MA, MACD lines, ADX): trend mein kaam karte hain, range mein whipsaw.
2. **Oscillators** (RSI, Stochastic, MACD-Histogram, Force Index): range mein kaam karte hain, strong trend mein qabl az waqt signal dete hain.
3. Alag qism ke indicators milayein taake ek ki kamzori doosra poori kare. Ek hi qism ke 3 indicators lagana faida nahi deta.

### 6.2 Settings table

| Indicator | Setting | Signal | Source |
|---|---|---|---|
| **EMA (Elder)** | 13 aur 26 | Slope = trend; dono ke beech = "value zone" | 04 [verify] |
| **MA crossover** | 5/20, 10/50, 50/200 (stocks), 4-9-18 (futures) | Chhota upar cross = buy; golden/death cross | 02, 07 |
| **9 EMA** | 9 | Forex mein mashhoor | 01 |
| **RSI** | 14 (tez: 9) | 70/30; strong trend mein 80/20; extreme zone mein divergence sab se ahem | 01, 02, 07 |
| **Stochastic (slow)** | 14,3,3 ya Elder ka 5,3 | 80/20; extreme zone mein divergence; %K-%D cross | 01, 02, 04 [verify] |
| **MACD** | 12, 26, 9 | Lines ka cross, zero line, histogram divergence | 01, 02, 04 |
| **MACD-Histogram** | 12, 26, 9 | Aakhri do bars ka slope: upar = bulls taqatwar | 04 |
| **Bollinger Bands** | 20, 2 SD | Squeeze = bari move aane wali; strong trend mein price band ke saath chalti hai, blindly fade na karein | 02 |
| **Force Index** | 2 EMA (entry), 13 EMA (trend) | Uptrend mein 2-EMA zero se neeche = buy setup | 04 [verify] |
| **ADX** | 14 (Elder: 13) | Upar jata = trend; <20 = range | 02, 04 |
| **CCI** | 20 | ±100 | 02 |
| **Williams %R** | 10-14 | Upar/neeche ke 20% | 02 |

### 6.3 Oscillator ke sunehre rules
- **Trend pehle, oscillator baad mein.** Oscillator trend analysis ke maatahat hai. (02)
- **Uptrend mein sirf oversold buy signals lein**, overbought par short na karein. Downtrend mein ulta. (02, 04)
- **Divergence sab se taqatwar signal hai:**
  - Bullish: price naya low, indicator ka low uncha.
  - Bearish: price naya high, indicator ka high neecha.
  - Elder ka sakht rule: MACD-H dono bottoms ke beech zero cross kare, tabhi divergence valid hai. [verify]
- **Nison:** "har baadal nahi barasta." Overbought/oversold sirf warning (baadal) hai; **candle signal confirmation (baarish) hai.**
- **MACD dheema hai.** Candles aksar MACD cross se pehle mur jaati hain; MACD baad ki tasdeeq ke liye hai. (01)

### 6.4 Elder Impulse System [verify settings]
- 13-EMA slope + MACD-H slope:
  - **Green** (dono upar): short karna mana.
  - **Red** (dono neeche): buy karna mana.
  - **Blue** (ikhtilaf): dono allowed.
- Yeh batata hai ke **kya nahi karna**; buy/sell ka signal nahi.

---

## 7. Chart patterns aur targets

### 7.1 Reversal patterns (02, 07)
- **Head & shoulders:** neckline ke neeche close par mukammal. Target = head se neckline tak ka faasla, breakout point se neeche. Aksar price wapas neckline tak aati hai (doosra mauqa).
- **Inverse H&S:** ulta; breakout par **volume barhna zaroori** hai.
- **Double top (M) / bottom (W):** beech wali trough/peak close se tootay tabhi mukammal. Target = pattern ki unchai.
- Tops jaldi bante hain, bottoms dheere.

### 7.2 Continuation patterns
- **Triangle:** breakout aam taur par base se apex tak ke 2/3 se 3/4 hisse mein. Target = base ki unchai. Ascending = bullish, descending = bearish.
- **Flag / pennant:** tez move (flagpole) ke baad chhota thehrao. Target = flagpole ki lambai, breakout se. Nison ka mohtaat tareeqa: flag ke neeche wale kinare se naapein.
- **Rectangle:** target = range ki unchai.
- **Cup & handle:** lip ke upar pehli candle close hone ka intezar karein. (07)

### 7.3 Target ke tareeqe (candles target nahi deteen)
- Pattern ki unchai, breakout se project karein.
- Agla support/resistance level.
- Channel line (Elder: buy value zone ke qareeb, target upper channel line).
- Swing: C + (B − A).
- **Target nikalne ke liye hai, naye trade ke liye nahi.** (01)

---

## 8. Risk management: sab se ahem section

### 8.1 Rules
| Rule | Matlab | Source |
|---|---|---|
| **2% rule** | Ek trade mein account ka 2% se zyada risk nahi. Professionals 0.25-1% lete hain. | 04 [verify exact], 02 |
| **6% rule** | Mahine ka nuqsan + khuli trades ka risk 6% ho jaye to baaqi mahina naye trade band. | 04 [verify] |
| **Daily stop** | Roz ke nuqsan ki had poori ho to us din trading band. | 06 |
| **Reward:risk** | Kam az kam 2:1, behtar 3:1 (jahan payout fixed na ho). | 02, 03, 04 |
| **Stop entry ke saath** | Stop trade lagate waqt lagayein; sirf trade ki direction mein move karein, kabhi door na karein. | 01, 03, 04 |
| **Averaging down nahi** | Haarti trade mein mazeed paisa daalna inkaar aur ummeed hai, analysis nahi. | 02, 04 |
| **Stress test** | Sochein: bari news ya 20% shock par account ka kya hoga? Jawab "khatam" ho to size kam karein. | 06 |
| **Correlated trades** | EUR/USD long aur GBP/USD long dono asal mein ek hi bara USD short hai. Exposure currency ke hisaab se jodein. | 06 |

### 8.2 Position size (Iron Triangle, Elder)
```
Max risk ($)       = Account × 2%   (ya kam)
Risk per unit      = |Entry − Stop|
Position size      = Max risk ÷ Risk per unit
```
Misaal: $1,000 account, 2% = $20 risk. Entry 1.1000, stop 1.0980 = 20 pips. Size aisa ho ke 20 pips = $20.

**Fixed-payout trades mein** poori lagayi raqam hi risk hai, is liye **ek trade = account ka 1-2%** se zyada nahi.

### 8.3 Drawdown ka hisaab
| Nuqsan | Wapas aane ke liye zaroori faida |
|---|---|
| 10% | 11% |
| 20% | 25% |
| 50% | 100% |

Is liye: **pehle bachaav, phir mustaqil munafa, phir bara munafa.** Is tarteeb ko kabhi ulta na karein. (04)

### 8.4 Stop lagane ke tareeqe
- Market ke noise ke bahar rakhein; round numbers aur sab ko nazar aane wale levels se thora hat kar.
- Pattern ka extreme (hammer ka low, engulfing ka high).
- Pichhli candle ka low/high.
- SafeZone, ATR 1-2 guna. [verify]
- Time stop: trade waqt par na chale to nikal jayein.

---

## 9. Psychology (Douglas + Elder)

### 9.1 Paanch bunyadi sachaiyan (Douglas)
1. **Kuch bhi ho sakta hai.** Koi ek trader kahin bhi aapka edge khatam kar sakta hai.
2. **Paisa banane ke liye yeh jaanna zaroori nahi ke aage kya hoga.**
3. **Kisi bhi edge mein jeet aur haar ki tarteeb random hai.** 20 trades mein 12 jeetengi, lekin kaunsi, yeh nahi pata.
4. **Edge sirf ek baat ke zyada imkaan ka ishara hai**, yaqeen nahi.
5. **Har lamha naya hai.** Pichhli trade agli ka faisla nahi karti.

### 9.2 Consistency ke saat usool
Main consistent winner hoon kyunke:
1. main apna edge objectively pehchanta hoon;
2. har trade ka risk pehle tay karta hoon;
3. risk ko poori tarah qabool karta hoon, ya trade chhor deta hoon;
4. edge par bina hichkichahat amal karta hoon;
5. jab market paisa de to munafa leta hoon;
6. apni ghaltiyon ki taraf jhukao par nazar rakhta hoon;
7. in usoolon ko kabhi nahi todta.

### 9.3 Chaar darr (~95% ghaltiyon ki jar, Douglas)
| Darr | Ghalti |
|---|---|
| Ghalat hone ka | Stop na lagana, nuqsan mein phanse rehna |
| Paisa khone ka | Valid signal par hichkichana |
| Mauqa chhoot jane ka | Signal se pehle kood jana, chase karna, bara size |
| Munafa chhoot jane ka | Munafa na lena, jeeti trade ko haarne dena |

### 9.4 Khatarnaak halaat
- **Jeet ke baad (euphoria):** "kuch ghalat nahi ho sakta", size barha dena. Jeetne ke baad aap **sab se zyada khatre** mein hote hain.
- **Haar ke baad (revenge):** "paisa wapas lena hai", zyada aur bari trades. Market dushman nahi; usay aapse koi gharaz nahi.
- **Gambling ki nishaniyan (Elder):** trade karne ki na rukne wali khwahish, nuqsan ke baad double karna, action ka nasha, nuqsan chhupana.
- **"When in doubt, stay out."** Trade na karna bhi ek position hai.

### 9.5 Rigid rules, flexible expectations
Rules sakht rakhein, ummeedein narm. Aam trader iska ulta karta hai. (03)

### 9.6 20-trade exercise (Douglas)
1. Ek bilkul wazeh system chunein (entry ka rule, stop ka rule, exit ka rule).
2. Agle **20 signals** bilkul usi tarah lein: koi skip nahi, koi tabdeeli nahi.
3. Size itna chhota ho ke **20 ki 20 haar jayein** to bhi aap pareshan na hon (demo account bhi theek hai).
4. Natija ek trade par nahi, poore 20 ke sample par parkhein.
5. Jab 20 trades bina kisi andar ki kashmakash ke ho jayein, tab agle marhale par jayein.

---

## 10. Records (Elder)

Har trade ke liye likhein:
- Tareekh, waqt, pair, direction, expiry/timeframe
- Entry ki wajah (kaunsa setup), screenshot
- Entry, stop, target (ya payout %)
- Natija, aur us waqt ka mood
- Kya rule toota?

Har hafte dekhein: **win rate breakeven (Section 1.5) se upar hai?** Kaunsa setup kaam kar raha hai, kaunsa nahi?

> "Records don't prevent mistakes, but they let you understand and correct them." (Elder ke khayal ka khulasa)

---

## 11. Fundamentals (forex ke liye, 05 + 08)

- **Interest rate ki ummeedein** currency ka sab se bara driver hain. Rate barhne ki ummeed = currency mazboot.
- Central bank ke sarbarahon ke bayanat aur data surprises par nazar rakhein.
- **USD/JPY risk barometer hai:** stocks ke saath chalta hai. Risk-off mein yen mazboot (USD/JPY neeche).
- **Carry trade** ka unwind achanak aur tez hota hai.
- Housing data (starts, permits, NAHB >50, Case-Shiller) rate ki ummeedon ka pehle se ishara deta hai.
- **Bari news (NFP, CPI, central bank faisle) ke waqt chhoti expiry ki trade na kholein.** Pattern news ke saamne bekaar hai. (07, 08)
- Retail trader ko news sab se aakhir mein milti hai; pehle spike ka peecha na karein. (08)

---

## 12. Ek mukammal tareeqa (sab kitaabon ko jor kar)

Yeh ek **educational framework** hai, jeetne ki guarantee nahi. Pehle demo par test karein.

**Trade se pehle (session shuru):**
1. Mood, sehat aur neend theek hai? Nahi to trade na karein. (04)
2. Economic calendar check karein; bari news ke waqt trade nahi. (07, 08)
3. Aaj ki daily loss limit likh lein. (06)

**Har trade ke liye:**
1. **Screen 1, bara timeframe:** trend kya hai? EMA ka slope, higher highs/lows. Trend nahi to range ke rules ya trade nahi.
2. **Screen 2, setup timeframe:** trend ke khilaf pullback hua? (RSI/Stochastic oversold uptrend mein, ya price value zone / support par.)
3. **Level:** pullback kisi support, trendline, Fibonacci ya role-reversal level par hai? (convergence)
4. **Trigger:** wahan trend ki direction mein candle pattern (hammer, bullish engulfing, morning star) **close** hua?
5. **Rukawat:** saamne qareeb mein resistance to nahi?
6. **Risk:** stop/expiry tay, size account ka 1-2%.
7. **Likh lein**, phir trade lein. Phir rules ke mutabiq chhor dein.

**Kab bilkul trade nahi:**
- Bara timeframe saaf nahi.
- Price range ke beech mein hai.
- Indicator ya pattern trend ke khilaf hai.
- Bari news aane wali hai.
- Aaj ki loss limit poori ho chuki hai.
- Aap gusse, josh ya "wapas lena hai" ki halat mein hain.

---

## 13. Murphy ke 10 qanoon (supplemented, [verify])
1. Trend ka naqsha banayein, pehle lamba timeframe.
2. Trend pehchanein aur uske saath chalein.
3. Low aur high dhoondein (support/resistance).
4. Jaanein ke kitna wapas aa sakta hai (retracement).
5. Line kheenchein (trendline).
6. Average ko follow karein (MA).
7. Mor seekhein (oscillators).
8. Warning ki nishaniyan jaanein (MACD, divergence).
9. Trend hai ya nahi? (ADX)
10. Tasdeeq ki nishaniyan jaanein (volume).

---

## 14. Detail kahan milegi

| File | Mauzoo |
|---|---|
| `01-nison-candlesticks.md` | Har candle pattern, windows, convergence, targets |
| `02-murphy-technical-analysis.md` | Dow, trend, patterns, indicators, Elliott, Fibonacci, intermarket |
| `03-douglas-trading-in-the-zone.md` | Psychology, 5 truths, 7 principles, 20-trade exercise |
| `04-elder-new-trading-for-a-living.md` | Triple Screen, Impulse, 2%/6%, stops, records |
| `05-fx-charts-and-fundamentals.md` | Bank of England research: charts kitne kaam karte hain |
| `06-fx-risk-management.md` | Risk ki qismein, limits, stress test |
| `07-fundamentals-of-investments.md` | TA ka bunyadi course, patterns, gaps, RSI |
| `08-excerpt-9781118998656.md` | Forex fundamentals: interest rates, carry, housing |
