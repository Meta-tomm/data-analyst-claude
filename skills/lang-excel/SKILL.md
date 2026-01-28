---
name: lang-excel
description: "Use when creating Excel formulas, Power Query, pivot tables, VBA, or Office Scripts. Advanced formulas, patterns, troubleshooting."
---

# Excel & Power Query

Best practices for Excel formulas, Power Query M, VBA, and Office Scripts.

## Formulas

### Lookup
```
=VLOOKUP(value, table, col_index, FALSE)
=INDEX(range, MATCH(value, lookup_range, 0))
=XLOOKUP(value, lookup_array, return_array, "Not Found")
```

### Conditional Aggregation
```
=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)
=COUNTIFS(range1, criteria1, range2, criteria2)
=AVERAGEIFS(avg_range, criteria_range, criteria)
```

### Text
```
=TEXTJOIN(", ", TRUE, range)
=TRIM(CLEAN(cell))
=LEFT(cell, FIND(" ", cell) - 1)
=SUBSTITUTE(cell, "old", "new")
```

### Date
```
=EOMONTH(date, 0)
=NETWORKDAYS(start, end, holidays)
=DATEDIF(start, end, "M")
=TEXT(date, "YYYY-MM-DD")
```

### Dynamic Arrays (Excel 365)
```
=FILTER(data, criteria_col = value)
=SORT(range, col_num, 1)
=UNIQUE(range)
=SORTBY(range, sort_range)
=SEQUENCE(rows, cols, start, step)
```

### Advanced
```
=LET(x, formula1, y, formula2, result_using_x_y)
=LAMBDA(param, expression)(value)
=MAP(array, LAMBDA(x, transform(x)))
=REDUCE(initial, array, LAMBDA(acc, x, acc + x))
```

## Power Query M

```m
let
    Source = Excel.CurrentWorkbook(){[Name="Table1"]}[Content],
    Filtered = Table.SelectRows(Source, each [Status] = "Active"),
    Grouped = Table.Group(Filtered, {"Category"}, {
        {"Total", each List.Sum([Amount]), type number},
        {"Count", each Table.RowCount(_), Int64.Type}
    }),
    Sorted = Table.Sort(Grouped, {{"Total", Order.Descending}})
in
    Sorted
```

### Common Transforms
```m
Table.RemoveColumns(table, {"Col1", "Col2"})
Table.RenameColumns(table, {{"OldName", "NewName"}})
Table.AddColumn(table, "NewCol", each [Col1] + [Col2])
Table.TransformColumnTypes(table, {{"Col", type number}})
Table.UnpivotOtherColumns(table, {"ID"}, "Attribute", "Value")
Table.NestedJoin(table1, "Key", table2, "Key", "Joined", JoinKind.LeftOuter)
```

## Pivot Tables Best Practices
1. Source data: no merged cells, no blanks in headers
2. Use Table format (Ctrl+T) for auto-expanding
3. Group dates by month/quarter/year
4. Calculated fields for custom metrics
5. Slicers for interactive filtering

## VBA Patterns (when needed)
```vba
Sub ProcessData()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Data")
    Dim lastRow As Long
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    Dim i As Long
    For i = 2 To lastRow
        ' Process each row
    Next i
End Sub
```

## Anti-Patterns
| Bad | Good |
|-----|------|
| Nested IF >3 levels | IFS() or SWITCH() |
| VLOOKUP | INDEX/MATCH or XLOOKUP |
| Volatile functions (INDIRECT) | Structured references |
| Merged cells | Center Across Selection |
| Hard-coded values | Named ranges |

## Language

Respond in the same language as the user.
