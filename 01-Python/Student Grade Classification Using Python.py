# -----------------------------
# Student Grade Classification
# -----------------------------

# Get marks from the user
physics = int(input("Enter Physics mark: "))
botany = int(input("Enter Botany mark: "))
zoology = int(input("Enter Zoology mark"))

# Display results              
print("---Results---")

# Physics Grade Evaluation
if physics >= 90 and physics <= 100:
    print("Physics mark : S Grade")
elif physics >= 80 and physics < 90:
    print("Physics mark : A Grade")
elif physics >= 70 and physics < 80:
    print("Physics mark : B Grade")
elif physics >= 60 and physics < 70:
    print("Physics mark : C Grade")
elif physics >= 55 and physics < 60:
    print("Physics : D Grade")
elif physics >= 50 and physics < 55:
    print("Physics : E Grade")
elif physics <= 50 and physics >= 0:
    print("Physics : Fail")
else:
    print("enter valid mark")

# Botany Grade Evaluation
if botany >= 90 and botany <= 100:
    print("Botany mark : S Grade")
elif botany >= 80 and botany < 90:
    print("Botany : A Grade")
elif botany >= 70 and botany < 80:
    print("Botany : B Grade")
elif botany >= 60 and botany < 70:
    print("Botany : C Grade")
elif botany >= 55 and botany < 60:
    print("Botany : D Grade")
elif botany >= 50 and botany < 55:
    print("Botany : E Grade")
elif botany <=50 and botany >= 0:
    print("Botany : Fail")
else:
    print("enter valid marks")

# Zoology Grade Evaluation
if zoology >= 90 and zoology <=100:
    print("Zoology : S Grade")
elif zoology >= 80 and zoology < 90:
    print("Zoology : A Grade")
elif zoology >= 70 and zoology < 80:
    print("Zoology : B Grade")
elif zoology >= 60 and zoology <70:
    print("Zoology : C Grade")
elif zoology >= 55 and zoology < 60:
    print("Zoology : D Grade")
elif zoology >= 50 and zoology < 55:
    print("Zoology : E Grade")
elif zoology <=50 and zoology >= 0:
    print("Zoology : Fail")
else:
    print("enter valid mark")

