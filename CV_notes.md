Minden minta = (valóság, modell_predikció)

TP = valós pozitív + predikció pozitív
TN = valós negatív + predikció negatív
FP = valós negatív + predikció pozitív
FN = valós pozitív + predikció negatív

Először mindig darabszámot számolunk.
Utána metrikát számolunk.

Az adatot k részre osztjuk.
k-1 részen tanítunk.
1 részen tesztelünk.
Ezt k-szor ismételjük.
A metrikákat átlagoljuk.

CV célja: stabilabb, megbízhatóbb teljesítménymérés.

CV = k-szoros mérés, minden minta egyszer teszt → átlagolás
Cél: torzítás / véletlen anomália kiszűrése

CV alatt metrikák:
- cross_val_score → alapból accuracy
- make_scorer(recall_score) → CV recall mérés
- pos_label → melyik labelt tekintjük "pozitívnak"
- CV célja: minden fold, majd átlag

CV saját datasettel:
- Fold = 5 (vagy ahogy szeretnéd)
- TP/TN/FP/FN soronként
- make_scorer(recall_score/precision_score) → spam-re
- CV output = foldonkénti scores + átlag
- Ellenőrzi a modell stabilitását

CV eredmények értelmezése:
- Accuracy ~0.98 → átlagosan mennyire pontos a modell
- Recall ~0.966 → hány valós spam-et talál meg
- Precision 1.0 → ami spam volt, az mind spamnek lett jósolva
- Megfigyelés: néha spam-et kihagy (FN), de téves pozitív nincs (FP=0)

- Recall javítása: több valós spam-et találjon meg
- Stratified CV: minden fold-ban hasonló ham/spam arány
- Class weighting: a ritkább osztályra nagyobb súlyt adni a modellezésnél
- Threshold tuning: LogisticRegression predikció küszöb módosítása
- CV során minden módosítás után újra mérni recall-t és precision-t