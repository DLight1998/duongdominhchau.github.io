#!/bin/python
import re

def readFile(path):
    with open(path, "r") as f:
        return f.read()

def processRow(rawRow):
    row = []
    for cell in re.findall('<td.*?>\s*(.+?)\s*</td>', rawRow, re.DOTALL):
        row += [ cell.replace("&nbsp;", " ").strip() ]
    return row

def singleRow(content, numColumns = 6, classes = ""):
    result = '<tr><td colspan="' + str(numColumns) + '"'
    if classes != "":
        result += ' class="' + classes + '"'
    result += '>'
    result += content
    result += '</td></tr>\n'
    return result

def semesterScores(heading, rows, summary):
    result = '<tr><td class="semester" colspan="6">' + heading + '</td></tr>\n'

    result += '<tr>\n'
    for cell in rows[0]:
        result += '    <th>' + cell + '</th>\n'
    result += '</tr>\n'

    for row in rows[1:]:
        result += '<tr class="data-row">\n'
        for cell in row:
            result += '    <td>' + cell + '</td>\n'
        result += '</tr>\n'
    for entry in summary:
        result += singleRow(entry)
    result += '\n'
    return result

rawInput = readFile("raw.html")

headingPattern = '<td class="main_1".*?>(.+?)</td>'
rowsPattern = '<table.+?((?:<tr.*?>.+?</tr>[^<]+)+).*?</table>'
pattern = headingPattern + '.*?' + rowsPattern
matches = re.findall(pattern, rawInput, re.DOTALL)

summaryPattern = '<table width="100%" height="100%".*?>(.+?)</table>'
rawSummaries = re.findall(summaryPattern, rawInput, re.DOTALL)

# Summary entries:
#     Tổng số tín chỉ đăng ký, Ðiểm trung bình học kỳ
#     Tổng số tín chỉ tích lũy học kỳ, Ðiểm trung bình tích lũy
#     Tổng số tín chỉ tích lũy, Ðiểm rèn luyện
summaries = []
label = None
for rawSummary in rawSummaries:
    summaries.append([])
    for cell in re.findall('<td.*?>(.+?)</td>', rawSummary, re.DOTALL):
        cell = cell.replace('&nbsp;', ' ').strip()
        if re.match('\d+(?:\.\d+)?', cell): # Value found
            summaries[-1].append(label + ': ' + cell)
            label = None
        else:
            label = cell
for i in range(0, len(matches) - len(summaries) + 1):
    summaries.append([
        "Tổng số tín chỉ đăng ký: n/a",
        "Ðiểm trung bình học kỳ: n/a",
        "Tổng số tín chỉ tích lũy học kỳ: n/a",
        "Ðiểm trung bình tích lũy: n/a",
        "Tổng số tín chỉ tích lũy: n/a",
        "Ðiểm rèn luyện: n/a",
    ])

output = ""
currentIndex = 0
for match in matches:
    rawHeading = match[0]
    rawRows = match[1]
    m = re.search('Học Kỳ (1|2|Hè).+?(20\d{2}).+?(20\d{2})', rawHeading)
    if m:
        semester = m.group(1)
        year = m.group(2) + '&ndash;' + m.group(3)
        heading = 'Học kỳ ' + semester + ' năm học ' + year
    else:
        continue
    rows = []
    for rawRow in re.findall('<tr>(.+?)</tr>', rawRows, re.DOTALL):
        rows += [ processRow(rawRow) ]
    rows[0] = ['STT', 'Mã học phần', 'Tên học phần', 'Số tín chỉ', 'Điểm số', 'Điểm chữ'] 
    for i in range(1, len(rows)):
        # Original columns:
        # 'Stt', 'Mã HP', 'Tên HP', 'Điều kiện', 'Nhóm',
        # 'Tín chỉ', 'Điểm chữ', 'Điểm số', 'Tích lũy'
        rows[i] = [ rows[i][k] for k in [0, 1, 2, 5, 6, 7] ]
    output += semesterScores(heading, rows, summaries[currentIndex])
    currentIndex += 1

template = readFile("template.html")
with open("Reorganized.html", "w") as f:
    f.write(template.replace("${TABLE_CONTENT}", output))
