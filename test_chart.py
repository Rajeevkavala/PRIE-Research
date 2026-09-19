import win32com.client
import time
import os

word = win32com.client.Dispatch('Word.Application')
word.Visible = False
try:
    doc = word.Documents.Add()
    rng = doc.Range(0, 0)
    # xlColumnClustered = 51
    shape = doc.InlineShapes.AddChart2(-1, 51, rng)
    chart = shape.Chart
    cd = chart.ChartData
    cd.Activate()
    time.sleep(1.0)
    wb = cd.Workbook
    ws = wb.Worksheets(1)
    
    categories = ['Accuracy', 'Specificity', 'Precision', 'Recall', 'F1 score']
    series_names = ['LogReg', 'RandForest', 'XGB-Base', 'Proposed']
    logreg = [99.20, 98.41, 99.21, 99.73, 98.92]
    rf = [89.60, 74.60, 88.39, 99.20, 83.87]
    xgb_base = [94.80, 87.30, 94.42, 98.94, 92.66]
    prop = [94.60, 88.10, 94.63, 98.40, 92.45]
    
    rows = [["Metric"] + series_names]
    for i, cat in enumerate(categories):
        rows.append([cat, logreg[i], rf[i], xgb_base[i], prop[i]])
        
    num_rows = len(rows)
    num_cols = len(rows[0])
    
    ws.UsedRange.Clear()
    top_left = ws.Cells(1, 1)
    bot_right = ws.Cells(num_rows, num_cols)
    ws.Range(top_left, bot_right).Value = rows
    
    addr = ws.Range(top_left, bot_right).Address
    chart.SetSourceData(f"='{ws.Name}'!{addr}")
    chart.HasTitle = False
    chart.HasLegend = True
    
    # Set Y axis min to 70 and max to 100
    try:
        val_axis = chart.Axes(2) # xlValue = 2
        val_axis.MinimumScale = 70
        val_axis.MaximumScale = 100
    except Exception as e:
        print("Axis scale note:", e)
        
    wb.Close(True)
    
    test_path = r"d:\4-1 AD\All College Docs and ppts\Documentations\PDR\PRIE-Research\test_bar_chart.docx"
    doc.SaveAs2(test_path)
    doc.Close(False)
    print("SUCCESS! Created bar chart:", test_path)
finally:
    word.Quit()
