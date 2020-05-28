`openpyxl`中获取活动工作表，之前一直用的是`wb.get_active_sheet()`，或者`wb.get_sheet_by_name('Sheet1')`，没想到今天一个都不管用了，错误提示是：



> ```
> AttributeError: 'Workbook' object has no attribute 'get_active_sheet'
> ```

试了别人会出问题的`wb.active`，倒是好了。去年还没有这个问题的呢，大概`openpyxl`升级了？？

