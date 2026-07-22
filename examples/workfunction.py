from python.analysis import WorkFunctionAnalyzer

analyzer = WorkFunctionAnalyzer(
    locpot="LOCPOT",
    outcar="OUTCAR"
)

result = analyzer.analyze()

print(result)
