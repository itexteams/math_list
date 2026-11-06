import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang66_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dữ liệu các trường hợp bài toán có thể sinh ra để đảm bảo phân hoạch đúng
                target_data = {
                    2.5: {
                        'parts': [
                            [1.0, 1.0, 0.5, 0.0],
                            [1.0, 1.0, 0.25, 0.25],
                            [1.0, 0.5, 0.5, 0.5]
                        ],
                        'k_options': [1, 2]
                    },
                    3.0: {
                        'parts': [
                            [1.0, 1.0, 1.0, 0.0],
                            [1.0, 1.0, 0.5, 0.5]
                        ],
                        'k_options': [2, 3]
                    }
                }

                # Random tổng điểm T và số câu đạt 1 điểm (k)
                T = random.choice([2.5, 3.0])
                k = random.choice(target_data[T]['k_options'])
                partitions = target_data[T]['parts']

                # Hàm định dạng số theo chuẩn Việt Nam (dấu phẩy)
                def fmt(v):
                    return str(v).replace('.', ',') if v != int(v) else str(int(v))

                def fmt_rounded(val):
                    s = f"{val:.2f}"
                    return s.replace('.', ',')

                # Xử lý sinh tự động các trường hợp chi tiết của lời giải
                cases_text_list = []
                total_omega = 0
                fav_total = 0
                fav_sum_parts = []
                sum_parts = []

                for idx, partition in enumerate(partitions):
                    case_num = idx + 1
                    freq = {}
                    for p in partition:
                        freq[p] = freq.get(p, 0) + 1

                    sorted_keys = sorted(list(freq.keys()), reverse=True)

                    perms = 24
                    for v in freq.values():
                        perms //= math.factorial(v)

                    ways_map = {1.0: 1, 0.5: 4, 0.25: 6, 0.1: 4, 0.0: 1}

                    ans_parts = []
                    ans_expr_parts = []
                    ways = perms
                    for score in sorted_keys:
                        freq_v = freq[score]
                        ways_for_k = ways_map[score]
                        ans_parts.append(f"{freq_v} câu được {fmt(score)} điểm " + ("mỗi câu " if freq_v > 1 else "") + f"có {ways_for_k} cách")
                        ans_expr_parts.append(f"{ways_for_k}^{freq_v}")
                        ways *= (ways_for_k ** freq_v)

                    ans_str = " ; ".join(ans_parts)
                    ans_expr = ".".join(ans_expr_parts)

                    total_omega += ways
                    sum_parts.append(str(ways))

                    ones = sum(1 for p in partition if p == 1.0)
                    if ones == k:
                        fav_total += ways
                        fav_sum_parts.append(str(ways))

                    set_str = "\\{" + "; ".join(fmt(x) for x in partition) + "\\}"

                    choose_parts = []
                    for score in sorted_keys:
                        v = freq[score]
                        choose_parts.append(f"{v} câu {fmt(score)} điểm")
                    if len(choose_parts) > 1:
                        choose_str = " và ".join([", ".join(choose_parts[:-1]), choose_parts[-1]])
                    else:
                        choose_str = choose_parts[0]

                    # Sinh chuỗi giải thích việc chọn vị trí giống y hệt mẫu
                    if len(freq) == 2:
                        vals = list(freq.values())
                        if set(vals) == {2}:
                            perm_text = f"Chọn {choose_str} nên số cách chọn là $C_4^2 = 6$"
                        elif set(vals) == {1, 3}:
                            perm_text = f"Chọn {choose_str} có số cách chọn là $C_4^1 = 4$"
                        else: 
                            fact_str = "".join([f"{v}!" for v in sorted(freq.values(), reverse=True)])
                            perm_text = f"Ta có 4 câu, chọn {choose_str}: \\\\\\\\\nSố cách xếp bộ điểm này là: $\\frac{{4!}}{{{fact_str}}} = {perms}$ (cách)"
                    else:
                        fact_str = "".join([f"{v}!" for v in sorted(freq.values(), reverse=True)])
                        perm_text = f"Ta có 4 câu, chọn {choose_str}: \\\\\\\\\nSố cách xếp bộ điểm này là: $\\frac{{4!}}{{{fact_str}}} = {perms}$ (cách)"

                    text = (f"\\textbf{{Trường hợp {case_num}:}} Bộ điểm ${set_str}$ \\\\\\\\\n"
                            f"Số cách chọn vị trí câu hỏi: {perm_text} \\\\\\\\\n"
                            f"Số cách chọn đáp án: {ans_str} \\\\\\\\\n"
                            f"Tổng số cách ở trường hợp này là ${perms}.({ans_expr}) = {ways}$ (cách)")
                    cases_text_list.append(text)

                dynamic_cases_str = "\\\\\\\\\n".join(cases_text_list)
                sum_str = " + ".join(sum_parts)
                fav_sum_str = " + ".join(fav_sum_parts) if fav_sum_parts else "0"

                # Tính xác suất
                P_val = fav_total / total_omega
                ans_correct = round(P_val, 2)

                # Tạo bảng quy tắc bằng TikZ
                tikz_img = ('''\\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\fill[blue!10] (0, 2) rectangle (1, 2.6);
            \\fill[blue!10] (1, 2) rectangle (2, 2.6);
            \\draw (0, 2) rectangle (1, 2.6) node[midway, blue, font=\\bfseries] {Đúng};
            \\draw (1, 2) rectangle (2, 2.6) node[midway, blue, font=\\bfseries] {Sai};
            \\foreach \\y in {0, 0.5, 1.0, 1.5} {
                \\fill[yellow!20] (0, \\y) rectangle (1, \\y+0.5);
                \\fill[green!20] (1, \\y) rectangle (2, \\y+0.5);
                \\draw (0, \\y) rectangle (1, \\y+0.5);
                \\draw (1, \\y) rectangle (2, \\y+0.5);
                \\draw (0.35, \\y+0.15) rectangle (0.65, \\y+0.35);
                \\draw (1.35, \\y+0.15) rectangle (1.65, \\y+0.35);
            }
            \\node[right] at (2.5, 2.25) {$\\triangleright$ Đúng $01$ ý trong $04$ ý được $0,1$ điểm};
            \\node[right] at (2.5, 1.75) {$\\triangleright$ Đúng $02$ ý trong $04$ ý được $0,25$ điểm};
            \\node[right] at (2.5, 1.25) {$\\triangleright$ Đúng $03$ ý trong $04$ ý được $0,5$ điểm};
            \\node[right] at (2.5, 0.75) {$\\triangleright$ Đúng cả $04$ ý được $1$ điểm};
            \\node[right] at (2.5, 0.25) {$\\triangleright$ Không đúng ý nào trong cả $04$ ý thì không được điểm};
            \\end{tikzpicture}
            \\end{center}''')

                # Cấu trúc câu hỏi
                noidungcauhoi = ('''Phần trắc nghiệm đúng sai của đề thi THPT Quốc Gia gồm có $04$ câu hỏi. Mỗi câu hỏi sẽ gồm $04$ ý trắc nghiệm đúng sai a), b), c), d) và mỗi ý chỉ gồm hai lựa chọn là \\textbf{đúng} hoặc \\textbf{sai}. Quy tắc tính điểm của một câu hỏi đúng sai này như sau:
            %s
            Một học sinh khoanh bừa ngẫu nhiên tất cả các ý của $4$ câu hỏi. Biết rằng kết quả cuối cùng học sinh này đạt được tổng điểm là $%s$ điểm. Tính xác suất để trong $4$ câu hỏi đó có đúng $%s$ câu học sinh trả lời đúng hoàn toàn (Kết quả làm tròn đến hàng phần trăm).''' % (tikz_img, fmt(T), k))

                # Cấu trúc lời giải
                loigiai_intro = ('''Mỗi câu hỏi sẽ gồm $04$ ý trắc nghiệm đúng sai a), b), c), d) và mỗi ý chỉ gồm hai lựa chọn là \\textbf{đúng} hoặc \\textbf{sai}.\\\\
            Tổng số cách trả lời cho mỗi câu hỏi là: $2^4 = 16$ (cách)\\\\
            Số cách để đạt các mức điểm như sau:\\\\
            Được $1$ điểm khi đúng cả $4$ ý có $C_4^4 = 1$ (cách)\\\\
            Được $0,5$ điểm khi đúng $3$ ý có $C_4^3 = 4$ (cách)\\\\
            Được $0,25$ điểm khi đúng $2$ ý có $C_4^2 = 6$ (cách)\\\\
            Được $0,1$ điểm khi đúng $1$ ý có $C_4^1 = 4$ (cách)\\\\
            Được $0$ điểm khi không làm đúng ý nào có $C_4^0 = 1$ (cách)\\\\
            Các trường hợp đạt tổng $%s$ điểm:\\\\
            Gọi $x_1, x_2, x_3, x_4$ là điểm số của $4$ câu hỏi thì khi đó $x_1 + x_2 + x_3 + x_4 = %s$.\\\\''' % (fmt(T), fmt(T)))

                loigiai_outro = ('''Vậy không gian mẫu là $n(\\Omega) = %s = %s$ (cách).\\\\
            Gọi $A$ là biến cố ``Có đúng $%s$ câu đạt $1$ điểm'' nên $n(A) = %s = %s$.\\\\
            Vậy xác suất cần tìm là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} \\approx %s$.''' % (sum_str, total_omega, k, fav_sum_str, fav_total, fav_total, total_omega, fmt_rounded(ans_correct)))

                loigiai = loigiai_intro + "\\\\\n" + dynamic_cases_str + "\\\\\\\\\n" + loigiai_outro
                dapan='\\shortans[0]{$%s$}\n'%(fmt_rounded(ans_correct))
                # Tạo tập hợp đáp án nhiễu cực chuẩn
                distractors = set([0.51, 0.49, 0.42, 0.09, 0.23, 0.96, 0.04, 0.92, 0.88, 0.12, 0.75, 0.65])
                distractors.discard(ans_correct)
                wrong_choices = random.sample(list(distractors), 3)

                # Gắn đáp án
                da = fmt_rounded(ans_correct)
                da_d = ('\\True $%s$' % da)
                da_s1 = '$%s$' % fmt_rounded(wrong_choices[0])
                da_s2 = '$%s$' % fmt_rounded(wrong_choices[1]) 
                da_s3 = '$%s$' % fmt_rounded(wrong_choices[2]) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

