hemoglob = float(input("Anna Hemoglobiini: "))
sukupuoli= (input("Oletko mies vai nainen? : "))
if sukupuoli=="mies":
    if hemoglob>=134 and hemoglob<=195:
        print("Normaali hemoglobiini")
    elif hemoglob>195:
        print("Korkea hemoglobiini")
    elif hemoglob<134:
        print("Alhainen hemoglobiini")
if sukupuoli=="nainen":
    if hemoglob >= 117 and hemoglob <= 175:
        print("Normaali hemoglobiini")
    elif hemoglob>175:
        print("Korkea hemoglobiini")
    elif hemoglob<117:
        print("Alhainen hemoglobiini")