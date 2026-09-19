import docx
import win32com.client
import time
import os

test_docx = r"d:\4-1 AD\All College Docs and ppts\Documentations\PDR\PRIE-Research\test_multi_charts.docx"

# 1. Create base document with markers
doc = docx.Document()
doc.add_paragraph("Start of document")
doc.add_paragraph("[[CHART_5]]")
doc.add_paragraph("Between chart 5 and 6")
doc.add_paragraph("[[CHART_6]]")
doc.add_paragraph("Between chart 6 and 7")
doc.add_paragraph("[[CHART_7]]")
doc.add_paragraph("End of document")
doc.save(test_docx)

# 2. Open via Word COM and replace markers with native editable charts
word = win32com.client.Dispatch('Word.Application')
word.Visible = False

try:
    wdoc = word.Documents.Open(test_docx)
    
    # ── CHART 5: Accuracy Line Chart ──
    f5 = wdoc.Content.Find
    f5.ClearFormatting()
    if f5.Execute(FindText="[[CHART_5]]"):
        rng = f5.Parent
        rng.Text = ""
        shape = wdoc.InlineShapes.AddChart2(-1, 65, rng)
        shape.Width = 234
        shape.Height = 135
        chart = shape.Chart
        cd = chart.ChartData
        cd.Activate()
        time.sleep(0.5)
        wb = cd.Workbook
        ws = wb.Worksheets(1)
        ws.UsedRange.Clear()
        
        iters = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        train_acc = [55, 72, 83, 88, 91, 93, 94.5, 95.0, 95.2, 95.2, 95.2]
        test_acc = [50, 68, 78, 84, 88, 91, 93.2, 94.0, 94.6, 94.6, 94.6]
        
        rows = [["Iterations", "Training", "Testing"]]
        for it, tr, te in zip(iters, train_acc, test_acc):
            rows.append([str(it), tr, te])
            
        top_left = ws.Cells(1, 1)
        bot_right = ws.Cells(len(rows), len(rows[0]))
        ws.Range(top_left, bot_right).Value = rows
        addr = ws.Range(top_left, bot_right).Address
        chart.SetSourceData(f"='{ws.Name}'!{addr}")
        chart.HasTitle = False
        chart.HasLegend = True
        
        # Axes
        try:
            chart.Axes(1).HasTitle = True
            chart.Axes(1).AxisTitle.Text = "Boosting Iterations (Trees)"
            chart.Axes(2).HasTitle = True
            chart.Axes(2).AxisTitle.Text = "Accuracy (%)"
            chart.Axes(2).MinimumScale = 0
            chart.Axes(2).MaximumScale = 100
        except Exception as ex:
            print("Chart 5 axis note:", ex)
            
        wb.Close(True)
        print("Inserted native Chart 5")
        
    # ── CHART 6: Loss Line Chart ──
    f6 = wdoc.Content.Find
    f6.ClearFormatting()
    if f6.Execute(FindText="[[CHART_6]]"):
        rng = f6.Parent
        rng.Text = ""
        shape = wdoc.InlineShapes.AddChart2(-1, 65, rng)
        shape.Width = 234
        shape.Height = 135
        chart = shape.Chart
        cd = chart.ChartData
        cd.Activate()
        time.sleep(0.5)
        wb = cd.Workbook
        ws = wb.Worksheets(1)
        ws.UsedRange.Clear()
        
        iters = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        train_loss = [90, 38, 22, 15, 11, 8.5, 6.2, 4.8, 3.9, 3.5, 3.39]
        test_loss = [92, 42, 26, 18, 14, 11.0, 8.5, 6.8, 5.5, 4.2, 3.50]
        
        rows = [["Iterations", "Training", "Testing"]]
        for it, tr, te in zip(iters, train_loss, test_loss):
            rows.append([str(it), tr, te])
            
        top_left = ws.Cells(1, 1)
        bot_right = ws.Cells(len(rows), len(rows[0]))
        ws.Range(top_left, bot_right).Value = rows
        addr = ws.Range(top_left, bot_right).Address
        chart.SetSourceData(f"='{ws.Name}'!{addr}")
        chart.HasTitle = False
        chart.HasLegend = True
        
        try:
            chart.Axes(1).HasTitle = True
            chart.Axes(1).AxisTitle.Text = "Boosting Iterations (Trees)"
            chart.Axes(2).HasTitle = True
            chart.Axes(2).AxisTitle.Text = "Loss (%)"
            chart.Axes(2).MinimumScale = 0
            chart.Axes(2).MaximumScale = 100
        except Exception as ex:
            print("Chart 6 axis note:", ex)
            
        wb.Close(True)
        print("Inserted native Chart 6")

    # ── CHART 7: Clustered Column Chart ──
    f7 = wdoc.Content.Find
    f7.ClearFormatting()
    if f7.Execute(FindText="[[CHART_7]]"):
        rng = f7.Parent
        rng.Text = ""
        shape = wdoc.InlineShapes.AddChart2(-1, 51, rng)
        shape.Width = 234
        shape.Height = 150
        chart = shape.Chart
        cd = chart.ChartData
        cd.Activate()
        time.sleep(0.5)
        wb = cd.Workbook
        ws = wb.Worksheets(1)
        ws.UsedRange.Clear()
        
        categories = ['Accuracy', 'Specificity', 'Precision', 'Recall', 'F1 score']
        series_names = ['LogReg', 'RandForest', 'XGB-Base', 'Proposed']
        logreg = [99.20, 98.41, 99.21, 99.73, 98.92]
        rf = [89.60, 74.60, 88.39, 99.20, 83.87]
        xgb_base = [94.80, 87.30, 94.42, 98.94, 92.66]
        prop = [94.60, 88.10, 94.63, 98.40, 92.45]
        
        rows = [["Metric"] + series_names]
        for i, cat in enumerate(categories):
            rows.append([cat, logreg[i], rf[i], xgb_base[i], prop[i]])
            
        top_left = ws.Cells(1, 1)
        bot_right = ws.Cells(len(rows), len(rows[0]))
        ws.Range(top_left, bot_right).Value = rows
        addr = ws.Range(top_left, bot_right).Address
        chart.SetSourceData(f"='{ws.Name}'!{addr}")
        chart.HasTitle = False
        chart.HasLegend = True
        
        try:
            chart.Axes(2).HasTitle = True
            chart.Axes(2).AxisTitle.Text = "%"
            chart.Axes(2).MinimumScale = 70
            chart.Axes(2).MaximumScale = 100
        except Exception as ex:
            print("Chart 7 axis note:", ex)
            
        wb.Close(True)
        print("Inserted native Chart 7")

    wdoc.Save()
    wdoc.Close(False)
    print("SUCCESS! All 3 native editable charts inserted into Word doc!")
finally:
    word.Quit()
